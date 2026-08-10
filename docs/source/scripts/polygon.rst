.. _scripts-polygon:

polygon
=======

:Soft Override: Unknown

`box <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/box.html>`_\ , `cylinder <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/cylinder.html>`_ and `polygon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/polygon.html>`_ are used in `tileGeometry.txt <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files/tilegeometry.html>`_ to define the tile depth of a tile.

You can find more information `here <https://pzwiki.net/wiki/Tile_depth>`_.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`tile <scripts-tile>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-polygon-plane:

.. attribute:: plane
   :noindex:

:Type: string

:Allowed values:    ``XY`` | ``XZ`` | ``YZ``

No description provided.


.. _scripts-polygon-points:

.. attribute:: points
   :noindex:

:Type: object (object: integer->>integer, kv: 'x', pairs: ' ')

Defines the points of the polygon. the format needs to be ``X1xY1 X2xY2 X3xY3`` and so on. The first point (X1, Y1) is connected to the second point (X2, Y2), the second point (X2, Y2) is connected to the third point (X3, Y3), and so on. The last point is connected to the first point, creating a closed shape.

You can have as many points as you want.


.. _scripts-polygon-rotate:

.. attribute:: rotate
   :noindex:

:Type: array (array of integer, separator: 'x')

No description provided.


.. _scripts-polygon-translate:

.. attribute:: translate
   :noindex:

:Type: array (array of integer, separator: 'x')

No description provided.


