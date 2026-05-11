.. _character_trait_definition:

character_trait_definition
==========================

Defines a character trait.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _character_trait_definition-charactertrait:

CharacterTrait
^^^^^^^^^^^^^^

   Type: ``{'main': 'string'}`` *(required)*

The registries trait definition ID to link to. see the wiki page about `registries <https://pzwiki.net/wiki/Registries>`_ for more information.

.. _character_trait_definition-cost:

Cost
^^^^

   Type: ``{'main': 'integer'}`` *(required)*

The cost of the trait when selecting a character. Negative values give points, positive values take points.

.. _character_trait_definition-disabledinmultiplayer:

DisabledInMultiplayer
^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}`` *(required)*

If true, this trait will be disabled in multiplayer games.

.. _character_trait_definition-grantedrecipes:

GrantedRecipes
^^^^^^^^^^^^^^

   Type: ``{'main': 'array'}``

A list of `craftRecipe <https://pzwiki.net/wiki/CraftRecipe>`_ IDs that are granted to the character when this trait is selected.

.. _character_trait_definition-isprofessiontrait:

IsProfessionTrait
^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}`` *(required)*

Defines whenever the trait is a profession trait or not, meaning it will only be available when selecting a profession.

.. _character_trait_definition-mutuallyexclusivetraits:

MutuallyExclusiveTraits
^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'array'}``

A list of trait IDs that are mutually exclusive with this trait. If one is selected, the others cannot be selected.

.. _character_trait_definition-texture:

Texture
^^^^^^^

   Type: ``{'main': 'string'}``

The path to the trait's icon texture. This should be a .png file located in the textures folder of your mod.

.. _character_trait_definition-uidescription:

UIDescription
^^^^^^^^^^^^^

   Type: ``{'main': 'string'}`` *(required)*

The translation key for the trait's description. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _character_trait_definition-uiname:

UIName
^^^^^^

   Type: ``{'main': 'string'}`` *(required)*

The translation key for the trait's name. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.

.. _character_trait_definition-xpboosts:

XPBoosts
^^^^^^^^

   Type: ``{'main': 'array'}``

A list of experience boosts granted by this trait. Each entry should contain a skill name and the corresponding boost amount.

For example:

.. code-block:: cpp

   XPBoosts = Axe=1;Blunt=1,

