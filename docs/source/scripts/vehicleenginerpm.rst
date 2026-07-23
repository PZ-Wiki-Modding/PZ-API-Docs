.. _scripts-vehicleenginerpm:

vehicleEngineRPM
================

.. attribute:: Soft Override

   Unknown

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

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`

This block can have the following child blocks:

- :ref:`data <scripts-data>`



ID
--

This block can have an ID.

.. attribute:: Optional

   False

.. attribute:: Can have spaces

   False


Parameters
----------

.. _scripts-vehicleenginerpm-version:

VERSION
^^^^^^^

.. attribute:: Type

   integer

Unclear what this does, preferably keep it at 1.


