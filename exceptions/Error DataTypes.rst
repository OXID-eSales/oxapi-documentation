===============
Error DataTypes
===============

This page lists **all** Error DataTypes available through the OXAPI, together with
their error **codes** and the human-readable **messages** attached to those codes.
It covers both the types shipped by ``graphql-base`` and the types (and additional
codes) contributed by the ``graphql-storefront-administration`` module.

Error DataTypes are the type-safe, schema-visible way of returning client-facing
errors as part of a payload's ``userErrors`` array (see :doc:`Error Handling`).
Every Error DataType implements ``ErrorInterface`` and therefore always exposes a
``code`` and a ``message`` field. Specific error types add further type-specific
fields (for example ``productId`` or ``inputPosition``) which can be queried via
inline fragments.

.. contents::
   :local:
   :depth: 2


Base infrastructure
===================

Every Error DataType is built on ``ErrorInterface`` (namespace
``OxidEsales\GraphQL\Base\DataType\Error``). As a GraphQL ``Type`` it defines the
contract shared by all errors and guarantees that a ``code`` and a ``message``
field are always available.


Error DataTypes provided by ``graphql-base``
============================================

The ``graphql-base`` module ships the following concrete Error DataTypes. Codes
follow the ``oegqlb.<category>.<name>`` naming scheme (``oegqlb`` = **o**\ xid
**e**\ Sales **g**\ raph\ **ql**-\ **b**\ ase).

.. _edt-authentication-error:

AuthenticationError
-------------------

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Constant
     - Code
     - Message
   * - ``CREDENTIALS_INCORRECT``
     - ``oegqlb.authentication.credentials_incorrect``
     - The provided credentials are invalid.
   * - ``TOKEN_QUOTA_EXCEEDED``
     - ``oegqlb.authentication.token_quota_exceeded``
     - The token quota for this user has been exceeded.

.. _edt-authorization-error:

AuthorizationError
------------------

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Constant
     - Code
     - Message
   * - ``UNAUTHORIZED_DELETE_TOKEN``
     - ``oegqlb.authorized.delete_token``
     - You are not authorized to delete this token.
   * - ``UNAUTHORIZED_VIEW_TOKEN``
     - ``oegqlb.authorized.view_token``
     - You are not authorized to view this token.

.. _edt-not-found-error:

NotFoundError
-------------

Extra fields: ``identifier: String!``.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Constant
     - Code
     - Message
   * - ``TOKEN``
     - ``oegqlb.not_found.token``
     - The token was not found.
   * - ``USER``
     - ``oegqlb.not_found.user``
     - The user was not found.

.. _edt-validation-error:

ValidationError
---------------

Extra fields: ``value: String!``.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Constant
     - Code
     - Message
   * - ``FINGERPRINT``
     - ``oegqlb.validation.fingerprint``
     - The fingerprint validation failed.
   * - ``REFRESH_TOKEN``
     - ``oegqlb.validation.refresh_token``
     - The provided refresh token is invalid.

Generic Error DataTypes (no predefined codes)
---------------------------------------------

The following Error DataTypes are reusable building blocks for
create/update/delete/uniqueness flows. They do **not** ship predefined code
constants — the ``code`` and ``message`` are supplied by the consuming module
(see :ref:`sfa-base-code-extensions` for how ``graphql-storefront-administration``
extends them). Each exposes an additional ``identifier: String!`` field.

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Type
     - Extra fields
     - Intended use
   * - ``NotCreatedError``
     - ``identifier``
     - A record could not be created.
   * - ``NotUpdatedError``
     - ``identifier``
     - A record could not be updated.
   * - ``NotDeletedError``
     - ``identifier``
     - A record could not be deleted.
   * - ``IdAlreadyExistError``
     - ``identifier``
     - A record with the given id already exists.


Error DataTypes provided by ``graphql-storefront-administration``
=================================================================

The ``graphql-storefront-administration`` module contributes error codes in two
ways: it defines **its own new Error DataTypes** (living under each domain's
``DataType/Error`` directory), and it **extends the generic graphql-base
errors with module-specific codes** (collected under ``Shared/DataType/Error``).

All codes contributed by this module follow the ``oegqlsa.<category>.<name>``
naming scheme (``oegqlsa`` = **o**\ xid **e**\ Sales **g**\ raph\ **ql**
**s**\ torefront-\ **a**\ dministration).

