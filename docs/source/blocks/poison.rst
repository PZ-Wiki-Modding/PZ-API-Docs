.. _poison:

Poison
======

Defines poison properties for a fluid script.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`fluid`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _poison-diluteratio:

diluteRatio
^^^^^^^^^^^

   Type: ``{'main': 'float'}``

The ratio at which the poison is diluted when mixed with other fluids.

.. _poison-maxeffect:

maxEffect
^^^^^^^^^

   Type: ``{'main': 'string'}``

Defines the strength of the poison.

   Allowed values:

   - ``Deadly``
   - ``Medium``

.. _poison-minamount:

minAmount
^^^^^^^^^

   Type: ``{'main': 'float'}``

The minimum amount required to consume to poison the player.

