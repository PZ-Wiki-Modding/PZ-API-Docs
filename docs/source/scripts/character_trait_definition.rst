.. _scripts-character_trait_definition:

character_trait_definition
==========================

:Soft Override: Unknown

Defines a character trait.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: True


Parameters
----------

.. _scripts-character_trait_definition-isprofessiontrait:

IsProfessionTrait
^^^^^^^^^^^^^^^^^

:Type: boolean
:Required: True

Defines whenever the trait is a profession trait or not, meaning it will only be available when selecting a profession.


.. _scripts-character_trait_definition-disabledinmultiplayer:

DisabledInMultiplayer
^^^^^^^^^^^^^^^^^^^^^

:Type: boolean
:Required: True

If true, this trait will be disabled in multiplayer games.


.. _scripts-character_trait_definition-cost:

Cost
^^^^

:Type: integer
:Required: True

The cost of the trait when selecting a character. Negative values give points, positive values take points.


.. _scripts-character_trait_definition-charactertrait:

CharacterTrait
^^^^^^^^^^^^^^

:Type: string
:Required: True

The registries trait definition ID to link to. see the wiki page about `registries <https://pzwiki.net/wiki/Registries>`_ for more information.


.. _scripts-character_trait_definition-uiname:

UIName
^^^^^^

:Type: string
:Required: True

The translation key for the trait's name. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.


.. _scripts-character_trait_definition-uidescription:

UIDescription
^^^^^^^^^^^^^

:Type: string
:Required: True

The translation key for the trait's description. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.


.. _scripts-character_trait_definition-mutuallyexclusivetraits:

MutuallyExclusiveTraits
^^^^^^^^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

A list of trait IDs that are mutually exclusive with this trait. If one is selected, the others cannot be selected.


.. _scripts-character_trait_definition-xpboosts:

XPBoosts
^^^^^^^^

:Type: object (object: string->>integer, kv: '=', pairs: ';')

A list of experience boosts granted by this trait. Each entry should contain a skill name and the corresponding boost amount.

For example:

.. code-block:: cpp

   XPBoosts = Axe=1;Blunt=1,


.. _scripts-character_trait_definition-grantedrecipes:

GrantedRecipes
^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

A list of `craftRecipe <https://pzwiki.net/wiki/CraftRecipe>`_ IDs that are granted to the character when this trait is selected.


.. _scripts-character_trait_definition-texture:

Texture
^^^^^^^

:Type: string

The path to the trait's icon texture. This should be a .png file located in the textures folder of your mod.


