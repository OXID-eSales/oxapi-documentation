Administrate the storefront
===========================

.. important::
   To administrate your storefront you need the  `GraphQL Storefront Administration module
   <https://github.com/OXID-eSales/graphql-storefront-administration/>`_ installed and activated.
   To use the queries and mutations of this module, admin rights are needed.
   This means that the user has to be assigned to the ``oxidadmin``-group.

What can be done?
-----------------

With the Storefront Administration module we are able to create products, change shop settings or administrate users.

Products
--------

The following queries/mutations exists to administrate products:


Creation:
^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductCreate`` query

    query productCreate {
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
        )
    }

As a result of the creation we get back the AdminProductDataTypeInterface, which contains all of the interesting
information about the new product. By default ``isActive``` and ``isHidden`` will be set to ``false``. If no ``id`` was
passed, an unique id will be generated and set.


Deletion:
^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductDelete`` query

    query productDelete {
        adminProductDelete(
            id: "productId"
        )
    }

If the deletion was successful, ``true`` will be returned.


Modification:
^^^^^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductModify`` query

    query productModify {
        adminProductModify(
            adminProduct: {
                id: "productId"
            }
        )
    }

To modify a product, the id of the product has to be passed. If a field was not set, it won't be updated. As a result,
the ``AdminProductDataType`` is returned.

Import:
^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProductsImport`` query

    query productImport {
        adminProductsImport(
            adminProduct: {
                id: "productId"
            }
        )
    }

The import works the same like the creation of a product. The only difference is, that multiple products can be created
at once. If the import fails at a specific point, a message will be shown with data like ``id`` and ``title`` and the
thrown error, to make it possible to identify the failed product and the problem. The result is a list of all imported
products as ``AdminProductDataType``.


Query an Admin-Product:
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: graphql
   :caption: call to ``adminProduct`` query

    query product {
        adminProduct(
            productId: "productId"
        )
    }

This query is only returning a single product. To get the product as ``AdminProductDataType`` only the ``productId`` is
needed.
