.. _scripts-component-craftrecipe:

component CraftRecipe
=====================

:Soft Override: Unknown

:Is Variant of: :ref:`component <scripts-component>`

No description provided.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`entity <scripts-entity>`

This block requires these following children to be valid:

- :ref:`inputs <scripts-inputs>`


ID
--

This block should have no ID.


Parameters
----------

.. _scripts-component-craftrecipe-category:

.. attribute:: category
   :noindex:

:Type: translation

:Default: ``Miscellaneous``

The category under which the recipe will be listed in the crafting menu. Helps to organize and identify recipes in crafting menu. Your category should have a key with the suffix ``IGUI_CraftingCategories_`` in the `IG_UI.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#ig-ui>`_ translation file to be properly displayed in the crafting menu. For example:

.. code-block:: java

   category = MyCategory,

And in the translation file:

.. code-block:: json

   {
     "IGUI_CraftingCategories_MyCategory": "My Category"
   }


.. _scripts-component-craftrecipe-needtobelearn:

.. attribute:: NeedToBeLearn
   :noindex:

:Type: Unknown

Whether the recipe needs to be learned before it can be crafted.


.. _scripts-component-craftrecipe-onaddtomenu:

.. attribute:: OnAddToMenu
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-component-craftrecipe-oncreate:

.. attribute:: OnCreate
   :noindex:

:Type: callback

Various callback functions can be added to a recipe to trigger at specific moments during the crafting process:


* `OnCreate <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#oncreate>`_ is called when the crafting recipe is finished.
* `OnTest <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#ontest>`_ is called to verify if the item can be used in the recipe.
* `OnFailed <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#onfailed>`_ is called when the crafting recipe fails or is canceled.
* `OnUpdate <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#onupdate>`_ is called every tick while the recipe is being crafted.

The callback needs to be a Lua function defined as a `global function <https://pzwiki.net/wiki/Lua_(language>`_\ #Local_and_global), which can also be stored in a global table. The vanilla game OnCreate's are stored in the `Java <https://pzwiki.net/wiki/Java>`_.

For example, for `OnCreate <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#oncreate>`_ you should have the following structure:

.. code-block:: lua

   ---@param craftRecipeData CraftRecipeData
   ---@param character IsoGameCharacter
   function MyOnCreateFunction(craftRecipeData, character)
       -- your custom code here
   end

The ``craftRecipeData`` is a `java object <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/entity/components/crafting/recipe/CraftRecipeData.html>`_ that contains the data of the crafting recipe. The ``character`` is the player character who is crafting the recipe.

For `OnTest <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#ontest>`_ you should have the following structure:

.. code-block:: lua

   ---@param item InventoryItem
   ---@param character IsoGameCharacter
   ---@return boolean logicTestResult
   function MyOnTestFunction(item, character)
       -- your custom code here
       return logicTestResult  -- based on your logic test above
   end


.. _scripts-component-craftrecipe-skillrequired:

.. attribute:: SkillRequired
   :noindex:

:Type: object (object: string->>integer, kv: ':', pairs: ';')

Specifies the skill level required to perform this crafting action. It should be formatted this way:

.. code-block:: java

   /* a single skill */
   skillRequired = <skill name>:<level>,

   /* multiple skills */
   skillRequired = <skill1 name>:<level>;<skill2 name>:<level>,

For the list of available skills, see the `wiki <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: java

   skillRequired = Blacksmith:3;Tailoring:2,


.. _scripts-component-craftrecipe-tags:

.. attribute:: tags
   :noindex:

:Type: array (array of string, separator: ';')

:Required: True

Specifies specific conditions which need to be respected to craft this item. At least one crafting bench tag is necessary for the craft to be recognized, such as ``AnySurfaceCraft``. The syntax is as follows:

.. code-block:: java

   /* single tag */
   Tags = tag1,

   /* multiple tags */
   Tags = tag1;tag2;...,

For example:

.. code-block:: java

   Tags = InHandCraft;CanAlwaysBeResearched,

A crafting bench tag can be created by adding a `component CraftBench <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/component/component-craftbench.html>`_ to an `entity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html>`_ script, which can then be used in this tags parameter.

You can find a list of tags available on the `wiki <https://pzwiki.net/wiki/CraftRecipe#List_of_tags>`_.


.. _scripts-component-craftrecipe-time:

.. attribute:: time
   :noindex:

:Type: integer

:Default: ``50``

The time it takes to craft the item, not using a specific unit of time so refer to the vanilla recipes to get an idea of what value to use.


.. _scripts-component-craftrecipe-timedaction:

.. attribute:: timedAction
   :noindex:

:Type: block (block: :ref:`timedAction <scripts-timedaction>`)

Refers to a timed action script block to trigger during the crafting process, for animations and/or sounds but also the calories burned and body heat generation.


.. _scripts-component-craftrecipe-tooltip:

.. attribute:: Tooltip
   :noindex:

:Type: translation

Description of the crafting which is shown in the crafting menu. The value needs be a key in the `Tooltip.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#tooltip>`_ translation file. For example:

.. code-block:: java

   Tooltip = MyTooltipKey,

And in the translation file:

.. code-block:: json

   {
     "MyTooltipKey": "This is my tooltip description."
   }


.. _scripts-component-craftrecipe-xpaward:

.. attribute:: xpAward
   :noindex:

:Type: Unknown

Specifies the experience points awarded for crafting this item. The parameter should be formatted this way:

.. code-block:: java

   /* a single skill */
   xpAward = <skill name>:<xp amount>,

   /* multiple skills */
   xpAward = <skill1 name>:<xp amount>;<skill2 name>:<xp amount>,format

For the list of available skills, see the `wiki <https://pzwiki.net/wiki/CraftRecipe#Available_skills>`_.

For example:

.. code-block:: java

   xpAward = Blacksmith:10;Tailoring:5,


