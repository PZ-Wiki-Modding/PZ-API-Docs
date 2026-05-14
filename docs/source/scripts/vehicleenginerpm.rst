.. _vehicleenginerpm:

vehicleEngineRPM
================

Unclear how the definition of this block works.

Here's the jeep example from the base game:

.. code-block:: cpp

   module Base 
   {
     vehicleEngineRPM jeep
     {
         VERSION = 1,
         data
         {
             gearChange = 3000,
             afterGearChange = 2000,
         }
         data
         {
             gearChange = 3500,
             afterGearChange = 2000,
         }
         data
         {
             gearChange = 4000,
             afterGearChange = 2500,
         }
         data
         {
             gearChange = 4500,
             afterGearChange = 2800,
         }
         data
         {
             gearChange = 6000,
             afterGearChange = 4500,
         }
     }
   }


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`

**Possible Child Blocks:**

- :ref:`data`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _vehicleenginerpm-version:

VERSION
^^^^^^^

:Type: integer

Unclear what this does, preferably keep it at 1.

