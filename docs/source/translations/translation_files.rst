.. _translation-files:

Translation Files
=================

Available translation file types, their descriptions and properties. The majority of the time the key prefix for translation keys need to be included or they won't work. While this is not always the case, it's preferable to follow these guidelines to avoid issues with missing translations and to make it cleaner when referencing the translation keys in code or scripts.

The pattern properties are patterns that the translation keys must match in order to be valid, they are simply more specific rules than just the prefix if you are interested in knowing the details. Those were defined from the vanilla translation files for the most part and might be incomplete or too specific.

.. _translation-files-Attributes:

Attributes
----------

.. list-table::
   :widths: auto

   * - File Name
     - Attributes
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^Attributes_Type_[A-Za-z_]+$``, ``^Attributes_ToosltipOverride_[A-Za-z_]+$``



.. _translation-files-BodyParts:

BodyParts
---------

.. list-table::
   :widths: auto

   * - File Name
     - BodyParts
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^BODYPART_[A-Z_]+$``



.. _translation-files-Challenge:

Challenge
---------

.. list-table::
   :widths: auto

   * - File Name
     - Challenge
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Challenge_``
   * - Pattern Properties
     - ``^Challenge_[A-Za-z0-9\s]+(_[A-Za-z0-9]+|InfoBox)$``



.. _translation-files-ContextMenu:

ContextMenu
-----------

.. list-table::
   :widths: auto

   * - File Name
     - ContextMenu
   * - Function
     - ``getText``
   * - Key Prefix
     - ``ContextMenu_``
   * - Pattern Properties
     - ``^ContextMenu_[A-Za-z0-9_]+$``

Translations used in the context menus of the game.

.. _translation-files-DynamicRadio:

DynamicRadio
------------

.. list-table::
   :widths: auto

   * - File Name
     - DynamicRadio
   * - Function
     - ``getRadioText``
   * - Key Prefix
     - ``AEBS_``
   * - Pattern Properties
     - ``^AEBS_[A-Za-z0-9_]+$``

Dynamic radio translations.

.. _translation-files-Entity:

Entity
------

.. list-table::
   :widths: auto

   * - File Name
     - Entity
   * - Function
     - ``getText``
   * - Key Prefix
     - ``EC_``
   * - Pattern Properties
     - ``^EC_[A-Za-z_]+$``

Translations for entity UIs.

.. _translation-files-EvolvedRecipeName:

EvolvedRecipeName
-----------------

.. list-table::
   :widths: auto

   * - File Name
     - EvolvedRecipeName
   * - Function
     - ``Translator.getItemEvolvedRecipeName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$``

Translations for evolved recipe scripts.

.. _translation-files-Farming:

Farming
-------

.. list-table::
   :widths: auto

   * - File Name
     - Farming
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Farming_``
   * - Pattern Properties
     - ``^Farming_[A-Za-z0-9_\s-]+$``

Translations for farming menus.

.. _translation-files-Fluids:

Fluids
------

.. list-table::
   :widths: auto

   * - File Name
     - Fluids
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Fluid_``
   * - Pattern Properties
     - ``^Fluid_[A-Za-z0-9_]+$``

Translations for fluid related UI elements and fluid containers.

.. _translation-files-GameSound:

GameSound
---------

.. list-table::
   :widths: auto

   * - File Name
     - GameSound
   * - Function
     - ``getText``
   * - Key Prefix
     - ``GameSound_``
   * - Pattern Properties
     - ``^GameSound_[A-Za-z0-9_]+$``

Game sounds and categories translations.

.. _translation-files-IG_UI:

IG_UI
-----

.. list-table::
   :widths: auto

   * - File Name
     - IG_UI
   * - Function
     - ``getText``
   * - Key Prefix
     - ``IGUI_``
   * - Pattern Properties
     - ``^IGUI_[A-Za-z0-9_\s:\.\/'!-]+$``

Translations for in-game user interface elements.

.. _translation-files-ItemName:

ItemName
--------

.. list-table::
   :widths: auto

   * - File Name
     - ItemName
   * - Function
     - ``getItemNameFromFullType``
   * - Pattern Properties
     - ``^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$``

Translations for item scripts. The key needs to be the full type of the item.

.. _translation-files-Location_Generic:

Location_Generic
----------------

.. list-table::
   :widths: auto


A translation file for the map. The filename needs to refer the file "map.info" in the mod's media folder.

.. _translation-files-MakeUp:

MakeUp
------

.. list-table::
   :widths: auto

   * - File Name
     - MakeUp
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^MakeUp(Category|Type)_[A-Za-z0-9]+$``

Translations for make up.

.. _translation-files-MapLabel:

MapLabel
--------

.. list-table::
   :widths: auto

   * - File Name
     - MapLabel
   * - Function
     - ``getText``
   * - Key Prefix
     - ``MapLabel_``
   * - Pattern Properties
     - ``^MapLabel_[A-Za-z]+$``



.. _translation-files-Mod:

Mod
---

.. list-table::
   :widths: auto

   * - File Name
     - Mod

Translations for the mod.info file. Possible keys are "name" and "description".

.. _translation-files-Moodles:

Moodles
-------

.. list-table::
   :widths: auto

   * - File Name
     - Moodles
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Moodles_``
   * - Pattern Properties
     - ``^Moodles_[A-Za-z0-9_]+(_desc)?_lvl0-9$``

Moodles status and descriptions translations

.. _translation-files-Moveables:

Moveables
---------

.. list-table::
   :widths: auto

   * - File Name
     - Moveables
   * - Function
     - ``Translator.getMoveableDisplayName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_!\s]+$``

