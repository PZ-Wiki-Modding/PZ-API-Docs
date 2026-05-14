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

:Type: float

The ratio at which the poison is diluted when mixed with other fluids.

.. _poison-maxeffect:

maxEffect
^^^^^^^^^

:Type: string

Defines the strength of the poison.

Allowed values:

    - ``None``
    - ``Mild``
    - ``Medium``
    - ``Severe``
    - ``Extreme``
    - ``Deadly``

.. _poison-minamount:

minAmount
^^^^^^^^^

:Type: float

The minimum amount required to consume to poison the player.

