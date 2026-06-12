==============
Error-Handling
==============

This page describes how client-aware errors are handled and returned by the
OXAPI. The goal is to provide consumers with precise, actionable error messages
(instead of generic ``Internal server error`` responses) while keeping the
approach type-safe, extendable by modules and compatible with the GraphQL
specification.

.. contents::
   :local:
   :depth: 2


Motivation
==========

Historically the OXAPI returned very generic error messages that did not point
to the actual cause of a problem. A query referencing a non-existing module id,
for example, produced only:

.. code-block:: json

   {
     "errors": [
       {
         "message": "Internal server error",
         "locations": [{ "line": 2, "column": 5 }],
         "path": ["moduleSettings"]
       }
     ]
   }

...for a request like:

.. code-block:: graphql

   query settings {
       moduleSettings(moduleId: "somenonexistingmodule") {
           name
           type
           supported
       }
   }

This is not a limitation of GraphQLite — it offers proper error handling. The
problem is that the underlying code did not provide the necessary context to the
exceptions. A good error message, by contrast, looks like this (GraphQL standard
syntax validation):

.. code-block:: json

   {
     "errors": [
       {
         "message": "Cannot query field \"title_de\" on type \"Product\". Did you mean \"title\"?",
         "locations": [{ "line": 3, "column": 5 }]
       }
     ]
   }


Goals / Acceptance Criteria
===========================

The error-handling solution must satisfy the following criteria:

* Errors are returned with a **unique code** and a **short, human-readable
  message**.
* Errors are **extendable with type-specific fields** (e.g. an ``id`` field for
  *NotFound* errors), and those fields can be queried.
* **Multiple modules** can extend the codes and add new GraphQL errors for an
  existing mutation.
* If multiple modules extend a mutation, the implementations **must not cancel
  each other out** — the same mutation should run the code of all modules and all
  errors should be handled.
* The more **type-safe**, the better: having errors as types in the schema makes
  it clear that ``code`` and ``message`` always exist.
* **HTTP status codes** correspond to where the error originates from
  (``4xx`` for client errors such as syntax errors or id mismatches, ``5xx`` for
  real server errors or unimplemented methods). These are already set correctly
  according to the GraphQL specification.


Error-Handling Concepts (Background)
====================================

Best practice for GraphQL error handling:

* Each error contains a **message** (for the developer) and a **code** (numeric
  or alphanumeric — it only needs to be unique for identification).
* Errors can be returned either as a **payload** or as a single **union type**.
* The message shown to the end user is decided by the **frontend**, based on the
  error code.

``ClientAwareInterface`` in the shop
------------------------------------

A general interface would prevent catching the specific exceptions and raising
specific error codes, so a generic ``ClientAwareInterface`` is not the right
tool here.

Knowing which exceptions can occur
----------------------------------

Every method (including those in the shop) should carry a ``@throws`` tag listing
all exceptions thrown but not caught — both for the method itself and for the
methods it calls. For example: if a service uses a repository method and the
repository throws an exception without catching it, that exception is added to
the ``@throws`` tag of the repository method **and** of the service method (and
so on up the chain).

With correct ``@throws`` tags it becomes possible to know the throwable
exceptions, catch them, and create a concrete GraphQL error including message and
code.


Evaluated Approaches
====================

Three approaches were evaluated during the spike.

Payload
-------

A dedicated payload type wraps the actual result together with a
``userErrors`` list.

**Advantages**

* Multiple error messages can be returned at once.
* The query is always the same (no union types to expand).
* Less schema complexity.

**Disadvantages**

* Less type-safety than union types.
* Uniqueness of codes has to be ensured manually.
* Multiple errors are rarely necessary and harder to handle.
* Each data type needs a separate ``userErrors`` field.

.. code-block:: graphql

   mutation {
     adminProductCreate(adminProductInput: { id: "newProduct" }) {
       id
     }
   }

.. code-block:: json

   {
     "data": {
       "productCreate": {
         "product": null,
         "userErrors": [
           { "code": "PRODUCT_ID_ALREADY_EXIST", "message": "A Product with the provided id already exists" }
         ]
       }
     }
   }

Union Types
-----------

The mutation returns a union of the success data type and one or more error
types.

**Advantages**