Moveable tiles as items translations.

.. _translation-files-MultiStageBuild:

MultiStageBuild
---------------

.. list-table::
   :widths: auto

   * - File Name
     - MultiStageBuild
   * - Function
     - ``Translator.getMultiStageBuild``
   * - Key Prefix
     - ``MultiStageBuild_``
   * - Pattern Properties
     - ``^MultiStageBuild_[A-Za-z0-9_]+$``

Translations for multi stage build.

.. _translation-files-Print_Media:

Print_Media
-----------

.. list-table::
   :widths: auto

   * - File Name
     - Print_Media
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Print_Media_``
   * - Pattern Properties
     - ``^Print_Media_[A-Za-z0-9_]+$``

Text content for media items such as newspapers, describing their content.

.. _translation-files-Print_Text:

Print_Text
----------

.. list-table::
   :widths: auto

   * - File Name
     - Print_Text
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Print_Text_``
   * - Pattern Properties
     - ``^Print_Text_[A-Za-z0-9_]+$``

Raw text content for media items such as newspapers, describing their content.

.. _translation-files-RadioData:

RadioData
---------

.. list-table::
   :widths: auto

   * - File Name
     - RadioData
   * - Function
     - ``getText``
   * - Key Prefix
     - ``RD_``
   * - Pattern Properties
     - ``^RD_[a-f0-9-]+$``

Radio translations with the key being a GUID of the radio text.

.. _translation-files-RecipeGroups:

RecipeGroups
------------

.. list-table::
   :widths: auto

   * - File Name
     - RecipeGroups
   * - Function
     - ``Translator.getRecipeGroupName``
   * - Key Prefix
     - ``RecipeGroup_``
   * - Pattern Properties
     - ``^RecipeGroup_[A-Za-z]+$``



.. _translation-files-Recipes:

Recipes
-------

.. list-table::
   :widths: auto

   * - File Name
     - Recipes
   * - Function
     - ``getRecipeDisplayName``
   * - Pattern Properties
     - ``^[A-Za-z0-9_\(\): -]+$``

Translations for the craftRecipe scripts. The key needs to be the ID of the craftRecipe block.

.. _translation-files-Recorded_Media:

Recorded_Media
--------------

.. list-table::
   :widths: auto

   * - File Name
     - Recorded_Media
   * - Function
     - ``getText``
   * - Key Prefix
     - ``RM_``
   * - Pattern Properties
     - ``^RM_[A-Za-z0-9_-]+$``

Recorded media translations with the key being a GUID of the media text.

.. _translation-files-Sandbox:

Sandbox
-------

.. list-table::
   :widths: auto

   * - File Name
     - Sandbox
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Sandbox_``
   * - Pattern Properties
     - ``^Sandbox_[A-Za-z0-9_]+(_option[0-9]+|_tooltip)?$``

Sandbox options translations.

.. _translation-files-Stash:

Stash
-----

.. list-table::
   :widths: auto

   * - File Name
     - Stash
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Stash_``
   * - Pattern Properties
     - ``^Stash_[A-Za-z0-9_]+$``

Survivor maps translations.

.. _translation-files-SurvivalGuide:

SurvivalGuide
-------------

.. list-table::
   :widths: auto

   * - File Name
     - SurvivalGuide
   * - Function
     - ``getText``
   * - Key Prefix
     - ``SurvivalGuide_``
   * - Pattern Properties
     - ``^SurvivalGuide_[A-Za-z0-9_]+$``

Survival guide translations.

.. _translation-files-SurvivorNames:

SurvivorNames
-------------

.. list-table::
   :widths: auto

   * - File Name
     - SurvivorNames
   * - Function
     - ``getText``
   * - Pattern Properties
     - ``^Survivor(Name|Surname)_[A-Za-z0-9_\s\.'-]+$``

All possible automatic character names. Used for random name generation of the player character or for zombies.

.. _translation-files-Tooltip:

Tooltip
-------

.. list-table::
   :widths: auto

   * - File Name
     - Tooltip
   * - Function
     - ``getText``
   * - Key Prefix
     - ``Tooltip_``
   * - Pattern Properties
     - ``^Tooltip_[A-Za-z0-9_]+$``

Tooltips used for UIs.

.. _translation-files-UI:

UI
--

.. list-table::
   :widths: auto

   * - File Name
     - UI
   * - Function
     - ``getText``
   * - Key Prefix
     - ``UI_``
   * - Pattern Properties
     - ``^UI_[A-Za-z0-9_\s/\-]+$``

Translation file for user interface elements.

