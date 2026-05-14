.. _blend:

blend
=====

Used to define blend rules for the `mapping tools <https://pzwiki.net/wiki/Mapping#Mapping_tools>`_ painting tool.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-blends`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _blend-blendtile:

blendTile
^^^^^^^^^

:Type: Any

Used to define the tiles which will be used for the blend around the ``mainTile``. This can be a single tile or an array of tiles, and it supports ``alias`` blocks.

For example:

.. code-block:: cpp

   blendTile = vegetation_farm_01_35

.. code-block:: cpp

   blendTile = [
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

   blendTile = [
     treez1
   ]

.. _blend-dir:

dir
^^^

:Type: Any

The direction the blend applies to.

Allowed values:

    - ``n``
    - ``ne``
    - ``e``
    - ``se``
    - ``s``
    - ``sw``
    - ``w``
    - ``nw``

.. _blend-exclude:

exclude
^^^^^^^

:Type: Any

A list of tiles which will be excluded from being blended. This can be a single tile or an array of tiles, and it supports ``alias`` blocks.

The format needs to be like this:

.. code-block:: cpp

   exclude = water lightgrass medgrass darkgrass

Where each entries separated by a space are an alias.

.. _blend-exclude2:

exclude2
^^^^^^^^

:Type: Any

No description

.. _blend-layer:

layer
^^^^^

:Type: Any

The layer the blend rule applies to. Should be one of the layers defined in the ``TMXconfig.txt`` file.

.. _blend-maintile:

mainTile
^^^^^^^^

:Type: Any

Used to identify which tiles will trigger the blend. This can be a single tile or an array of tiles, and it supports ``alias`` blocks.

For example:

.. code-block:: cpp

   mainTile = vegetation_farm_01_35

.. code-block:: cpp

   mainTile = [
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

   mainTile = [
     treez1
   ]

