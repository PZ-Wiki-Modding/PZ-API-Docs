.. _component-craftbench:

component CraftBench
====================

Used to add a crafting bench property to an `entity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html>`_ script, which can then be used in the `tags <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#tags>`_ parameter of a `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ script to create a crafting bench tag.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`entity`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _component-craftbench-recipes:

Recipes
^^^^^^^

:Type: array (array of string, separator: ';')

The tag name for this crafting bench to be used in the `tags <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html#tags>`_ parameter of a `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ script.

