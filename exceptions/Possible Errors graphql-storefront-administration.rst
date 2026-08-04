========================================================================
Possible Errors per Query/Mutation — graphql-storefront-administration
========================================================================

This page lists every GraphQL **query** and **mutation** of the
``graphql-storefront-administration`` module and the Error DataTypes (including
their codes and messages) that can appear in the operation's payload
``userErrors`` array.

.. note::
   Only errors returned as part of the payload's ``userErrors`` are listed here.
   A failing authentication/authorization check is returned as a **top-level**
   GraphQL error (not inside ``userErrors``) and is therefore not part of the
   tables below.

   All codes are prefixed with ``oegqlsa.``. See :doc:`Error DataTypes` for the
   full type/field reference.

.. contents::
   :local:
   :depth: 1

``adminProduct``
----------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProducts``
-----------------

This operation returns no error DataTypes.

.. _op-admin-product-create:

``adminProductCreate``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - :ref:`IdAlreadyExistError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.product``
     - A product with the provided ID already exists.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

.. _op-admin-product-modify:

``adminProductModify``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.is_variant``
     - The product is a variant.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.language_fields_not_updated``
     - The language fields for the product could not be updated.

``adminProductDelete``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.product``
     - A product with the provided ID could not be deleted.

``adminProductsImport``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.id_already_exists.product``
     - A product with the provided ID already exists.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found (returned directly when a successfully imported product cannot be reloaded).

``adminProductsModify``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.product.is_variant``
     - The product is a variant.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`ImportError <edt-import-error>`
     - ``oegqlsa.product.language_fields_not_updated``
     - The language fields for the product could not be updated.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found (returned directly when a successfully modified product cannot be reloaded).

``addVariantToProduct``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.parent_is_variant``
     - The parent product is a variant.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.language_fields_not_updated``
     - The language fields for the product could not be updated.

``variantModify``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.is_not_variant``
     - The product is not a variant.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.language_fields_not_updated``
     - The language fields for the product could not be updated.

``variantRemove``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.is_not_variant``
     - The product is not a variant.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.product``
     - A product with the provided ID could not be deleted.

``adminProductSetIcon``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemoveIcon``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductSetThumbnail``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemoveThumbnail``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductSetPicture``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemovePicture``
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductAssignCategory``
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - :ref:`ProductCategoryError <edt-product-category-error>`
     - ``oegqlsa.product_category.already_assigned``
     - The category is already assigned to the product.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductUnassignCategory``
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - :ref:`ProductCategoryError <edt-product-category-error>`
     - ``oegqlsa.product_category.not_assigned``
     - The category is not assigned to the product.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductAddAttribute``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`ProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.already_has_attribute``
     - The product already has this attribute assigned.

``adminProductRemoveAttribute``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`ProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.does_not_have_attribute``
     - The product does not have this attribute assigned.

``adminProductModifyAttribute``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`ProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.does_not_have_attribute``
     - The product does not have this attribute assigned.

``adminProductAssignManufacturer``
----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.manufacturer``
     - The manufacturer was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductUnassignManufacturer``
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`ProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductAssignToSubshop``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.shop``
     - The shop was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.shop_is_not_subshop``
     - The shop is not a subshop of the current shop.
   * - :ref:`ProductShopError <edt-product-shop-error>`
     - ``oegqlsa.product_shop.already_assigned_to_subshop``
     - The product is already assigned to the subshop.

``adminProductUnassignFromSubshop``
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.shop``
     - The shop was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.shop_is_not_subshop``
     - The shop is not a subshop of the current shop.
   * - :ref:`ProductShopError <edt-product-shop-error>`
     - ``oegqlsa.product_shop.not_assigned_to_subshop``
     - The product is not assigned to the subshop.

``adminProductModifyMetaData``
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.

``adminProductModifySeoUrl``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - :ref:`ProductSeoError <edt-product-seo-error>`
     - ``oegqlsa.seo.main_url_not_editable``
     - The main SEO URL cannot be edited when the product has category, vendor or manufacturer assignments.
   * - :ref:`ProductSeoError <edt-product-seo-error>`
     - ``oegqlsa.seo.related_object_not_assigned``
     - The related object is not assigned to the product.

``downloadFileCreate``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.download_file``
     - A download file with the provided ID already exists.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.

``downloadFileModify``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file``
     - The download file was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.download_file``
     - A download file with the provided ID could not be updated.

``downloadFileDelete``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file``
     - The download file was not found.
   * - :ref:`DownloadFileError <edt-download-file-error>`
     - ``oegqlsa.download_file.has_valid_downloads``
     - You cannot delete this file, as long as it has valid downloads.

``scalePriceCreate``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.scale_price``
     - A scale price with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.scale_price``
     - A scale price with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.

``scalePriceModify``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.scale_price``
     - A scale price with the provided ID could not be updated.

``scalePriceDelete``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.

``state``
---------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.

``stateCreate``
---------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.state_id``
     - The state id is invalid.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.state_iso_alpha_2``
     - The state ISO alpha-2 code is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.country``
     - The country was not found.
   * - :ref:`IdAlreadyExistError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.state``
     - A state with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.state``
     - A state with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.

``stateModify``
---------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.state_id``
     - The state id is invalid.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.state_iso_alpha_2``
     - The state ISO alpha-2 code is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.country``
     - The country was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.state``
     - A state with the provided ID could not be updated.

``stateDelete``
---------------

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.state``
     - A state with the provided ID could not be deleted.
