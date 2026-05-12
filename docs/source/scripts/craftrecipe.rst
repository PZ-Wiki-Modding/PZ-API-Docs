.. _craftrecipe:

craftRecipe
===========

Defines a crafting recipe.

This block can be soft overridden in scripts.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`

**Required Child Blocks:**

- :ref:`inputs`

**Possible Child Blocks:**

- :ref:`inputs`
- :ref:`itemmapper`
- :ref:`outputs`
- :ref:`overlaymapper`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _craftrecipe-allowbatchcraft:

AllowBatchCraft
^^^^^^^^^^^^^^^

    Type: boolean
    Default: True

The AllowBatchCraft parameter is used to allow the recipe to be crafted in batches. This will make a slider appear on the crafting to craft multiple ones at once. Needs to be a boolean and default is true, set to false to disable batch craft.

.. _craftrecipe-autolearnall:

AutoLearnAll
^^^^^^^^^^^^

    Type: Any

The ``autoLearnAll`` parameter specifies that all the provided skills and their associated level need to be reached to learn the recipe. The parameter should be formated this way:

.. code-block:: cpp

   /* a single skill */
   autoLearnAll = <skill name>:<level amount>,

   /* multiple skills */
   autoLearnAll = <skill1 name>:<level amount>;<skill2 name>:<level amount>,format

For the list of available skills, see `this <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: cpp

   autoLearnAll = Carving:3;Maintenance:2,

.. _craftrecipe-autolearnany:

AutoLearnAny
^^^^^^^^^^^^

    Type: Any

The autoLearnAny parameter specifies that at least one of the skills and its associated level need to be reached to learn the recipe. The parameter should be formated this way:

.. code-block:: cpp

   /* a single skill */
   autoLearnAny = <skill name>:<level amount>,

   /* multiple skills */
   autoLearnAny = <skill1 name>:<level amount>;<skill2 name>:<level amount>,format

For the list of available skills, see `this <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: cpp

   autoLearnAny = Carving:3;Maintenance:2,

.. _craftrecipe-category:

category
^^^^^^^^

    Type: Any

The category under which the recipe will be listed in the crafting menu. Helps to organize and identify recipes in the crafting menu. Currently doesn't support translations (confirmed last 42.15).

.. _craftrecipe-icon:

Icon
^^^^

    Type: Any

Specifies the icon associated with this crafting recipe. The icon needs to be located in ``media/textures``\ , for example ``media/textures/myIcon.png`` will be refered to as ``Icon = myIcon,``.

This seems to be used only once in the vanilla recipes with the entry Icon = "Item_WaterDrop", as the icon usually defaults to the items that will be crafted.

.. _craftrecipe-metarecipe:

MetaRecipe
^^^^^^^^^^

    Type: Any

A meta recipe is used to link two recipes so that if the meta recipe is known then this recipe will be known.

.. _craftrecipe-needtobelearn:

NeedToBeLearn
^^^^^^^^^^^^^

    Type: Any

Whether the recipe needs to be learned before it can be crafted.

.. _craftrecipe-oncreate:

OnCreate
^^^^^^^^

    Type: Any

The OnCreate parameter allows the referencing of a Lua function that will be called when the crafting recipe is finished. This can be used to add custom behavior to the crafting recipe when it gets finished. The Lua function needs to be a `global function <https://pzwiki.net/wiki/Lua_(language>`_\ #Local_and_global), it can also be in a global table. The vanilla game OnCreate's are stored in the `Java <https://pzwiki.net/wiki/Java>`_.

The function should have the following structure:

.. code-block:: lua

   function MyOnCreateFunction(craftRecipeData, character)
       -- your custom code here
   end

The ``craftRecipeData`` is a `java object <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/entity/components/crafting/recipe/CraftRecipeData.html>`_ that contains the data of the crafting recipe. The ``character`` is the player character who is crafting the recipe.

.. _craftrecipe-ontest:

OnTest
^^^^^^

    Type: Any

The OnTest parameter is used to define a Lua function that will be called to verify if the recipe can be crafted. If the function returns true, the recipe can be crafted but if the function returns false, the recipe cannot be crafted. The Lua function needs to be a `global function <https://pzwiki.net/wiki/Lua_(language>`_\ #Local_and_global), it can also be in a global table. The vanilla game OnTest's are stored in the `Java <https://pzwiki.net/wiki/Java>`_.

The function should have the following structure:

.. code-block:: lua

   function MyOnTestFunction(item, character)
       -- your custom code here
       return logicTestResult  -- based on your logic test above
   end

``item`` is an InventoryItem while ``character`` is the player trying to craft this recipe.

.. _craftrecipe-overlaystyle:

overlayStyle
^^^^^^^^^^^^

    Type: Any

No description

.. _craftrecipe-recipegroup:

recipeGroup
^^^^^^^^^^^

    Type: Any

No description

.. _craftrecipe-researchany:

ResearchAny
^^^^^^^^^^^

    Type: Any

No description

.. _craftrecipe-researchskilllevel:

ResearchSkillLevel
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _craftrecipe-skillrequired:

SkillRequired
^^^^^^^^^^^^^

    Type: Any

Specifies the skill level required to perform this crafting action. It should be formated this way:

.. code-block:: cpp

   /* a single skill */
   skillRequired = <skill name>:<level>,

   /* multiple skills */
   skillRequired = <skill1 name>:<level>;<skill2 name>:<level>,

For the list of available skills, see `this <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: cpp

   skillRequired = Blacksmith:3;Tailoring:2,

.. _craftrecipe-tags:

tags
^^^^

    Type: array (required)

Specifies specific conditions which need to be respected to craft this item. At least one crafting bench tag is necessary for the craft to be recognized, such as ``AnySurfaceCraft``. The syntax is as follows:

.. code-block:: cpp

   /* single tag */
   Tags = tag1,

   /* multiple tags */
   Tags = tag1;tag2;...,

For example:

.. code-block:: cpp

   Tags = InHandCraft;CanAlwaysBeResearched,

.. _craftrecipe-time:

time
^^^^

    Type: Any
    Default: 50

The time it takes to craft the item, not using a specific unit of time.

.. _craftrecipe-timedaction:

timedAction
^^^^^^^^^^^

    Type: Any

Refers to a timed action script block, used to trigger during the crafting process, for animations and/or sounds but also the calories burned and body heat generation.

.. _craftrecipe-tooltip:

Tooltip
^^^^^^^

    Type: Any

Description of the crafting which is shown in the crafting menu.

.. _craftrecipe-xpaward:

xpAward
^^^^^^^

    Type: Any

Specifies the experience points awarded for crafting this item. The parameter should be formated this way:

.. code-block:: cpp

   /* a single skill */
   xpAward = <skill name>:<xp amount>,

   /* multiple skills */
   xpAward = <skill1 name>:<xp amount>;<skill2 name>:<xp amount>,format

For the list of available skills, see `this <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: cpp

   xpAward = Blacksmith:10;Tailoring:5,

