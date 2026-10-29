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
   :widths: 17 31 52

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
   :widths: 24 31 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.product``
     - A product with the provided ID already exists.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.download_file``
     - A download file with the provided ID already exists.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.scale_price``
     - A scale price with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.scale_price``
     - A scale price with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

.. _op-admin-product-modify:

``adminProductModify``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.is_variant``
     - The product is a variant.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.

``adminProductDelete``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 19 33 48

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

Every failing entry is returned as an ``AdminImportError`` that carries the code
and message of the original error plus the ``inputPosition`` of the entry. With
the default rollback strategy ``ROLLBACK_WHOLE_IMPORT`` exactly one
``AdminImportError`` is returned; with ``ROLLBACK_FAILING_PRODUCT`` one
``AdminImportError`` per failing entry is returned.

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.id_already_exists.product``
     - A product with the provided ID already exists.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.validation.product_id``
     - The product id is invalid.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.id_already_exists.download_file``
     - A download file with the provided ID already exists.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.id_already_exists.scale_price``
     - A scale price with the provided ID already exists.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_created.scale_price``
     - A scale price with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductsModify``
-----------------------

Failing entries are returned as ``AdminImportError`` in the same way as for
``adminProductsImport``.

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.product.is_variant``
     - The product is a variant.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`AdminImportError <edt-import-error>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductAddVariant``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
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
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.

``adminVariantModify``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.is_not_variant``
     - The product is not a variant.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.language``
     - No language was found for the provided locale.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.product_language_fields``
     - The language fields of the product with the provided ID could not be updated.

``adminVariantRemove``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.is_not_variant``
     - The product is not a variant.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.product``
     - A product with the provided ID could not be deleted.

``adminProductSetIcon``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemoveIcon``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 31 48

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductSetThumbnail``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemoveThumbnail``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 31 48

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductSetPicture``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product_image``
     - The product image was not found.
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductRemovePicture``
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.product_picture_position``
     - The product picture position is invalid.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductAssignCategory``
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 29 37 34

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - :ref:`AdminProductCategoryError <edt-product-category-error>`
     - ``oegqlsa.product_category.price_category_not_assignable``
     - A price category cannot be assigned to a product.
   * - :ref:`AdminProductCategoryError <edt-product-category-error>`
     - ``oegqlsa.product_category.already_assigned``
     - The category is already assigned to the product.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductUnassignCategory``
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 29 26 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.
   * - :ref:`AdminProductCategoryError <edt-product-category-error>`
     - ``oegqlsa.product_category.not_assigned``
     - The category is not assigned to the product.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.

``adminProductAddAttribute``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 31 28 41

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`AdminProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.already_has_attribute``
     - The product already has this attribute assigned.

