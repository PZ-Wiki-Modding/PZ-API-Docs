.. _evolvedrecipe:

evolvedrecipe
=============

Defines a dynamic recipe.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _evolvedrecipe-addingredientifcooked:

AddIngredientIfCooked
^^^^^^^^^^^^^^^^^^^^^

:Type: boolean

Whenever ingredients can be added even after the item has been cooked.

.. _evolvedrecipe-addingredientsound:

AddIngredientSound
^^^^^^^^^^^^^^^^^^

:Type: block (block: :ref:`sound`)
:Default: ``AddItemInBeverage``

The `sound <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_ which will be played when an ingredient is added.

If set to ``AddItemInBeverage``\ , when the `ingredient <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ has the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-tags>`_ ``base:wetbeverageingredient``\ , the sound will be changed to ``AddWetItemInBeverage`` but if not present, it will changed to ``AddDryItemInBeverage``.

.. _evolvedrecipe-baseitem:

BaseItem
^^^^^^^^

:Type: block (block: :ref:`item`, with :ref:`module`)

The `item <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ which will serve as the base for this recipe, that is the item which will be combined with the ingredients to create the `ResultItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#resultitem>`_.

.. _evolvedrecipe-canaddspicesempty:

CanAddSpicesEmpty
^^^^^^^^^^^^^^^^^

:Type: boolean

If true, the `spices <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-spice>`_ can be added to the `BaseItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#baseitem>`_ directly without any ingredients yet added.

.. _evolvedrecipe-cookable:

Cookable
^^^^^^^^

:Type: boolean

If true, the `ResultItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#resultitem>`_ will be cookable.

Allowed values:

    - ``true``

.. _evolvedrecipe-maxitems:

MaxItems
^^^^^^^^

:Type: integer
:Range: Min: 1

The maximum number of ingredients which will be used in this recipe. Unique `spices <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-spice>`_ on the other hand can be added infinitely.

.. _evolvedrecipe-minimumwater:

MinimumWater
^^^^^^^^^^^^

:Type: float
:Default: ``0.0``

The minimum amount of water which must be present in the `BaseItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#baseitem>`_ for this recipe to be valid.

.. _evolvedrecipe-name:

Name
^^^^

:Type: string

The translation key for the name of this recipe which will be retrieved from the `Recipes.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#recipes>`_ file.

.. _evolvedrecipe-resultitem:

ResultItem
^^^^^^^^^^

:Type: block (block: :ref:`item`, with :ref:`module`)

No description

.. _evolvedrecipe-template:

Template
^^^^^^^^

:Type: block (block: :ref:`evolvedrecipe`)

Whenever an item uses this recipe via the `EvolvedRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-evolvedrecipe>`_ parameter, and links to the recipe of the ``Template``\ , that ingredient will be added to both the template and this evolved recipe. This allows you to make variants of the same evolved recipe with different containers, for example for beverages, where the same recipe can be used for a cup, a bottle or a jar.

It will not copy the parameters of the template recipe however, only the ingredients.

