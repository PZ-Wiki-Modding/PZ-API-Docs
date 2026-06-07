.. _tilegeometry:

tileGeometry
============

Used to define tile geometries for each `tile <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/tile.html>`_ in a `tileset <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/tileset.html>`_.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-tilegeometry`

**Possible Child Blocks:**

- :ref:`tileset`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _tilegeometry-version:

VERSION
^^^^^^^

:Type: integer

The version of the tile geometry file format. The vanilla files use version ``2``.

If the value is ``1``\ :


* coordinates will be parsed as is

If the value is ``2``\ :


* coordinates will be divided by 10000

Allowed values:

    - ``1``
    - ``2``

