.. _craftrecipe:

craftRecipe
===========

The 'craftRecipe' script block is used to define a crafting recipe, which allows players to craft items or tiles in the game based on the parent script block. For example, a craftRecipe defined inside a `module <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/module.html>`_ will be a recipe to craft an item usually, while when defined inside an `entity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html>`_ it will be the building recipe for that entity.

A craftRecipe will usually require an `inputs <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/inputs.html>`_ and `outputs <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/outputs.html>`_ block. Other parameters are used to define properties of this recipe, such as the `time <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#time>`_ it takes to craft or the `XP awarded <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#xpaward>`_ for crafting it.

For example:

.. code-block:: cpp

   module yourModule /* or Base */
   {
       craftRecipe yourRecipeID
       {
           ...
       }
   }

To define a translation for this recipe, you need to create an entry in the translation file `Recipes.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#recipes>`_. The translation entry should be formatted like this:

.. code-block:: json

   {
     "yourRecipeID": "Your recipe"
   }

Notice how you shouldn't use the `module <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/module.html>`_ in the translation file key and only the craftRecipe ID.

Here's an example of a craftRecipe with some parameters defined:

.. code-block:: cpp

   craftRecipe SawLogs
   {
       timedAction = SawLogs,
       Time = 230,
       Tags = InHandCraft;CanBeDoneFromFloor,
       category = Carpentry,
       xpAward = Woodwork:5,
       inputs
       {
           item 1 [Base.Log] flags[Prop2],
           item 1 tags[Saw] mode:keep flags[MayDegradeLight;Prop1],
       }
       outputs
       {
           item 3 Base.Plank,
       }
   }

Or:

.. code-block:: cpp

   craftRecipe CarveWhistle
   {
       time = 200,
       tags = AnySurfaceCraft;Survivalist,
       category = Carving,
       xpAward = Carving:60,
       SkillRequired = Carving:6,
       needTobeLearn = true,
       AutoLearnAny = Carving:8,
       timedAction = SharpenStake,
       inputs
       {
           item 1 tags[DrillWood;DrillMetal;DrillWoodPoor] mode:keep flags[MayDegradeLight],
           item 1 tags[SharpKnife] mode:keep flags[MayDegradeLight],
           item 1 [Base.SmallAnimalBone] flags[Prop2;AllowDestroyedItem],
       }
       outputs
       {
           item 1 Base.Whistle_Bone,
       }
   }

And a more advanced one:

.. code-block:: cpp

   craftRecipe RefillHurricaneLantern
   {
       timedAction = Making,
       Time = 50,
       OnCreate = Recipe.OnCreate.RefillHurricaneLantern,
       /* OnTest = Recipe.OnTest.RefillHurricaneLantern, */
       Tags = InHandCraft;CanBeDoneInDark,
       category = Miscellaneous, /*category = Survival,*/
       inputs
       {
           item 1 [Base.Lantern_Hurricane;Base.Lantern_Hurricane_Copper;Base.Lantern_Hurricane_Forged;Base.Lantern_Hurricane_Gold;Base.Lantern_Hurricane_Silver] mode:destroy flags[NotFull;AllowFavorite;InheritFavorite;ItemCount] mappers[LampMapper],
           item 1 [*],
           -fluid 1.0 [Petrol],
       }
       outputs
       {
           item 1 mapper:LampMapper,
       }
       itemMapper LampMapper
       {
           Base.Lantern_Hurricane = Base.Lantern_Hurricane,
           Base.Lantern_Hurricane_Copper = Base.Lantern_Hurricane_Copper,
           Base.Lantern_Hurricane_Forged = Base.Lantern_Hurricane_Forged,
           Base.Lantern_Hurricane_Gold = Base.Lantern_Hurricane_Gold,
           Base.Lantern_Hurricane_Silver = Base.Lantern_Hurricane_Silver,

           default = Base.Lantern_Hurricane,
       }
   }

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

:Type: boolean
:Default: ``True``

The AllowBatchCraft parameter is used to allow the recipe to be crafted in batches. This will make a slider appear on the crafting to craft multiple ones at once. Needs to be a boolean and default is true, set to false to disable batch craft.

.. _craftrecipe-autolearnall:

AutoLearnAll
^^^^^^^^^^^^

:Type: Any

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

:Type: Any

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

:Type: Any

The category under which the recipe will be listed in the crafting menu. Helps to organize and identify recipes in the crafting menu. Currently doesn't support translations (confirmed last 42.15).

.. _craftrecipe-icon:

Icon
^^^^

:Type: Any

Specifies the icon associated with this crafting recipe. The icon needs to be located in ``media/textures``\ , for example ``media/textures/myIcon.png`` will be refered to as ``Icon = myIcon,``.

This seems to be used only once in the vanilla recipes with the entry ``Icon = Item_WaterDrop,``\ , as the icon usually defaults to the items that will be crafted.

.. _craftrecipe-metarecipe:

MetaRecipe
^^^^^^^^^^

:Type: Any

A meta recipe is used to link two recipes so that if the meta recipe is known then this recipe will be known.

.. _craftrecipe-needtobelearn:

NeedToBeLearn
^^^^^^^^^^^^^

:Type: Any

Whether the recipe needs to be learned before it can be crafted.

.. _craftrecipe-oncreate:

OnCreate
^^^^^^^^

:Type: Any

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

:Type: Any

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

:Type: Any

No description

.. _craftrecipe-recipegroup:

recipeGroup
^^^^^^^^^^^

:Type: Any

No description

.. _craftrecipe-researchany:

ResearchAny
^^^^^^^^^^^

:Type: Any

No description

.. _craftrecipe-researchskilllevel:

ResearchSkillLevel
^^^^^^^^^^^^^^^^^^

:Type: Any

No description

.. _craftrecipe-skillrequired:

SkillRequired
^^^^^^^^^^^^^

:Type: Any

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

:Type: array **(required)**

Specifies specific conditions which need to be respected to craft this item. At least one crafting bench tag is necessary for the craft to be recognized, such as ``AnySurfaceCraft``. The syntax is as follows:

.. code-block:: cpp

   /* single tag */
   Tags = tag1,

   /* multiple tags */
   Tags = tag1;tag2;...,

For example:

.. code-block:: cpp

   Tags = InHandCraft;CanAlwaysBeResearched,

A crafting bench tag can be created by adding a `component CraftBench <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/component/component-craftbench.html>`_ to an `entity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html>`_ script, which can then be used in this tags parameter.

.. _craftrecipe-time:

time
^^^^

:Type: Any
:Default: ``50``

The time it takes to craft the item, not using a specific unit of time.

.. _craftrecipe-timedaction:

timedAction
^^^^^^^^^^^

:Type: Any

Refers to a timed action script block, used to trigger during the crafting process, for animations and/or sounds but also the calories burned and body heat generation.

.. _craftrecipe-tooltip:

Tooltip
^^^^^^^

:Type: Any

Description of the crafting which is shown in the crafting menu.

.. _craftrecipe-xpaward:

xpAward
^^^^^^^

:Type: Any

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

