Translation Files
=================

Available translation file types and their descriptions.

.. _attributes-translation:

Attributes
-----------

.. list-table::
   :widths: auto

   * - File Name
     - ``Attributes``
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^Attributes_Type_[A-Za-z_]+$``, ``^Attributes_ToosltipOverride_[A-Za-z_]+$``

.. _bodyparts-translation:

BodyParts
----------

.. list-table::
   :widths: auto

   * - File Name
     - ``BodyParts``
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^BODYPART_[A-Z_]+$``

.. _challenge-translation:

Challenge
----------

.. list-table::
   :widths: auto

   * - File Name
     - ``Challenge``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Challenge_``
   * - Pattern Properties
     - ``^Challenge_[A-Za-z0-9\s]+(_[A-Za-z0-9]+|InfoBox)$``

.. _contextmenu-translation:

ContextMenu
------------

Translations used in the context menus of the game.

.. list-table::
   :widths: auto

   * - File Name
     - ``ContextMenu``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``ContextMenu_``
   * - Pattern Properties
     - ``^ContextMenu_[A-Za-z0-9_]+$``

.. _dynamicradio-translation:

DynamicRadio
-------------

Dynamic radio translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``DynamicRadio``
   * - Function
     - ``getRadioText``
   * - Key Prefix
     - ``AEBS_``
   * - Pattern Properties
     - ``^AEBS_[A-Za-z0-9_]+$``

.. _entity-translation:

Entity
-------

Translations for entity UIs.

.. list-table::
   :widths: auto

   * - File Name
     - ``Entity``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``EC_``
   * - Pattern Properties
     - ``^EC_[A-Za-z_]+$``

.. _evolvedrecipename-translation:

EvolvedRecipeName
------------------

Translations for evolved recipe scripts.

.. list-table::
   :widths: auto

   * - File Name
     - ``EvolvedRecipeName``
   * - Function
     - ``Translator.getItemEvolvedRecipeName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$``

.. _farming-translation:

Farming
--------

Translations for farming menus.

.. list-table::
   :widths: auto

   * - File Name
     - ``Farming``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Farming_``
   * - Pattern Properties
     - ``^Farming_[A-Za-z0-9_\s-]+$``

.. _fluids-translation:

Fluids
-------

Translations for fluid related UI elements and fluid containers.

.. list-table::
   :widths: auto

   * - File Name
     - ``Fluids``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Fluid_``
   * - Pattern Properties
     - ``^Fluid_[A-Za-z0-9_]+$``

.. _gamesound-translation:

GameSound
----------

Game sounds and categories translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``GameSound``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``GameSound_``
   * - Pattern Properties
     - ``^GameSound_[A-Za-z0-9_]+$``

.. _ig_ui-translation:

IG_UI
------

Translations for in-game user interface elements.

.. list-table::
   :widths: auto

   * - File Name
     - ``IG_UI``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``IGUI_``
   * - Pattern Properties
     - ``^IGUI_[A-Za-z0-9_\s:\.\/'!-]+$``

.. _itemname-translation:

ItemName
---------

Translations for item scripts. The key needs to be the full type of the item.

.. list-table::
   :widths: auto

   * - File Name
     - ``ItemName``
   * - Function
     - ``getItemNameFromFullType``
   * - Pattern Properties
     - ``^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$``

.. _location_generic-translation:

Location_Generic
-----------------

A translation file for the map. The filename needs to refer the file "map.info" in the mod's media folder.

.. list-table::
   :widths: auto

   * - File Name
     - ``Location_Generic``
   * - Function
     - ``N/A``
   * - Keys
     - ``title``, ``description``, ``$schema``

.. _makeup-translation:

MakeUp
-------

Translations for make up.

.. list-table::
   :widths: auto

   * - File Name
     - ``MakeUp``
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^MakeUp(Category|Type)_[A-Za-z0-9]+$``

.. _maplabel-translation:

MapLabel
---------

.. list-table::
   :widths: auto

   * - File Name
     - ``MapLabel``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``MapLabel_``
   * - Pattern Properties
     - ``^MapLabel_[A-Za-z]+$``

.. _mod-translation:

Mod
----

Translations for the mod.info file. Possible keys are "name" and "description".

.. list-table::
   :widths: auto

   * - File Name
     - ``Mod``
   * - Function
     - ``N/A``
   * - Keys
     - ``name``, ``description``, ``$schema``

.. _moodles-translation:

Moodles
--------

Moodles status and descriptions translations

.. list-table::
   :widths: auto

   * - File Name
     - ``Moodles``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Moodles_``
   * - Pattern Properties
     - ``^Moodles_[A-Za-z0-9_]+(_desc)?_lvl0-9$``

.. _moveables-translation:

Moveables
----------

Moveable tiles as items translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``Moveables``
   * - Function
     - ``Translator.getMoveableDisplayName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_!\s]+$``

