.. _scripts-component-craftbench:

component CraftBench
====================

:Soft Override: Unknown
:Is Variant of: :ref:`component <scripts-component>`

Used to add a crafting bench property to an `entity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html>`_ script, which can then be used in the `tags <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#tags>`_ parameter of a `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ script to create a crafting bench tag.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`entity <scripts-entity>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-component-craftbench-recipes:

Recipes
^^^^^^^

:Type: array (array of string, separator: ';')

The tag name for this crafting bench to be used in the `tags <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#tags>`_ parameter of a `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ script.


