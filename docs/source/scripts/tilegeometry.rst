.. _scripts-tilegeometry:

tileGeometry
============

:Soft Override: Unknown

Used to define tile geometries for each `tile <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/tile.html>`_ in a `tileset <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/tileset.html>`_.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`ROOT-TileGeometry <scripts-root-tilegeometry>`

This block can have the following child blocks:

- :ref:`tileset <scripts-tileset>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-tilegeometry-version:

VERSION
^^^^^^^

:Type: integer
:Allowed values: 
* ``1``
* ``2``

The version of the tile geometry file format. The vanilla files use version ``2``.

If the value is ``1``\ :


* coordinates will be parsed as is

If the value is ``2``\ :


* coordinates will be divided by 10000


