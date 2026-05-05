.. _alias:

alias
=====

Defines an alias for a list of tiles. This can be directly be refered to in `rule <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/rule.html>`_ blocks to list a bunch of tiles in different blocks or to organize them by type. Say for example you can list all the trees in an alias to use later, or split by tree type to easily associate to a color.

Here is an example of how to use it:

.. code-block:: cpp

   alias
   {
       name = treez1
       tiles = [
           e_americanholly_1_3
           e_americanholly_1_2
           e_americanholly_1_1
           e_americanlinden_1_11
           e_americanlinden_1_10
           e_americanlinden_1_15
           e_americanlinden_1_14
           e_canadianhemlock_1_3
           e_canadianhemlock_1_2
           e_canadianhemlock_1_1
           e_carolinasilverbell_1_15
           e_carolinasilverbell_1_14
           e_cockspurhawthorn_1_15
           e_cockspurhawthorn_1_14
           e_cockspurhawthorn_1_13
           e_dogwood_1_15
           e_dogwood_1_14
           e_easternredbud_1_15
           e_easternredbud_1_14
           vegetation_trees_01_13
           vegetation_trees_01_14
           vegetation_trees_01_15
           vegetation_trees_01_8
           vegetation_trees_01_9
           vegetation_trees_01_10
           vegetation_trees_01_11
           vegetation_trees_01_17
       ]
   }

   rule
   {
       label = General Trees
       bitmap = 1
       color = 139 156 68
       tiles = [
         treez1
       ]
       layer = 0_Vegetation
   }


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-rules`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _alias-name:

name
^^^^

   Type: ``{'main': 'string'}``

No description

.. _alias-tiles:

tiles
^^^^^

   Type: ``Any``

No description

