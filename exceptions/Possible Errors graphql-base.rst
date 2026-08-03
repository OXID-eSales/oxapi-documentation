========================================================================
Possible Errors per Query/Mutation — graphql-base
========================================================================

This page lists every GraphQL **query** and **mutation** of the ``graphql-base``
module and the Error DataTypes (including their codes and messages) that can
appear in the operation's payload ``userErrors`` array.

.. note::
   Only errors returned as part of the payload's ``userErrors`` are listed here.
   A failing authentication/authorization check is returned as a **top-level**
   GraphQL error (not inside ``userErrors``) and is therefore not part of the
   tables below.

   All codes are prefixed with ``oegqlb.``. See :doc:`Error DataTypes` for the
   full type/field reference.

.. contents::
   :local:
   :depth: 1


``token``
---------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-validation-error>`
     - ``oegqlb.validation.credentials``
     - The provided credentials are invalid.
   * - :ref:`AuthenticationError <edt-authentication-error>`
     - ``oegqlb.authentication.token_quota_exceeded``
     - The token quota for this user has been exceeded.

``login``
---------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-validation-error>`
     - ``oegqlb.validation.credentials``
     - The provided credentials are invalid.
   * - :ref:`AuthenticationError <edt-authentication-error>`
     - ``oegqlb.authentication.token_quota_exceeded``
     - The token quota for this user has been exceeded.

``tokens``
----------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`AuthorizationError <edt-authorization-error>`
     - ``oegqlb.authorized.view_token``
     - You are not authorized to view this token.

``refresh``
-----------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-validation-error>`
     - ``oegqlb.validation.fingerprint``
     - The fingerprint validation failed.
   * - :ref:`ValidationError <edt-validation-error>`
     - ``oegqlb.validation.refresh_token``
     - The provided refresh token is invalid.
   * - :ref:`AuthenticationError <edt-authentication-error>`
     - ``oegqlb.authentication.token_quota_exceeded``
     - The token quota for this user has been exceeded.

``customerTokensDelete``
------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`AuthorizationError <edt-authorization-error>`
     - ``oegqlb.authorized.delete_token``
     - You are not authorized to delete this token.
   * - :ref:`NotFoundError <edt-not-found-error>`
     - ``oegqlb.not_found.user``
     - The user was not found.

``tokenDelete``
---------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-not-found-error>`
     - ``oegqlb.not_found.token``
     - The token was not found.

``shopTokensDelete``
--------------------

This operation returns no error DataTypes.

``regenerateSignatureKey``
--------------------------

This operation returns no error DataTypes.
