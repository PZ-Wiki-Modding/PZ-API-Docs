.. _tile:

tile
====

Defines some tile properties of a specific tile on a tileset.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`tileset`

**Possible Child Blocks:**

- :ref:`box`
- :ref:`cylinder`
- :ref:`polygon`
- :ref:`properties`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _tile-animation:

animation
^^^^^^^^^

:Type: Any

No description

.. _tile-animationtime:

animationTime
^^^^^^^^^^^^^

:Type: Any

No description

.. _tile-isprofessiontrait:

IsProfessionTrait
^^^^^^^^^^^^^^^^^

:Type: Any

No description

.. _tile-modelscript:

modelScript
^^^^^^^^^^^

:Type: block (block: :ref:`model`, with :ref:`module`)

No description

.. _tile-rotate:

rotate
^^^^^^

:Type: array (array of integer, separator: ' ')

No description

.. _tile-runtime:

runtime
^^^^^^^

:Type: Any

No description

.. _tile-scale:

scale
^^^^^

:Type: array (array of float, separator: ' ')

No description

.. _tile-translate:

translate
^^^^^^^^^

:Type: array (array of integer, separator: ' ')

No description

.. _tile-xy:

xy
^^

:Type: Any

The position of the tile in the tileset.

If inside a `tileGeometry.txt <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-tilegeometry.html>`_ file, the separator is ``x`` but when inside a `spriteModels.txt <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-spritemodels.html>`_

