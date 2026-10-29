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
   :class: graphql-sdl

   query settings {
       moduleSettings(moduleId: "somenonexistingmodule") {
           name
           type
           supported
       }
   }

This is not a limitation of GraphQLite — it offers proper error handling. The
problem is that the underlying shop did not provide the necessary context to the
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

The message above is still not perfect, because it misses information about the
context for the frontend. The error-handling solution must satisfy the following
criteria:

* Errors are returned with a **unique code** and a **short, human-readable
  message**.
* Errors are **extendable with type-specific fields** (e.g. an ``identifier``
  field for *NotFound* errors), and those fields can be queried.
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
   :class: graphql-sdl

   mutation {
     adminProductCreate(adminProductInput: { id: "newProduct" }) {
       adminProduct {
         id
       }
       userErrors {
         code
         message
       }
     }
   }

.. code-block:: json

   {
     "data": {
       "adminProductCreate": {
         "adminProduct": null,
         "userErrors": [
           { "code": "oegqlsa.id_already_exists.product", "message": "A product with the provided ID already exists." }
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
   :class: graphql-sdl

   mutation {
     adminProductCreate(adminProductInput: { id: "newProduct" }) {
       __typename
       ... on AdminProductDataType {
         id
         title
       }
       ... on ValidationError {
         code
         message
         value
       }
       ... on IdAlreadyExistsError {
         code
         message
         identifier
       }
     }
   }

.. code-block:: json

   {
     "data": {
       "adminProductCreate": {
         "__typename": "IdAlreadyExistsError",
         "code": "oegqlsa.id_already_exists.product",
         "message": "A product with the provided ID already exists.",
         "identifier": "newProduct"
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
   :class: graphql-sdl

   mutation {
     adminProductCreate(adminProductInput: { id: "newProduct" }) {
       id
     }
   }

.. code-block:: json

   {
     "errors": [
       {
         "message": "A product with the provided ID already exists.",
         "extensions": { "code": "oegqlsa.id_already_exists.product" }
       }
     ]
   }


Chosen Approach: Payload
========================

The **Payload** approach is used because it fits all acceptance criteria —
combined with a mix of union types for specific errors and their type-specific
fields.

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
``message``. And when specific errors are needed, fragments help to query the
specific fields for the specific errors.


Implementation (PHP)
====================

Error DataTypes
---------------

Every error implements ``ErrorInterface``. The shared ``code``/``message``
handling lives in ``AbstractError``, so a concrete Error DataType only needs to
add its type-specific fields (e.g. ``value`` on ``ValidationError``) — or nothing
at all when ``code`` and ``message`` suffice (e.g. ``AuthenticationError``).

.. code-block:: php

   #[Type]
   interface ErrorInterface
   {
       #[Field]
       public function code(): string;

       #[Field]
       public function message(): string;
   }

   abstract class AbstractError implements ErrorInterface
   {
       public function __construct(
           private readonly string $code,
           private readonly string $message,
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

   /**
    * @Type()
    */
   final class ValidationError extends AbstractError
   {
       public const FINGERPRINT = 'oegqlb.validation.fingerprint';

       public function __construct(
           string $code,
           private readonly string $value = '',
       ) {
           parent::__construct($code, $this->messages()[$code]);
       }

       /** @Field() */
       public function value(): string
       {
           return $this->value;
       }

       /** @return array<string, string> */
       private function messages(): array
       {
           return [
               self::FINGERPRINT => 'The fingerprint validation failed.',
           ];
       }
   }

   /**
    * @Type()
    */
   final class AuthenticationError extends AbstractError
   {
       public const CREDENTIALS_INCORRECT = 'oegqlb.authentication.credentials_incorrect';
       public const TOKEN_QUOTA_EXCEEDED = 'oegqlb.authentication.token_quota_exceeded';

       public function __construct(string $code)
       {
           parent::__construct($code, $this->messages()[$code]);
       }

       /** @return array<string, string> */
       private function messages(): array
       {
           return [
               self::CREDENTIALS_INCORRECT => 'The provided credentials are invalid.',
               self::TOKEN_QUOTA_EXCEEDED => 'The token quota for this user has been exceeded.',
           ];
       }
   }

Payloads
--------

A payload carries the actual result together with a ``userErrors`` list. The
shared ``userErrors`` handling lives in ``AbstractPayload``; a concrete payload
(here: ``LoginPayload``) only adds its result field.

.. code-block:: php

   interface PayloadInterface
   {
       /** @return ErrorInterface[] */
       public function userErrors(): array;
   }

   abstract class AbstractPayload implements PayloadInterface
   {
       /** @param ErrorInterface[] $userErrors */
       public function __construct(
           private readonly array $userErrors = [],
       ) {
       }

       /**
        * @Field()
        * @return ErrorInterface[]
        */
       public function userErrors(): array
       {
           return $this->userErrors;
       }
   }

   interface LoginPayloadInterface extends PayloadInterface
   {
       public function login(): ?LoginInterface;
   }

   /** @Type() */
   final class LoginPayload extends AbstractPayload implements LoginPayloadInterface
   {
       /** @param ErrorInterface[] $userErrors */
       public function __construct(
           private readonly ?LoginInterface $login,
           array $userErrors = [],
       ) {
           parent::__construct($userErrors);
       }

       /** @Field() */
       public function login(): ?LoginInterface
       {
           return $this->login;
       }
   }

Service
-------

The service contains the business logic and throws typed exceptions — it does
**not** know about GraphQL errors or payloads.

.. code-block:: php

   /**
    * @throws InvalidLogin
    * @throws TokenQuota
    */
   public function login(?string $userName, ?string $password): LoginInterface
   {
       $user = $this->legacyInfrastructure->login($userName, $password);

       return new LoginDatatype(
           refreshToken: $this->refreshTokenService->createRefreshTokenForUser($user),
           accessToken: $this->tokenService->createTokenForUser($user),
       );
   }

ExceptionConverter
------------------

The ``ExceptionConverter`` sits between the controller and the service. It
catches the known exceptions thrown by the service and converts them into
``ErrorInterface`` instances. Its return type is a union of the service's
success type and ``ErrorInterface``.

.. code-block:: php

   class LoginExceptionConverter implements LoginExceptionConverterInterface
   {
       public function __construct(
           private readonly LoginServiceInterface $loginService,
       ) {
       }

       public function login(?string $userName, ?string $password): LoginInterface|ErrorInterface
       {
           try {
               return $this->loginService->login($userName, $password);
           } catch (InvalidLogin) {
               return new AuthenticationError(AuthenticationError::CREDENTIALS_INCORRECT);
           } catch (TokenQuota) {
               return new AuthenticationError(AuthenticationError::TOKEN_QUOTA_EXCEEDED);
           }
       }
   }

The converter is registered as a Symfony service mapping the interface to the
concrete class:

.. code-block:: yaml

   # services.yaml
   OxidEsales\GraphQL\Base\ExceptionConverter\LoginExceptionConverterInterface:
       class: OxidEsales\GraphQL\Base\ExceptionConverter\LoginExceptionConverter

Controller
----------

The controller calls the converter and checks whether the result is an error:

.. code-block:: php

   /**
    * Query of Base Module.
    * Retrieve a refresh token and access token.
    *
    * @Query(outputType="LoginPayload")
    */
   public function login(?string $username = null, ?string $password = null): LoginPayloadInterface
   {
       $result = $this->loginExceptionConverter->login($username, $password);

       if ($result instanceof ErrorInterface) {
           return new LoginPayload(null, [$result]);
       }

       return new LoginPayload($result);
   }


Generated Schema
================

.. code-block:: graphql
   :class: graphql-sdl

   interface ErrorInterface {
       code: String!
       message: String!
   }

   type ValidationError implements ErrorInterface {
       code: String!
       message: String!
       value: String!
   }

   type AuthenticationError implements ErrorInterface {
       code: String!
       message: String!
   }

   interface LoginInterface {
       accessToken: String!
       refreshToken: String!
   }

   type LoginPayload {
       login: LoginInterface
       userErrors: [ErrorInterface!]!
   }

   type Query {
       login(username: String, password: String): LoginPayload
   }


Requests and Responses
======================

Basic request
-------------

.. code-block:: graphql
   :class: graphql-sdl

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

.. _eh-extra-error-field:

Request with an extra error field
----------------------------------

Type-specific fields (e.g. a ``value`` on a ``ValidationError``) can be
queried via inline fragments:

.. code-block:: graphql
   :class: graphql-sdl

   query {
     login(username: "admin", password: "admin") {
       login {
         accessToken
         refreshToken
       }
       userErrors {
         code
         message
         ... on ValidationError {
           value
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
             "code": "oegqlb.authentication.credentials_incorrect",
             "message": "The provided credentials are invalid."
           }
         ]
       }
     }
   }


.. _eh-consume-by-type:

Consuming errors: check the type, not the code
==============================================

Because every error is an explicit **type** in the schema, a consumer does
**not** parse or pattern-match the ``code`` string to find out *what kind* of
error occurred — the type already carries that information:

* **Frontend (GraphQL):** branch on ``__typename`` and read the type-specific
  fields via inline fragments.
* **Backend (PHP):** branch with ``instanceof`` on the concrete Error DataType
  (or on ``ErrorInterface`` to detect "any error at all").

The ``code`` is then only needed for the *finer* sub-reason within a type and to
resolve the user-facing message — never to determine the error category.

.. code-block:: typescript

   for (const error of result.userErrors) {
     switch (error.__typename) {          // check the TYPE, not the code
       case "NotFoundError":   return showNotFound(error.identifier);
       case "ValidationError": return highlightField(error.value);
       default:                return showGeneric(error.message);
     }
   }

Without typed errors the consumer would instead have to parse the ``code``
string (split ``oegqlb.not_found.token`` or match code prefixes) to recover the
same categorisation — fragile, and easy to break when codes change.


Frontend i18n
=============

Once the error **type** has decided *how* to handle the error (see
:ref:`eh-consume-by-type`), the ``code`` is used only to resolve the localized,
user-facing text — it is **not** the discriminator. The frontend maps the code
to a translation key:

.. code-block:: text

   t(`errors.${result.code}`)
   // -> "The product with ID 'abc123' was not found"


Extending Errors in Modules
===========================

Modules can extend an existing flow with new exceptions and surface them as
meaningful errors. The example below adds a ``TwoFactorRequiredException`` from a
security module.

Without handling, the GraphQL login query would return a generic
``Internal Server Error``. To show a meaningful error, the **ExceptionConverter**
must also handle the new exception. This is done via **decoration (composition)**
of the converter's interface.

The base ``AuthenticationError`` only knows its own codes and assigns the message
in its constructor, so it cannot be reused for a module-specific code. Instead the
module ships its own Error DataType — it only needs to implement ``ErrorInterface``
(here via ``AbstractError``) and assign its own code and message.

TwoFactorRequiredError
----------------------

.. code-block:: php

   /**
    * @Type()
    */
   final class TwoFactorRequiredError extends AbstractError
   {
       public const TWO_FA_REQUIRED = 'oesm.login.2fa_required';

       public function __construct(string $code)
       {
           parent::__construct($code, $this->messages()[$code]);
       }

       /** @return array<string, string> */
       private function messages(): array
       {
           return [
               self::TWO_FA_REQUIRED => '2FA authentication required.',
           ];
       }
   }

LoginExceptionConverterDecorator
---------------------------------

.. code-block:: php

   class LoginExceptionConverterDecorator implements LoginExceptionConverterInterface
   {
       public function __construct(
           private LoginExceptionConverterInterface $inner,
       ) {
       }

       public function login(?string $userName, ?string $password): LoginInterface|ErrorInterface
       {
           try {
               return $this->inner->login($userName, $password);
           } catch (TwoFactorRequiredException) {
               return new TwoFactorRequiredError(TwoFactorRequiredError::TWO_FA_REQUIRED);
           }
       }
   }

services.yaml
-------------

.. code-block:: yaml

   OxidEsales\GraphQL\Customer\Service\LoginExceptionConverterDecorator:
     decorates: OxidEsales\GraphQL\Base\ExceptionConverter\LoginExceptionConverterInterface
     arguments:
       $inner: '@.inner'

With this decoration the login process in GraphQL is extended, and the existing
controller transparently uses the new decorated converter. If the
``LoginExceptionConverterInterface`` does not exist (i.e. the graphql-base
module isn't activated), the decoration is simply ignored.

To return a different error — optionally with extra fields — the new error only
needs to implement ``ErrorInterface``. Its additional fields can then be
fetched with fragments (see :ref:`Request with an extra error field
<eh-extra-error-field>` above).


Notes
=====

* Only **composition** (``@.inner``) must be used, to ensure that several
  modules can extend exception-converter without breaking the decoration chain.
