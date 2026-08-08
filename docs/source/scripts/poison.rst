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

.. _scripts-poison-diluteratio:

.. attribute:: diluteRatio
   :noindex:

:Type: float

The ratio at which the poison is diluted when mixed with other fluids.


.. _scripts-poison-maxeffect:

.. attribute:: maxEffect
   :noindex:

:Type: string

:Allowed values:    ``Deadly`` | ``Extreme`` | ``Medium`` | ``Mild`` | ``None`` | ``Severe``

Defines the strength of the poison.


.. _scripts-poison-minamount:

.. attribute:: minAmount
   :noindex:

:Type: float

The minimum amount required to consume to poison the player.


