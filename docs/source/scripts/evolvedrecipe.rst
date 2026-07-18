.. _scripts-evolvedrecipe:

evolvedrecipe
=============

.. attribute:: Soft Override

   Unknown

Defines a dynamic recipe where items can be added in as ingredients in multiple steps. This is notably used to define soups, stews or beverages that can accept multiple combination of ingredients. Stats from each `items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ are added to the final product.

For an item to be accepted in a specific evolvedrecipe, it needs to have the parameter `EvolvedRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-evolvedrecipe>`_ which lists every evolved recipes it can be used in and in what quantity.

For example:

.. code-block:: cpp

   evolvedrecipe Sandwich
   {
       BaseItem = Base.BreadSlices,
       MaxItems = 4,
       ResultItem = Base.Sandwich,
       Name = Make Sandwich,
       CanAddSpicesEmpty = true,
       AddIngredientIfCooked = true,
       Template = Sandwich,
       Cookable = true,
   }

   item Processedcheese
   {
       EvolvedRecipe = Sandwich:5;Burger:5;Hotdog:5;Rice:5;Pasta:5;Bread:5;Omelette:5;Toast:5,
       ...
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

.. attribute:: Optional

   False

.. attribute:: Can have spaces

   True


Parameters
----------

.. _scripts-evolvedrecipe-addingredientifcooked:

AddIngredientIfCooked
^^^^^^^^^^^^^^^^^^^^^

.. attribute:: Type

   boolean

Whenever ingredients can be added even after the item has been cooked.


.. _scripts-evolvedrecipe-addingredientsound:

AddIngredientSound
^^^^^^^^^^^^^^^^^^

.. attribute:: Type

   block (block: :ref:`sound <scripts-sound>`)

.. attribute:: Default

   ``AddItemInBeverage``

The `sound <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_ which will be played when an ingredient is added.

If set to ``AddItemInBeverage``\ , when the `ingredient <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ has the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-tags>`_ ``base:wetbeverageingredient``\ , the sound will be changed to ``AddWetItemInBeverage`` but if not present, it will changed to ``AddDryItemInBeverage``.


.. _scripts-evolvedrecipe-baseitem:

BaseItem
^^^^^^^^

.. attribute:: Type

   block (block: :ref:`item <scripts-item>`, with :ref:`module`)

The `item <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ which will serve as the base for this recipe, that is the item which will be combined with the ingredients to create the `ResultItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#resultitem>`_.


.. _scripts-evolvedrecipe-canaddspicesempty:

CanAddSpicesEmpty
^^^^^^^^^^^^^^^^^

.. attribute:: Type

   boolean

If true, the `spices <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-spice>`_ can be added to the `BaseItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#baseitem>`_ directly without any ingredients yet added.


.. _scripts-evolvedrecipe-cookable:

Cookable
^^^^^^^^

.. attribute:: Type

   boolean

.. attribute:: Allowed values

   
* ``true``

If true, the `ResultItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#resultitem>`_ will be cookable.


.. _scripts-evolvedrecipe-maxitems:

MaxItems
^^^^^^^^

.. attribute:: Type

   integer

.. attribute:: Minimum

   ``1``

The maximum number of ingredients which will be used in this recipe. Unique `spices <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-spice>`_ on the other hand can be added infinitely.


.. _scripts-evolvedrecipe-minimumwater:

MinimumWater
^^^^^^^^^^^^

.. attribute:: Type

   float

.. attribute:: Default

   ``0.0``

The minimum amount of water which must be present in the `BaseItem <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html#baseitem>`_ for this recipe to be valid.


.. _scripts-evolvedrecipe-name:

Name
^^^^

.. attribute:: Type

   string

The translation key for the name of this recipe which will be retrieved from the `Recipes.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#recipes>`_ file.


.. _scripts-evolvedrecipe-resultitem:

ResultItem
^^^^^^^^^^

.. attribute:: Type

   block (block: :ref:`item <scripts-item>`, with :ref:`module`)

No description provided.


.. _scripts-evolvedrecipe-template:

Template
^^^^^^^^

.. attribute:: Type

   string

Whenever an `item <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ uses this recipe via the `EvolvedRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-evolvedrecipe>`_ parameter, and links to the recipe of the ``Template``\ , that ingredient will be added to both every evolved recipe with this template value. This allows you to make variants of the same evolved recipe with different containers, for example for beverages, where the same recipe can be used for a cup, a bottle or a jar.