.. _edt-download-file-error:

DownloadFileError
-----------------

Extra fields: ``fileId: String!``.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Constant
     - Code
     - Message
   * - ``HAS_VALID_DOWNLOADS``
     - ``oegqlsa.download_file.has_valid_downloads``
     - You cannot delete this file, as long as it has valid downloads.

.. _edt-import-error:

ImportError
-----------

Extra fields: ``inputPosition: Int!`` — the position of the failing entry in the
import input list.

This type has **no predefined codes**; the ``code`` and ``message`` are provided
dynamically per failing import entry (they are propagated from the underlying
error that occurred while importing that entry).

Example
~~~~~~~

While importing a list of products, one entry fails (e.g. an
``IdAlreadyExistError`` is thrown for the second product). Its ``code`` and
``message`` are copied into a new ``ImportError``, and ``inputPosition`` is set to
the position of the failing entry (1-based). That ``ImportError`` is then returned
in the payload's ``userErrors``:

.. code-block:: php

   // $inputPosition = 2 (second product in the input list)
   new ImportError($error->code(), $error->message(), $inputPosition);
   // -> code: "oegqlsa.id_already_exists.product"
   //    message: "A product with the provided ID already exists."
   //    inputPosition: 2

.. _edt-product-error:

ProductError
------------

Extra fields: ``productId: String!``.

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``IS_VARIANT``
     - ``oegqlsa.product.is_variant``
     - The product is a variant.
   * - ``IS_NOT_VARIANT``
     - ``oegqlsa.product.is_not_variant``
     - The product is not a variant.
   * - ``PARENT_IS_VARIANT``
     - ``oegqlsa.product.parent_is_variant``
     - The parent product is a variant.
   * - ``NOT_SAVED``
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - ``LANGUAGE_FIELDS_NOT_UPDATED``
     - ``oegqlsa.product.language_fields_not_updated``
     - The language fields for the product could not be updated.

.. _edt-product-attribute-error:

ProductAttributeError
---------------------

Extra fields: ``productId: String!``, ``attributeId: String!``.

.. list-table::
   :header-rows: 1
   :widths: 33 40 27

   * - Constant
     - Code
     - Message
   * - ``PRODUCT_ALREADY_HAS_ATTRIBUTE``
     - ``oegqlsa.product_attribute.already_has_attribute``
     - The product already has this attribute assigned.
   * - ``PRODUCT_DOES_NOT_HAVE_ATTRIBUTE``
     - ``oegqlsa.product_attribute.does_not_have_attribute``
     - The product does not have this attribute assigned.

.. _edt-product-category-error:

ProductCategoryError
--------------------

Extra fields: ``categoryId: String!``, ``productId: String!``.

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``CATEGORY_ALREADY_ASSIGNED``
     - ``oegqlsa.product_category.already_assigned``
     - The category is already assigned to the product.
   * - ``CATEGORY_NOT_ASSIGNED``
     - ``oegqlsa.product_category.not_assigned``
     - The category is not assigned to the product.

.. _edt-product-shop-error:

ProductShopError
----------------

Extra fields: ``productId: String!``, ``subshopId: Int!``.

.. list-table::
   :header-rows: 1
   :widths: 32 42 26

   * - Constant
     - Code
     - Message
   * - ``ALREADY_ASSIGNED_TO_SUBSHOP``
     - ``oegqlsa.product_shop.already_assigned_to_subshop``
     - The product is already assigned to the subshop.
   * - ``NOT_ASSIGNED_TO_SUBSHOP``
     - ``oegqlsa.product_shop.not_assigned_to_subshop``
     - The product is not assigned to the subshop.

.. _edt-product-seo-error:

ProductSeoError
---------------

Extra fields: ``productId: String!``.

.. list-table::
   :header-rows: 1
   :widths: 32 40 28

   * - Constant
     - Code
     - Message
   * - ``MAIN_URL_NOT_EDITABLE``
     - ``oegqlsa.seo.main_url_not_editable``
     - The main SEO URL cannot be edited when the product has category, vendor or manufacturer assignments.
   * - ``RELATED_OBJECT_NOT_ASSIGNED``
     - ``oegqlsa.seo.related_object_not_assigned``
     - The related object is not assigned to the product.