* Type-safe.
* Uniqueness of errors is guaranteed by the union type itself.
* Out-of-the-box handling of errors (the existing data type stays untouched).
* Errors can be categorised (Validation, Authorization, Server Errors).
* Depending on the structure, codes are optional (because the error type already
  identifies the error).

**Disadvantages**

* Only a single error message can be returned.
* More schema complexity.

.. code-block:: graphql

   mutation {
     adminProductCreate(input: { id: "newProduct" }) {
       __typename
       ... on AdminProductDataType {
         id
         title
       }
       ... on ValidationError {
         code
         message
         field
       }
       ... on AlreadyExistError {
         code
         message
         id
       }
     }
   }

.. code-block:: json

   {
     "data": {
       "adminProductCreate": {
         "__typename": "AlreadyExistError",
         "code": "oe.already_exist.product",
         "message": "A Product with id 'cool-id' already exists",
         "id": "cool-id"
       }
     }
   }

References:

* https://dev.to/mnove/better-graphql-error-handling-with-typed-union-responses-1e1n
* https://blog.logrocket.com/handling-graphql-errors-like-a-champ-with-unions-and-interfaces/
* https://graphql.wtf/episodes/30-graphql-error-handling-with-union-types

GraphQLite ClientAware
----------------------

Errors are returned in the standard top-level ``errors`` array, with a code in
the ``extensions``.

**Advantages**

* Less schema complexity.
* The query is always the same (no union types).
* Out-of-the-box handling of errors (the existing data type stays untouched).

**Disadvantages**

* Less type-safe.
* Uniqueness of codes has to be ensured manually.
* Only a single error message can be returned.

.. code-block:: graphql

   mutation {
     adminProductCreate(adminProductInput: { id: "newProduct" }) {
       id
     }
   }

.. code-block:: json

   {
     "errors": [
       {
         "message": "A Product with the provided id already exists",
         "extensions": { "code": "PRODUCT_ID_ALREADY_EXIST" }
       }
     ]
   }


Chosen Approach: Payload
========================

The **Payload** approach is used because it fits all acceptance criteria.

* **Union types** fail on extendability: to return new/different errors from
  another module, the controller would have to be adjusted, which results in a
  new mutation/query per module. The frontend would then face *n* queries /
  mutations that all do the base functionality plus the module-specific error
  handling — an unmanageable state.
* **ClientAware** errors have almost zero type-safety. Extensions could carry
  additional data such as a code or id, but only the message is guaranteed —
  none of this is visible in the schema.

Type-safety with the Payload approach is not 100% (you cannot enforce specific
errors for a given query/mutation), but the frontend knows from the schema that
every result (payload) may contain one or more errors, each with a ``code`` and a
``message``.


Implementation (PHP)
====================

Data Types
----------

.. code-block:: php

   /** @Type() */
   interface UserErrorInterface
   {
       /** @Field() */
       public function code(): string;

       /** @Field() */
       public function message(): string;
   }

   /** @Type() */
   final class UserError implements UserErrorInterface
   {
       public function __construct(
           private string $code,
           private string $message,
       ) {
       }

       /** @Field() */
       public function code(): string
       {
           return $this->code;
       }

       /** @Field() */
       public function message(): string
       {
           return $this->message;
       }
   }

   interface PayloadInterface
   {
       /** @return UserErrorInterface[] */
       public function userErrors(): array;
   }

   interface LoginPayloadInterface extends PayloadInterface
   {
       public function login(): ?LoginInterface;
   }

   /** @Type() */
   final class LoginPayload implements LoginPayloadInterface
   {
       /** @param UserErrorInterface[] $userErrors */
       public function __construct(
           private ?LoginInterface $login,
           private array $userErrors = [],
       ) {
       }

       /** @Field() */
       public function login(): ?LoginInterface
       {
           return $this->login;
       }

       /**
        * @Field()
        * @return UserErrorInterface[]
        */
       public function userErrors(): array
       {
           return $this->userErrors;
       }
   }

Service
-------

The service catches the known exceptions and turns them into ``UserError``
entries instead of letting them bubble up as generic errors.

.. code-block:: php

   public function login(?string $userName, ?string $password): LoginPayload
   {
       try {
           $user = $this->legacyInfrastructure->login($userName, $password);

           return new LoginPayload(
               new LoginDatatype(
                   refreshToken: $this->refreshTokenService->createRefreshTokenForUser($user),
                   accessToken: $this->tokenService->createTokenForUser($user),
               ),
           );
       } catch (InvalidLogin $e) {
           return new LoginPayload(
               null,
               [new UserError('oegqlb.login.invalid', 'Username/password combination is invalid')],
           );
       }
   }

