Extending Types as a Customer
==============================

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