.. _multistagebuild-translation:

MultiStageBuild
----------------

Translations for multi stage build.

.. list-table::
   :widths: auto

   * - File Name
     - ``MultiStageBuild``
   * - Function
     - ``Translator.getMultiStageBuild``
   * - Key Prefix
     - ``MultiStageBuild_``
   * - Pattern Properties
     - ``^MultiStageBuild_[A-Za-z0-9_]+$``

.. _print_media-translation:

Print_Media
------------

Text content for media items such as newspapers, describing their content.

.. list-table::
   :widths: auto

   * - File Name
     - ``Print_Media``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Print_Media_``
   * - Pattern Properties
     - ``^Print_Media_[A-Za-z0-9_]+$``

.. _print_text-translation:

Print_Text
-----------

Raw text content for media items such as newspapers, describing their content.

.. list-table::
   :widths: auto

   * - File Name
     - ``Print_Text``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Print_Text_``
   * - Pattern Properties
     - ``^Print_Text_[A-Za-z0-9_]+$``

.. _radiodata-translation:

RadioData
----------

Radio translations with the key being a GUID of the radio text.

.. list-table::
   :widths: auto

   * - File Name
     - ``RadioData``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``RD_``
   * - Pattern Properties
     - ``^RD_[a-f0-9-]+$``

.. _recipegroups-translation:

RecipeGroups
-------------

.. list-table::
   :widths: auto

   * - File Name
     - ``RecipeGroups``
   * - Function
     - ``Translator.getRecipeGroupName``
   * - Key Prefix
     - ``RecipeGroup_``
   * - Pattern Properties
     - ``^RecipeGroup_[A-Za-z]+$``

.. _recipes-translation:

Recipes
--------

Translations for the craftRecipe scripts. The key needs to be the ID of the craftRecipe block.

.. list-table::
   :widths: auto

   * - File Name
     - ``Recipes``
   * - Function
     - ``getRecipeDisplayName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_\(\): -]+$``

.. _recorded_media-translation:

Recorded_Media
---------------

Recorded media translations with the key being a GUID of the media text.

.. list-table::
   :widths: auto

   * - File Name
     - ``Recorded_Media``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``RM_``
   * - Pattern Properties
     - ``^RM_[A-Za-z0-9_-]+$``

.. _sandbox-translation:

Sandbox
--------

Sandbox options translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``Sandbox``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Sandbox_``
   * - Pattern Properties
     - ``^Sandbox_[A-Za-z0-9_]+(_option[0-9]+|_tooltip)?$``

.. _stash-translation:

Stash
------

Survivor maps translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``Stash``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Stash_``
   * - Pattern Properties
     - ``^Stash_[A-Za-z0-9_]+$``

.. _survivalguide-translation:

SurvivalGuide
--------------

Survival guide translations.

.. list-table::
   :widths: auto

   * - File Name
     - ``SurvivalGuide``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``SurvivalGuide_``
   * - Pattern Properties
     - ``^SurvivalGuide_[A-Za-z0-9_]+$``

.. _survivornames-translation:

SurvivorNames
--------------

All possible automatic character names. Used for random name generation of the player character or for zombies.

.. list-table::
   :widths: auto

   * - File Name
     - ``SurvivorNames``
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^Survivor(Name|Surname)_[A-Za-z0-9_\s\.'-]+$``

.. _tooltip-translation:

Tooltip
--------

Tooltips used for UIs.

.. list-table::
   :widths: auto

   * - File Name
     - ``Tooltip``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Tooltip_``
   * - Pattern Properties
     - ``^Tooltip_[A-Za-z0-9_]+$``

.. _ui-translation:

UI
---

Translation file for user interface elements.

.. list-table::
   :widths: auto

   * - File Name
     - ``UI``
   * - Function
     - ``getText``
   * - Key Prefix
     - ``UI_``
   * - Pattern Properties
     - ``^UI_[A-Za-z0-9_\s/\-]+$``

