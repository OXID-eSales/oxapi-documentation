Administrate the storefront
===========================

.. important::
   To administrate your storefront you need the  `GraphQL Storefront Administration module
   <https://github.com/OXID-eSales/graphql-storefront-administration/>`_ installed and activated.
   To use the queries and mutations of this module, admin rights are needed.
   This means that the user has to be assigned to the ``oxidadmin``-group.

.. important::
   The `GraphQL Storefront Administration module
   <https://github.com/OXID-eSales/graphql-storefront-administration/>`_ is currently still
   under development. We already have a prototype version which can be tried out.
   If you are interested in working with this module, please contact us.

What can be done?
-----------------

With the Storefront Administration module we are able to create products, change shop settings or administrate users.

Products
--------

The following queries/mutations exists to administrate products:


Creation:
^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductCreate`` mutation

    mutation productCreate {
        adminProductCreate(
            adminProductInput: {
                id: "coolId"
                languageInputs: [
                    {
                        locale: "en"
                        title: "ProductName"
                    }
                ]
            }
        ) {
            adminProduct {
                id
                active
            }
        }
    }

As a result of the creation we get back an ``AdminProductPayload``. Its ``adminProduct`` field contains the new product
as ``AdminProductDataType`` with all of the interesting information. By default ``isActive`` and ``isHidden`` will be
set to ``false``. If no ``id`` was passed, an unique id will be generated and set.


Deletion:
^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductDelete`` mutation

    mutation productDelete {
        adminProductDelete(
            productId: "productId"
        ) {
            success
        }
    }

The mutation returns a ``BooleanPayload``. If the deletion was successful, ``success`` is ``true``.


Modification:
^^^^^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductModify`` mutation

    mutation productModify {
        adminProductModify(
            id: "productId"
            adminProductInput: {
                isActive: false
            }
        ) {
            adminProduct {
                id
                active
            }
        }
    }

To modify a product, the id of the product has to be passed. If a field was not set, it won't be updated. As a result,
an ``AdminProductPayload`` with the modified ``AdminProductDataType`` is returned.

Import:
^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductsImport`` mutation

    mutation productImport {
        adminProductsImport(
            adminProductsInput: [
                {
                    id: "productId-1"
                },
                {
                    id: "productId-2"
                }
            ]
            onFail: ROLLBACK_WHOLE_IMPORT
        ) {
            adminProducts {
                id
                active
            }
        }
    }

The import works the same like the creation of a product. The only difference is, that multiple products can be created
at once. The result is an ``AdminProductsPayload`` whose ``adminProducts`` field contains all imported products as
``AdminProductDataType``.

If the import of a product fails, an ``AdminImportError`` is returned in ``userErrors``. It contains the ``code`` and
``message`` of the underlying error and the ``inputPosition`` of the failed product in the input list, to make it
possible to identify the failed product and the problem. The ``onFail`` argument defines what happens in this case:

* ``ROLLBACK_WHOLE_IMPORT`` (default): the whole import is rolled back and only the first ``AdminImportError`` is
  returned.
* ``ROLLBACK_FAILING_PRODUCT``: only the failing products are skipped. All other products are imported and one
  ``AdminImportError`` per failed product is returned.


Query an Admin-Product:
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProduct`` query

    query product {
        adminProduct(
            productId: "productId"
        ) {
            adminProduct {
                id
                active
            }
        }
    }

This query is only returning a single product. To get the product as ``AdminProductDataType`` inside an
``AdminProductPayload`` only the ``productId`` is needed.