``adminProductRemoveAttribute``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 31 30 39

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`AdminProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.does_not_have_attribute``
     - The product does not have this attribute assigned.

``adminProductModifyAttribute``
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 31 30 39

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`AdminProductAttributeError <edt-product-attribute-error>`
     - ``oegqlsa.product_attribute.does_not_have_attribute``
     - The product does not have this attribute assigned.

``adminProductAssignManufacturer``
----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 34 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.manufacturer``
     - The manufacturer was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductUnassignManufacturer``
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 21 31 48

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`AdminProductError <edt-product-error>`
     - ``oegqlsa.product.not_saved``
     - The product could not be saved.

``adminProductAssignToSubshop``
-------------------------------

This operation is only available in the Enterprise Edition.

.. list-table::
   :header-rows: 1
   :widths: 25 34 41

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.shop_is_not_subshop``
     - The shop is not a subshop of the current shop.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.shop``
     - The shop was not found.
   * - :ref:`AdminProductShopError <edt-product-shop-error>`
     - ``oegqlsa.product_shop.already_assigned_to_subshop``
     - The product is already assigned to the subshop.

``adminProductUnassignFromSubshop``
-----------------------------------

This operation is only available in the Enterprise Edition.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`ValidationError <edt-sa-validation>`
     - ``oegqlsa.validation.shop_is_not_subshop``
     - The shop is not a subshop of the current shop.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.shop``
     - The shop was not found.
   * - :ref:`AdminProductShopError <edt-product-shop-error>`
     - ``oegqlsa.product_shop.not_assigned_to_subshop``
     - The product is not assigned to the subshop.

``adminProductAssignSelectionList``
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 29 36

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.selection_list``
     - The selection list was not found.
   * - :ref:`AdminProductSelectionListError <edt-product-selection-list-error>`
     - ``oegqlsa.product_selection_list.already_assigned``
     - The selection list is already assigned to the product.
   * - :ref:`AdminProductSelectionListError <edt-product-selection-list-error>`
     - ``oegqlsa.product_selection_list.assignment_failed``
     - The selection list could not be assigned to the product.

``adminProductUnassignSelectionList``
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 29 36

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.product``
     - The product was not found.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.selection_list``
     - The selection list was not found.
   * - :ref:`AdminProductSelectionListError <edt-product-selection-list-error>`
     - ``oegqlsa.product_selection_list.not_assigned``
     - The selection list is not assigned to the product.

``adminProductModifyMetaData``
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 17 32 51

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
   * - :ref:`AdminProductSeoError <edt-product-seo-error>`
     - ``oegqlsa.seo.main_url_not_editable``
     - The main SEO URL cannot be edited when the product has category, vendor or manufacturer assignments.
   * - :ref:`AdminProductSeoError <edt-product-seo-error>`
     - ``oegqlsa.seo.missing_related_object_id``
     - A related object id is required for this SEO type.
   * - :ref:`AdminProductSeoError <edt-product-seo-error>`
     - ``oegqlsa.seo.related_object_not_assigned``
     - The related object is not assigned to the product.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.category``
     - The category was not found.

``adminAttribute``
------------------

.. list-table::
   :header-rows: 1
   :widths: 17 33 50

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.

``adminAttributes``
-------------------

This operation returns no error DataTypes.

``adminAttributeCreate``
------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 31 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.attribute``
     - An attribute with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.attribute``
     - An attribute with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.

``adminAttributeModify``
------------------------

.. list-table::
   :header-rows: 1
   :widths: 19 35 46

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.attribute``
     - An attribute with the provided ID could not be updated.

``adminAttributeDelete``
------------------------

.. list-table::
   :header-rows: 1
   :widths: 19 35 46

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.attribute``
     - The attribute was not found.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.attribute``
     - An attribute with the provided ID could not be deleted.

``adminDownloadFileCreate``
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 31 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.download_file``
     - A download file with the provided ID already exists.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file_in_ftp_dir``
     - The download file was not found in the FTP directory.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.download_file``
     - A download file with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file``
     - The download file was not found.

``adminDownloadFileModify``
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 19 36 45

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

``adminDownloadFileDelete``
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 26 29 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.download_file``
     - The download file was not found.
   * - :ref:`AdminDownloadFileError <edt-download-file-error>`
     - ``oegqlsa.download_file.has_valid_downloads``
     - You cannot delete this file, as long as it has valid downloads.

``adminScalePriceCreate``
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 24 31 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.scale_price``
     - A scale price with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.scale_price``
     - A scale price with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.

``adminScalePriceModify``
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 19 36 45

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.
   * - :ref:`NotUpdatedError <edt-sa-not-updated>`
     - ``oegqlsa.not_updated.scale_price``
     - A scale price with the provided ID could not be updated.

``adminScalePriceDelete``
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 17 35 48

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.scale_price``
     - The scale price was not found.

``adminState``
--------------

.. list-table::
   :header-rows: 1
   :widths: 17 29 54

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.

``adminStateCreate``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 24 31 45

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
   * - :ref:`IdAlreadyExistsError <edt-sa-id-already-exist>`
     - ``oegqlsa.id_already_exists.state``
     - A state with the provided ID already exists.
   * - :ref:`NotCreatedError <edt-sa-not-created>`
     - ``oegqlsa.not_created.state``
     - A state with the provided ID could not be created.
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.

``adminStateModify``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 19 36 45

   * - Error DataType
     - Code
     - Message
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

``adminStateDelete``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 19 31 50

   * - Error DataType
     - Code
     - Message
   * - :ref:`NotFoundError <edt-sa-not-found>`
     - ``oegqlsa.not_found.state``
     - The state was not found.
   * - :ref:`NotDeletedError <edt-sa-not-deleted>`
     - ``oegqlsa.not_deleted.state``
     - A state with the provided ID could not be deleted.