Controller
----------

.. code-block:: php

   /**
    * Query of Base Module.
    * Retrieve a refresh token and access token.
    *
    * @Query(outputType="LoginPayload")
    */
   public function login(?string $username = null, ?string $password = null): LoginPayloadInterface
   {
       return $this->loginService->login($username, $password);
   }


Generated Schema
================

.. code-block:: graphql

   interface UserErrorInterface {
       code: String!
       message: String!
   }

   type UserError implements UserErrorInterface {
       code: String!
       message: String!
   }

   type Login {
       accessToken: String!
       refreshToken: String!
   }

   type LoginPayload {
       login: Login
       userErrors: [UserErrorInterface]!
   }

   type Query {
       login(username: String, password: String): LoginPayload!
   }


Requests and Responses
======================

Basic request
-------------

.. code-block:: graphql

   query {
     login(username: "admin", password: "admin") {
       login {
         accessToken
         refreshToken
       }
       userErrors {
         code
         message
       }
     }
   }

Request with an extra error field
----------------------------------

Type-specific fields (e.g. an ``id`` on a ``NotFoundError``) can be queried via
inline fragments:

.. code-block:: graphql

   query {
     login(username: "admin", password: "admin") {
       login {
         accessToken
         refreshToken
       }
       userErrors {
         code
         message
         ... on NotFoundError {
           id
         }
       }
     }
   }

Response — success
------------------

.. code-block:: json

   {
     "data": {
       "login": {
         "login": {
           "accessToken": "eyJ0eXAiOiJKV1Q...",
           "refreshToken": "def50200..."
         },
         "userErrors": []
       }
     }
   }

Response — failure
------------------

.. code-block:: json

   {
     "data": {
       "login": {
         "login": null,
         "userErrors": [
           {
             "code": "INVALID_LOGIN",
             "message": "Username/password combination is invalid"
           }
         ]
       }
     }
   }


Frontend i18n
=============

The frontend resolves the user-facing text from the error code via translation
keys:

.. code-block:: text

   t(`errors.${result.code}`)
   // -> "The product with ID 'abc123' was not found"


Extending Errors in Modules
===========================

Modules can extend an existing flow with new exceptions and surface them as
meaningful errors. The example below adds a ``TwoFactorRequiredException`` from a
security module.

Without handling, the GraphQL login query would return a generic
``Internal Server Error``. To show a meaningful error, the login service must
also handle the new exception. This is done via **decoration (composition)**.

LoginServiceDecorator
---------------------

.. code-block:: php

   class LoginServiceDecorator extends LoginService
   {
       public function __construct(
           private LoginServiceInterface $inner,
       ) {
       }

       public function login(?string $userName, ?string $password): LoginPayload
       {
           try {
               return $this->inner->login($userName, $password);
           } catch (TwoFactorRequiredException $e) {
               return new LoginPayload(
                   null,
                   [new UserError('oesm.login.2fa_required', '2FA authentication required.')],
               );
           }
       }
   }

services.yaml
-------------

.. code-block:: yaml

   OxidEsales\GraphQL\Customer\Service\LoginService:
     decorates: OxidEsales\GraphQL\Base\Service\LoginServiceInterface
     arguments:
       $inner: '@.inner'

With this decoration the login process in GraphQL is extended, and the existing
controller transparently uses the new decorated ``login`` method. If the GraphQL
module is not activated together with the security module (i.e. the
``LoginServiceInterface`` does not exist), the decoration is simply ignored.

To return a different error — optionally with extra fields — the new error only
needs to implement ``UserErrorInterface``. Its additional fields can then be
fetched with fragments (see *Request with an extra error field* above).

Restrictions
------------

* Only **composition** (``@.inner``) must be used, to ensure that several
  modules can extend the service without breaking the decoration chain.


Notes
=====

* The union type used for extra error fields is generated automatically by
  GraphQLite. Its name consists of the ``Union`` prefix, the query/mutation name,
  and **all** possible return types. The naming strategy can be adjusted within
  the ``SchemaFactory``.
