Read and update configurations
==============================

.. important::
   To read and update configurations you need the  `GraphQL Configuration Access module
   <https://github.com/OXID-eSales/graphql-configuration-access/>`_ installed and activated.

List configurations
-------------------

To read or update configurations it's important to know which type the configuration has, you want to modify
or read to.
Three list queries are available to figure that out. One for module- (``moduleSettings``), one for theme- (``themeSettings``)
and one for shop-configurations (``shopSettings``).

Here is one example how to use it:

.. code-block:: graphql
   :caption: call to ``moduleSettings`` query

    query settings {
        moduleSettings(
            moduleId: "awesomeModule"
        )
    }

.. code-block:: json
   :caption: ``moduleSettings`` query response

    {
        "data": {
            "moduleSettings": [
                {
                    "name": "intSetting",
                    "type": "num",
                    "supported": true
                },
                {
                    "name": "floatSetting",
                    "type": "num",
                    "supported": true
                },
                {
                    "name": "boolSetting",
                    "type": "bool",
                    "supported": true
                },
                {
                    "name": "stringSetting",
                    "type": "str",
                    "supported": true
                },
                {
                    "name": "arraySetting",
                    "type": "arr",
                    "supported": true
                }
            ]
        }
    }

The returned data is showing the ``name`` of the setting, the ``type``, to know how to fetch or change the
setting and whether the type is ``supported`` by the module queries and mutations at all.

Read configurations
-------------------

If the type is known, you can read the setting by using one of the type separated queries.
The ``name`` of the setting and in our case the corresponding ``module`` is necessary to explicitly
select the configuration.

.. code-block:: graphql
   :caption: call to ``moduleSettingBoolean`` query

    query booleanSetting {
        moduleSettingBoolean(
            name: "booleanSetting",
            moduleId: "awesomeModule"
        ) {
            name
            value
        }
    }

.. code-block:: json
   :caption: ``moduleSettingBoolean`` query response

    {
        "data": {
            "moduleSettingBoolean": {
                "name": "booleanSetting",
                "value": false,
            }
        }
    }

Update configurations
---------------------

To update a setting, the ``name``, the new ``value`` and in our case the ``module`` is necessary.

.. code-block:: graphql
   :caption: call to ``moduleSettingBooleanChange`` query

    query booleanSetting {
        moduleSettingBoolean(
            name: "booleanSetting",
            value: true
            moduleId: "awesomeModule"
        ) {
            name
            value
        }
    }

.. code-block:: json
   :caption: ``moduleSettingBooleanChange`` query response

    {
        "data": {
            "moduleSettings": {
                "name": "booleanSetting",
                "value": true,
            }
        }
    }


.. important::
   Pay attention that the types for module/theme/shop-queries or mutations can be different.
   Also the handling of the values depends on the implementation in the shop.
   Only the handling of Theme-configurations are currently implemented by the module itself.

