.. _component-craftrecipe:

component CraftRecipe
=====================




Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`entity`

**Required Child Blocks:**

- :ref:`inputs`

**Possible Child Blocks:**

- :ref:`inputs`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _component-craftrecipe-category:

category
^^^^^^^^

 (see :ref:`craftrecipe-category`)
    Type: Any

The category under which the recipe will be listed in the crafting menu. Helps to organize and identify recipes in the crafting menu. Currently doesn't support translations (confirmed last 42.15).

.. _component-craftrecipe-needtobelearn:

NeedToBeLearn
^^^^^^^^^^^^^

 (see :ref:`craftrecipe-needtobelearn`)
    Type: Any

Whether the recipe needs to be learned before it can be crafted.

.. _component-craftrecipe-onaddtomenu:

OnAddToMenu
^^^^^^^^^^^

    Type: Any

No description

.. _component-craftrecipe-oncreate:

OnCreate
^^^^^^^^

 (see :ref:`craftrecipe-oncreate`)
    Type: Any

The OnCreate parameter allows the referencing of a Lua function that will be called when the crafting recipe is finished. This can be used to add custom behavior to the crafting recipe when it gets finished. The Lua function needs to be a `global function <https://pzwiki.net/wiki/Lua_(language>`_\ #Local_and_global), it can also be in a global table. The vanilla game OnCreate's are stored in the `Java <https://pzwiki.net/wiki/Java>`_.

The function should have the following structure:

.. code-block:: lua

   function MyOnCreateFunction(craftRecipeData, character)
       -- your custom code here
   end

The ``craftRecipeData`` is a `java object <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/entity/components/crafting/recipe/CraftRecipeData.html>`_ that contains the data of the crafting recipe. The ``character`` is the player character who is crafting the recipe.

.. _component-craftrecipe-skillrequired:

SkillRequired
^^^^^^^^^^^^^

 (see :ref:`craftrecipe-skillrequired`)
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

.. _component-craftrecipe-tags:

tags
^^^^

 (see :ref:`craftrecipe-tags`)
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

.. _component-craftrecipe-time:

time
^^^^

 (see :ref:`craftrecipe-time`)
    Type: Any
    Default: 50

The time it takes to craft the item, not using a specific unit of time.

.. _component-craftrecipe-timedaction:

timedAction
^^^^^^^^^^^

 (see :ref:`craftrecipe-timedaction`)
    Type: Any

Refers to a timed action script block, used to trigger during the crafting process, for animations and/or sounds but also the calories burned and body heat generation.

.. _component-craftrecipe-tooltip:

Tooltip
^^^^^^^

 (see :ref:`craftrecipe-tooltip`)
    Type: Any

Description of the crafting which is shown in the crafting menu.

.. _component-craftrecipe-xpaward:

xpAward
^^^^^^^

 (see :ref:`craftrecipe-xpaward`)
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

