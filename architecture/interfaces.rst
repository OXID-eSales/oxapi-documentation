GraphQL Interfaces and Type Inheritance
========================================

GraphQLite provides two clean patterns for mapping PHP interfaces to GraphQL types. Understanding when and how to use them is essential for designing a well-structured schema.

Pattern A: ``@Type`` on the Implementation Only
------------------------------------------------

Use this pattern when you **do not** need a GraphQL interface in your schema. The PHP interface serves purely as a code-level contract, while all GraphQL annotations live on the implementing class.

.. code-block:: php

    // PHP Interface — no @Type, no @Field
    interface AdminProductDataTypeInterface
    {
        public function getId(): string;
    }

    // Implementation — @Type and @Field annotations here
    /** @Type() */
    class AdminProductDataType implements AdminProductDataTypeInterface
    {
        /** @Field */
        public function getId(): string { ... }
    }

In this case, GraphQLite generates a single ``AdminProductDataType`` type in the schema. The PHP interface remains invisible to GraphQL consumers.

Pattern B: ``@Type`` on the Interface
-------------------------------------

Use this pattern when you **want** a GraphQL interface to appear in your schema, for example when multiple types share a common set of fields.

.. code-block:: php

    // PHP Interface — @Type and @Field annotations here
    /** @Type() */
    interface AdminProductDataTypeInterface
    {
        /** @Field */
        public function getId(): string;
    }

    // Implementation — @Type is optional (GraphQLite can derive it)
    /** @Type() */
    class AdminProductDataType implements AdminProductDataTypeInterface
    {
        // @Field is not necessary — it is inherited from the interface
    }

GraphQLite will generate both a GraphQL interface type and the implementing object type. The ``@Field`` annotations are inherited, so there is no need to repeat them on the class.

.. note::

    If you annotate the interface with ``@Type`` but **not** the implementing class, GraphQLite will still auto-generate a type for the class. However, the generated name will use an ``Impl`` suffix (e.g. ``AdminProductDataTypeImpl``), which is usually undesirable. Always annotate both the interface and the class explicitly.


When to Use GraphQL Interfaces
-------------------------------

GraphQL interfaces are only necessary when your schema requires an **inheritance structure** — that is, when a single query or mutation can return different concrete types that share a common set of fields. There are two typical scenarios:

One interface, multiple implementations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A query returns different types that implement the same interface. Consumers use **inline fragments** to access type-specific fields:

.. code-block:: graphql

    query {
        searchResults {
            # Common fields from the interface
            id

            # Type-specific fields via fragments
            ... on Product { title }
            ... on Category { name }
        }
    }

Class inheritance (automatic interface generation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When one implementation class extends another, GraphQLite **automatically** generates a GraphQL interface from the base class:

.. code-block:: graphql
    :class: graphql-sdl

    # Auto-generated interface from the Contact class
    interface ContactInterface {
        name: String!
    }

    type Contact implements ContactInterface {
        name: String!
    }

    type User implements ContactInterface {
        name: String!
        email: String!
    }

This allows a controller to declare ``Contact`` as the return type while the actual implementation can return a ``User``. Consumers can access the additional fields through fragments:

.. code-block:: graphql

    query {
        contact {
            name
            ... on User {
                email
            }
        }
    }

Current Decision
-----------------

In our GraphQL modules, we use **Pattern A** — PHP interfaces are used extensively for code-level contracts (e.g. type safety, testability, dependency inversion), but they are **not** exposed as GraphQL interfaces in the schema.
The ``@Type`` and ``@Field`` annotations live solely on the implementing classes.

There is currently no need for a shared GraphQL interface or inheritance structure across types. Should the need arise in the future — for example, when a query must return polymorphic results — Pattern B would be the recommended approach.