.. _sfa-base-code-extensions:

Additional codes for ``graphql-base`` error types
--------------------------------------------------

The module also extends the generic ``graphql-base`` Error DataTypes with its own
codes. These are **not** new GraphQL types — the errors returned are still the
base types (``NotFoundError``, ``ValidationError``, ``NotCreatedError``,
``NotUpdatedError``, ``NotDeletedError``, ``IdAlreadyExistError``). The module
only registers additional ``oegqlsa.*`` codes and their messages for them.

.. _edt-sa-not-found:

NotFoundError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``DOWNLOAD_FILE``
     - ``oegqlsa.not_found.download_file``
     - The download file was not found.
   * - ``DOWNLOAD_FILE_IN_FTP_DIR``
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - ``PRODUCT``
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - ``PRODUCT_IMAGE``
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - ``ATTRIBUTE``
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - ``CATEGORY``
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - ``MANUFACTURER``
     - ``oegqlsa.not_found.manufacturer``
     - The manufacturer was not found.
   * - ``SHOP``
     - ``oegqlsa.not_found.shop``
     - The shop was not found.
   * - ``STATE``
     - ``oegqlsa.not_found.state``
     - The state was not found.
   * - ``COUNTRY``
     - ``oegqlsa.not_found.country``
     - The country was not found.
   * - ``SCALE_PRICE``
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.

.. _edt-sa-validation:

ValidationError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 33 40 27

   * - Constant
     - Code
     - Message
   * - ``PRODUCT_PICTURE_POSITION``
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - ``PRODUCT_ID``
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - ``SHOP_IS_NOT_SUBSHOP``
     - ``oegqlsa.validation.shop_is_not_subshop``
     - The shop is not a subshop of the current shop.
   * - ``STATE_ID``
     - ``oegqlsa.validation.state_id``
     - The state id is invalid.
   * - ``STATE_ISO_ALPHA_2``
     - ``oegqlsa.validation.state_iso_alpha_2``
     - The state ISO alpha-2 code is invalid.

.. _edt-sa-not-created:

NotCreatedError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``DOWNLOAD_FILE``
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - ``SCALE_PRICE``
     - ``oegqlsa.not_created.scale_price``
     - A scale price with the provided ID could not be created.
   * - ``STATE``
     - ``oegqlsa.not_created.state``
     - A state with the provided ID could not be created.

.. _edt-sa-not-updated:

NotUpdatedError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``DOWNLOAD_FILE``
     - ``oegqlsa.not_updated.download_file``
     - A download file with the provided ID could not be updated.
   * - ``SCALE_PRICE``
     - ``oegqlsa.not_updated.scale_price``
     - A scale price with the provided ID could not be updated.
   * - ``STATE``
     - ``oegqlsa.not_updated.state``
     - A state with the provided ID could not be updated.

.. _edt-sa-not-deleted:

NotDeletedError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``PRODUCT``
     - ``oegqlsa.not_deleted.product``
     - A product with the provided ID could not be deleted.
   * - ``STATE``
     - ``oegqlsa.not_deleted.state``
     - A state with the provided ID could not be deleted.

.. _edt-sa-id-already-exist:

IdAlreadyExistError (additional codes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 42 28

   * - Constant
     - Code
     - Message
   * - ``DOWNLOAD_FILE``
     - ``oegqlsa.id_already_exists.download_file``
     - A download file with the provided ID already exists.
   * - ``PRODUCT``
     - ``oegqlsa.id_already_exists.product``
     - A product with the provided ID already exists.
   * - ``SCALE_PRICE``
     - ``oegqlsa.id_already_exists.scale_price``
     - A scale price with the provided ID already exists.
   * - ``STATE``
     - ``oegqlsa.id_already_exists.state``
     - A state with the provided ID already exists.


Summary
=======

.. list-table::
   :header-rows: 1
   :widths: 45 20 35

   * - Module
     - Error DataTypes
     - Predefined codes
   * - ``graphql-base``
     - 8 (4 with codes, 4 generic)
     - 8
   * - ``graphql-storefront-administration`` (own types)
     - 7
     - 14 (``ImportError`` has no predefined codes)
   * - ``graphql-storefront-administration`` (base-type extensions)
     - reuses 6 base types
     - 28
