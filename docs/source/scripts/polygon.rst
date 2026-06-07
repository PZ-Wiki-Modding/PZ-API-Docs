.. _polygon:

polygon
=======

`box <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/box.html>`_\ , `cylinder <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/cylinder.html>`_ and `polygon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/polygon.html>`_ are used in `tileGeometry.txt <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-tilegeometry.html>`_ to define the tile depth of a tile.

You can find more information `here <https://pzwiki.net/wiki/Tile_depth>`_.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`tile`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _polygon-plane:

plane
^^^^^

:Type: string

No description

Allowed values:

    - ``XY``
    - ``XZ``
    - ``YZ``

.. _polygon-points:

points
^^^^^^

:Type: object (object: integer->>integer, kv: 'x', pairs: ' ')

Defines the points of the polygon. the format needs to be ``X1xY1 X2xY2 X3xY3`` and so on. The first point (X1, Y1) is connected to the second point (X2, Y2), the second point (X2, Y2) is connected to the third point (X3, Y3), and so on. The last point is connected to the first point, creating a closed shape.

You can have as many points as you want.

.. _polygon-rotate:

rotate
^^^^^^

 (see :ref:`box-translate`)
:Type: array (array of integer, separator: 'x')

No description

.. _polygon-translate:

translate
^^^^^^^^^

 (see :ref:`box-translate`)
:Type: array (array of integer, separator: 'x')

No description

