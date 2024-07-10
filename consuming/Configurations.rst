Read and update configurations
==============================

.. important::
   To read and update configurations you need the  `GraphQL Configuration Access module
   <https://github.com/OXID-eSales/graphql-configuration-access/>`_ installed and activated.
   To use the queries and mutations of this module, admin rights are needed.
   This means that the user has to be assigned to the ``oxidadmin``-group.

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

    mutation changeBooleanSetting {
        moduleSettingBooleanChange(
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
            "moduleSettingsBooleanChange": {
                "name": "booleanSetting",
                "value": true,
            }
        }
    }

List Themes
-----------

Use this queries to get the list of all themes. You can use filter like ``title`` to filter theme by its title or ``active`` to filter theme on basis of its status.

.. code-block:: graphql
   :caption: call to ``themesList`` query

    query themeListFilter {
      themesList(
        filters: {
          title: {
            contains: "Theme"
          }
          active: {
            equals: true
          }
        }) {
        title
        identifier
        version
        description
        active
      }
    }

.. code-block:: json
   :caption: ``themesList`` query response

    {
      "data": {
        "themesList": [
          {
            "title": "APEX Theme",
            "identifier": "apex",
            "version": "1.3.0",
            "description": "APEX - Bootstrap 5 TWIG Theme",
            "active": true
          },
          {
            "title": "Wave",
            "identifier": "wave",
            "version": "3.0.1",
            "description": "Wave is OXID`s official responsive theme based on the CSS framework Bootstrap 4.",
            "active": false
          }
        ]
      }
    }

Switch Theme
------------

In order to activate a theme by a given it pass themeId as ``identifier``, you will receive response as Bool value whether given theme was activated or not.

.. code-block:: graphql
   :caption: call to ``switchTheme`` query

    mutation switchTheme{
      switchTheme(identifier: "apex")
    }

.. code-block:: json
   :caption: ``switchTheme`` query response

    {
      "data": {
        "switchTheme": true
      }
    }

List Modules
------------

Use this queries to get the list of all modules. You can use filter like ``title`` to filter theme by its title or ``active`` to filter module on basis of its status.

.. code-block:: graphql
   :caption: call to ``modulesList`` query

    query modulesList {
      modulesList(
        filters: {
          title: {
            contains: "Base"
          }
          active: {
            equals: true
          }
        }){
            id
            version
            title
            description
            thumbnail
            author
            url
            email
            active
      }
    }

.. code-block:: json
   :caption: ``modulesList`` query response

    {
      "data": {
        "modulesList": [
          {
            "id": "moduleId",
            "version": "1.3.0",
            "title": "GraphQL Storefront",
            "description": "GraphQL Storefront",
            "thumbnail": "http://www.someUrl.com",
            "author": "oxid",
            "url": "url",
            "email": "some@email.com",
            "active": true
          },
          {
            ....
          }
        ]
      }
    }

Activate Module
---------------

In order to activate a module by a given it pass module id as ``moduleId``, you will receive response as Bool value whether given module was activated or not.

.. code-block:: graphql
   :caption: call to ``activateModule`` query

    mutation activateModule{
      activateModule(moduleId: "awesomeModule")
    }

.. code-block:: json
   :caption: ``activateModule`` query response

    {
      "data": {
        "activateModule": true
      }
    }

Deactivate Module
---------------

In order to deactivate a module by a given it pass module id as ``moduleId``, you will receive response as Bool value whether given module was deactivated or not.

.. code-block:: graphql
   :caption: call to ``deactivateModule`` query

    mutation deactivateModule{
      deactivateModule(moduleId: "awesomeModule")
    }

.. code-block:: json
   :caption: ``deactivateModule`` query response

    {
      "data": {
        "deactivateModule": true
      }
    }

.. important::
   Pay attention that the types for module/theme/shop-queries or mutations can be different.
   Also the handling of the values depends on the implementation in the shop.
   Only the handling of Theme-configurations are currently implemented by the module itself.

