.. _scripts-poison:

Poison
======

:Soft Override: Unknown

Defines poison properties for a fluid script.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`fluid <scripts-fluid>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-poison-maxeffect:

maxEffect
^^^^^^^^^

:Type: string
:Allowed values: 
* ``None``
* ``Mild``
* ``Medium``
* ``Severe``
* ``Extreme``
* ``Deadly``

Defines the strength of the poison.


.. _scripts-poison-minamount:

minAmount
^^^^^^^^^

:Type: float

The minimum amount required to consume to poison the player.


.. _scripts-poison-diluteratio:

diluteRatio
^^^^^^^^^^^

:Type: float

The ratio at which the poison is diluted when mixed with other fluids.


