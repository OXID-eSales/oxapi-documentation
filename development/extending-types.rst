Extending Types as a Customer
==============================

In case you need to add fields to data types provided by another module (even OXID's GraphQL modules) you can use the `Extending a type feature in GraphQLite <https://graphqlite.thecodingmachine.io/docs/extend-type>`_.

Extending output types (DataTypes)
-----------------------------------

There are two approaches to add fields to an existing DataType.

Using ``@ExtendType`` (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``@ExtendType`` annotation adds fields directly to the existing GraphQL type. This is the simplest approach and keeps the schema clean:

.. code-block:: php

    use TheCodingMachine\GraphQLite\Annotations\ExtendType;
    use TheCodingMachine\GraphQLite\Annotations\Field;

    /** @ExtendType(class=Product::class) */
    class MyProductExtension
    {
        /** @Field */
        public function getCustomColor(Product $product): string
        {
            // your custom logic
        }
    }

The new field appears directly on the existing type — consumers simply add it to their query:

.. code-block:: graphql

    query {
        product(productId: "abc") {
            title
            customColor
        }
    }

**Advantages:**

- The schema stays clean — no additional types or interfaces are generated.
- Follows the composition over inheritance principle.
- ``__typename`` remains unchanged, so client-side caching (e.g. Apollo, urql) is not affected.

**Disadvantage:**

- Each field method receives the original object and resolves its value independently. If multiple new fields rely on data from the same source (e.g. database), each field triggers its own query. There is no built-in way to load the data for all new fields in a single call.

Full example: Extend the product type
"""""""""""""""""""""""""""""""""""""""

Given that you have

- a custom module that

    - adds a custom ``subtitle`` field to the ``oxarticle`` database table
    - extends the ``OxidEsales\Eshop\Application\Model\Article`` model with a ``subtitle()`` method

- want this field exposed via the GraphQL API
- have installed the ``oxid-esales/graphql-storefront`` module

**Create the extend type**

The ``@ExtendType`` annotation has a ``class`` argument which has to be the data type you want to extend. That being the PHP class with the ``@Type`` annotation.

.. literalinclude:: ../examples/extending/ProductExtendType.php
   :language: php

The first argument is always the class you are extending. When a client asks for your field, you'll get the original data type and can then fetch the OXID eShop model from it in case needed.

This results in the following GraphQL schema

.. literalinclude:: ../examples/extending/ProductExtendType.graphql
   :language: graphql

**Register the type**

For GraphQLite to find your newly created extend type

- it must be registered via the namespace mappers ``getTypeNamespaceMapping()``
- needs to exist in the DI container and the container identifier MUST be the fully qualified class name

Namespace mapper:

.. literalinclude:: ../examples/extending/NamespaceMapper.php
   :language: php

services.yaml:

.. literalinclude:: ../examples/extending/services.yaml
   :language: yaml

Using class inheritance
^^^^^^^^^^^^^^^^^^^^^^^^

If you need to add multiple fields that all require data from the same source, extending the DataType class can be more efficient. The extended class receives all additional data as constructor arguments, so everything can be loaded in a single query before the object is created.

.. note::

    This approach is **only possible if the DataType class is not** ``final``.

.. warning::

    Class inheritance creates a **new** GraphQL type (e.g. ``ExtendedProduct``). Existing queries and mutations in the module still return the **original** type (e.g. ``Product``), so the new fields will never appear in their responses.
    This approach is therefore only useful when you also build your **own query or mutation** that explicitly returns the extended type or the new created interface (see :ref:`Class inheritance (automatic interface generation) <class-inheritance-automatic-interface-generation>`). If you simply want to add fields to the responses of existing queries/mutations, use ``@ExtendType`` instead.

.. code-block:: php

    /** @Type() */
    class ExtendedProduct extends Product
    {
        public function __construct(
            private string $id,
            private string $title,
            private string $customColor,
            private float $customWeight,
        ) {
            parent::__construct($id, $title);
        }

        /** @Field */
        public function getCustomColor(): string
        {
            return $this->customColor;
        }

        /** @Field */
        public function getCustomWeight(): float
        {
            return $this->customWeight;
        }
    }

Consumers access the new fields through inline fragments:

.. code-block:: graphql

    query {
        product(productId: "abc") {
            title
            ... on ExtendedProduct {
                customColor
                customWeight
            }
        }
    }

**Advantages:**

- All additional data can be loaded in one go (e.g. a single database query) before constructing the object, rather than one query per field.

**Disadvantages:**

- The schema becomes more complex — GraphQLite automatically generates an additional interface and type (e.g. ``ProductInterface``, ``Product``, ``ExtendedProduct``).
- ``__typename`` changes from ``Product`` to ``ExtendedProduct``, which can affect client-side caching.
- Consumers need to use inline fragments to access the new fields.
- Existing queries and mutations are not affected — they still return the original type, so you must build your own query or mutation that returns the extended type or there interface.

Extending input types
----------------------

Unlike output types, GraphQLite does **not** provide an ``@ExtendInput`` annotation. There is no way to transparently add fields to an existing input type.

The available options are:

- ``@Decorate`` — allows post-processing of an input object after creation, but does **not** add new fields to the GraphQL schema. Useful for validation or value transformation only.
- **New input type + new mutation** — create your own input type with the additional fields and expose it through a new mutation in a new controller.

.. code-block:: php

    /** @Input() */
    class MyCustomProductInput
    {
        public string $title;
        public string $customColor;
    }

    class MyProductMutationController
    {
        /** @Mutation() */
        public function myCustomCreateProduct(
            MyCustomProductInput $input
        ): Product {
            // your custom logic
        }
    }

This means the original mutation remains unchanged, and a new mutation is added alongside it. It is not possible to modify the parameter signature of an existing mutation without overriding every query and mutation that uses the original input type.

.. note::

    The GraphQL specification does not support interfaces on input types. PHP interfaces on input classes can still be useful for testability and shared type hints at the code level, but they will never appear in the GraphQL schema.

Best practice
--------------

Try to withstand the urge to create another module for this case and integrate the GraphQL type mapping into your existing module.
That way you do not end up with an invalid state when activating/deactivating a module.
Otherwise you might deactivate the module that adds the ``subtitle()`` method to the ``OxidEsales\Eshop\Application\Model\Article`` class. The ``subtitle`` field is still in your GraphQL schema, but requesting that field will result in a PHP Fatal Error.
