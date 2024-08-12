Authorization
=============

Authorization and Authentication in the GraphQL API is handled via JSON Web
Tokens. Please keep in mind that not all queries need authorization. The
token is mandatory for all mutations though and some fields are only accessible
with a valid token.

.. important::
   There is no server side session!

Consumer usage
--------------

Using only JWT access tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `graphql-base` module provides you with a `token` query that returns a JWT
to be used in future requests.

**Request:**

.. code-block:: graphql

    query {
        token (
            username: "admin",
            password: "admin"
        )
    }

**Response:**

.. code-block:: json

    {
        "data": {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        }
    }

This `token` is then to be sent in the HTTP `Authorization` header as a bearer
token.

.. code-block:: yaml

   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

If you want to have a brief look into the JWT you received head over
to `jwt.io <https://jwt.io>`_.

Using refresh tokens
^^^^^^^^^^^^^^

Refresh tokens add a layer of security to the authentication workflow of your clientside application.

Simply put, a refresh token is what the application uses instead of saving, or
asking for, the user's credentials. With this workflow, the access token can
(and should) be issued a much shorter lifespan without deteriorating user
experience through frequent login requests and provide security through rapid
iteration of the identification through which the API is accessed.

Typical lifetime of an access token should be from a few minutes to a few hours.
Refresh tokens should be a few days to a few months respectively.
These lifetimes are configurable in the `graphql-base` module settings.
The access token contains an expiration datetime under the `exp` JWT claim.

The workflow involves using two queries - `login` and `refresh`.
Logging in as a user should be done through the following query.

**Request:**

.. code-block:: graphql

   query ($username: String!, $password: String!) { login (username: $username, password: $password)
      {
         accessToken
         refreshToken
      }
   }

**Response:**

.. code-block:: json

   {
      "data": {
         "accessToken": "a-very-long-jwt-encoded-token"
         "refreshToken": "your-refresh-token"
      }
   }

An `HttpOnly` cookie, for token sidejack prevention, will be set, which the
client infrastructure should be able to handle appropriately. In the case of a
browser this means setting up the cookie for either cross origin or same origin
operation in the module settings. Along with the cookie, a `fingerprintHash`
claim is set in the JWT access token. This will need to be passed in the next
step.

After the access token's lifetime elapses it will need to be refreshed. The
`refresh` query looks as follows.

**Request:**

.. code-block:: graphql

   query {
      refresh (
         refreshToken: "your-refresh-token",
         fingerprintHash: "from-access-token-claims"
      )
   }

This request must have the `HttpOnly` fingerprint cookie set during login.
If both the token and the fingerprint-fingerprintHash pair are correct the
client will receive a new `accessToken` in the response payload, containing a
new `fingerprintHash` claim to go with a newly set `fingerprint` cookie.

**Response:**

.. code-block:: json

{
    "data": {
        "refresh": "a-new-very-long-jwt-encoded-token"
    }
}

For more examples of using refresh tokens in a frontend client scenario please
check out `hasura's sample code on the topic <https://github.com/hasura/jwt-guide>`_
as well as their `"Ultimate guide to handling JWTs on frontend clients" <https://hasura.io/blog/best-practices-of-using-jwt-with-graphql#silent-refresh>`_
which contains a more in-depth look on both the client and server side along
with graphical explanations of how all information flows between thefrontend
application and the authentication server.

Protect your queries/mutations/types
------------------------------------

In order to protect your own queries, mutations or types you may use GraphQLite's
build in `authentication and authorization <https://graphqlite.thecodingmachine.io/docs/authentication-authorization>`_
features.

The `graphql-base` module brings an authentication- and authorization service
implemented in ``OxidEsales\GraphQL\Base\Service\Authentication`` and
``OxidEsales\GraphQL\Base\Service\Authorization`` to connect the GraphQLite library
to OXID's security mechanism.

Authentication
^^^^^^^^^^^^^^

The authentication service is responsible for creating and validating the JSON
Web Token, as well as resolving the ``@Logged`` annoation.

.. literalinclude:: examples/ControllerWithLogged.php
   :language: php

Using the ``@Logged()`` annotations prevents consumers from using
your resolver without a valid JWT.

Authorization
^^^^^^^^^^^^^

For finer grained access control you may use the ``@Right()`` annotation to ask
if the token in use allows for a specific right. These rights are coupled to the
user group which will be stored in the token itself.

.. literalinclude:: examples/ControllerWithRights.php
   :language: php

In case you need to have more control on how the authorization service decides,
you may register a handler for the ``OxidEsales\GraphQL\Base\Event\BeforeAuthorization``
event and oversteer the result in your event subscriber, see :ref:`events-BeforeAuthorization`.

.. note::
   If the admin is created, it isn't assigned to the ``oxidadmin`` group by default. As the rights are
   dependent on the group, the user would have no special rights. Be sure the group is set.

.. important::

   We decided to show queries and mutations in the schema even if the user is unauthorized.
   This means that the ``@HideIfUnauthorized``-annotation shouldn't be used.

Map rights to groups
^^^^^^^^^^^^^^^^^^^^

In order to use the ``SEE_BASKET`` right as we have seen in the last example, we
need to map this right to a user group. For this to work we need to create a
``PermissionProvider`` in our module and register it with the ``graphql_permission_provider``
tag in our ``services.yaml`` file.

.. literalinclude:: examples/PermissionProvider.php
   :language: php
