.. _scripts-rule:

rule
====

.. attribute:: Soft Override

   Unknown

.. attribute:: No comma

   True

A ``rule`` block defines a conversion rule for the `BMP to TMX <https://pzwiki.net/wiki/BMP_to_TMX>`_ conversion process in the `mapping tools <https://pzwiki.net/wiki/Mapping#Mapping_tools>`_. It is used to associate a color on the BMP for the vegetation or main image to a list of tiles to apply on a specific layer in the TMX.

For example:

.. code-block:: cpp

   rule
   {
     label = Sand
     bitmap = 0
     color = 210 200 160
     tiles = sand
     layer = 0_Floor
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`ROOT-Rules <scripts-root-rules>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-rule-label:

label
^^^^^

.. attribute:: Type

   string

No description provided.


.. _scripts-rule-bitmap:

bitmap
^^^^^^

.. attribute:: Type

   integer

A value of ``1`` will have this rule used for the vegetation image, while a value of ``0`` will have it used for the main tiles image. Trees will for example use ``1`` while ground tiles will use ``0``.


.. _scripts-rule-tiles:

tiles
^^^^^

.. attribute:: Type

   Unknown

A list of tiles to apply randomly for this color. You can also use an alias block here to reference a list of tiles.

For example:

.. code-block:: cpp

   tiles = vegetation_farm_01_35

.. code-block:: cpp

   tiles = [
       vegetation_farm_01_32
       vegetation_farm_01_33
       vegetation_farm_01_34
       vegetation_farm_01_35
       vegetation_farm_01_36
       vegetation_farm_01_37
       vegetation_farm_01_38
       vegetation_farm_01_39
   ]

Or with one or more alias blocks:

.. code-block:: cpp

   alias
   {
       name = treez1
       tiles = [
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

.. code-block:: cpp

   tiles = [
     treez1
   ]


.. _scripts-rule-color:

color
^^^^^

.. attribute:: Type

   array (array of integer, separator: ' ')

The RGB color to replace with the tiles in the ``tiles`` parameter. This is the color you painted in your image file to associate to this rule.


.. _scripts-rule-layer:

layer
^^^^^

.. attribute:: Type

   string

The layer to apply the tiles on.


