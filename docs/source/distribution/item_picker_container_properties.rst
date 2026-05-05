ItemPickerContainer properties
==============================

Reference documentation for ItemPickerContainer procedural list entry properties. Those are used to define the procedural distributions which will be used for the containers of the rooms.

.. _item-picker-property-name:

name
----

The procedural distribution entry name.


.. _item-picker-property-min:

min
---

A minimum value of 1 will force this entry to spawn.


.. _item-picker-property-max:

max
---

The maximum number of times this procedural distribution entry can spawn.


.. _item-picker-property-weightChance:

weightChance
------------


.. _item-picker-property-forceForItems:

forceForItems
-------------

If the container's room has one of those tiles, this procedural distribution entry will be forced to spawn.

**Type:**

- Main: ``array``
- Separator: ``;``


.. _item-picker-property-forceForTiles:

forceForTiles
-------------

If the square of the container has one of those tiles, this procedural distribution entry will be forced to spawn.

**Type:**

- Main: ``array``
- Separator: ``;``


.. _item-picker-property-forceForRooms:

forceForRooms
-------------

If the building of the container has one of those rooms, this procedural distribution entry will be forced to spawn.

**Type:**

- Main: ``array``
- Separator: ``;``


.. _item-picker-property-forceForZones:

forceForZones
-------------

**Type:**

- Main: ``array``
- Separator: ``;``

.. warning::

   This property does nothing and has no effect.


