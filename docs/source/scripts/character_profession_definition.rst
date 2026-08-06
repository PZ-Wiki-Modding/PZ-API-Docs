.. _scripts-character_profession_definition:

character_profession_definition
===============================

:Soft Override: Unknown

Defines a character profession.

.. code-block:: cpp

   character_profession_definition yourmod:example_profession
   {
       CharacterProfession = yourmod:example_profession,
       Cost = -6,
       UIName = UI_prof_MetalWorker,
       UIDescription = UI_profdesc_metalworker,
       IconPathName = profession_metalworker,
       XPBoosts = MetalWelding=4,
       GrantedRecipes = Advanced_Forge;Blast_Furnace,
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

:Optional: False

:Can have spaces: False


Parameters
----------

.. _scripts-character_profession_definition-characterprofession:

.. attribute:: CharacterProfession
   :noindex:

:Type: string

The `registries <https://pzwiki.net/wiki/Registries>`_ profession ID to link to.


.. _scripts-character_profession_definition-cost:

.. attribute:: Cost
   :noindex:

:Type: integer

The cost of the profession when selecting a character. Negative values remove points, positive values add points.


.. _scripts-character_profession_definition-uiname:

.. attribute:: UIName
   :noindex:

:Type: string

The translation key for the profession's name. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.


.. _scripts-character_profession_definition-uidescription:

.. attribute:: UIDescription
   :noindex:

:Type: string

The translation key for the profession's description. The translation key needs to be in the UI translation file. See the wiki page about `translations <https://pzwiki.net/wiki/Translations>`_ for more information.


.. _scripts-character_profession_definition-iconpathname:

.. attribute:: IconPathName
   :noindex:

:Type: string

No description provided.


.. _scripts-character_profession_definition-grantedtraits:

.. attribute:: GrantedTraits
   :noindex:

:Type: array (array of string, separator: ';')

A list of character trait IDs that are granted to the character when this profession is selected.


.. _scripts-character_profession_definition-xpboosts:

.. attribute:: XPBoosts
   :noindex:

:Type: object (object: string->>integer, kv: '=', pairs: ';')

A list of experience boosts granted by this profession. Each entry should contain a skill name and the corresponding boost amount.

For example:

.. code-block:: cpp

   XPBoosts = Axe=1;Blunt=1,


.. _scripts-character_profession_definition-grantedrecipes:

.. attribute:: GrantedRecipes
   :noindex:

:Type: array (array of string, separator: ';')

A list of `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ IDs that are granted to the character when this profession is selected.


