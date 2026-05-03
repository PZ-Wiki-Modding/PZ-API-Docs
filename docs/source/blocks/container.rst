.. _container:

container
=========




Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`part`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _container-capacity:

capacity
^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

.. _container-conditionaffectscapacity:

conditionAffectsCapacity
^^^^^^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

Sets whenever the condition of the part will impact the `capacity <https://pz-wiki-modding.github.io/pz-scripts-data/blocks/container.html#container-capacity>`_. A lower condition will negatively impact the container's capacity.

.. _container-contenttype:

contentType
^^^^^^^^^^^

   Type: ``{'main': 'string'}``

Unclear how this parameter works exactly. The game uses it to define the "content" of tires and gas tanks by providing the string keys ``Gasoline`` or ``Air``. It seems to simply remove any item container being used as the container for this part.

.. _container-seat:

seat
^^^^

   Type: ``{'main': 'string'}``

The seat ID of this container. When present, this container can be used as a seat for a vehicle.

.. _container-test:

test
^^^^

   Type: ``{'main': 'string'}``

Refers to a Lua global function returning a boolean which is used to determine whether an item can be put in this container when trying to transfer items.

Here's an example from the vanilla game, with the parmeter being set to:

.. code-block:: cpp

   test = Vehicles.ContainerAccess.GloveBox

With the Lua function being defined as:

.. code-block:: lua

   function Vehicles.ContainerAccess.GloveBox(vehicle, part, chr)
     if chr:getVehicle() == vehicle then
       local seat = vehicle:getSeat(chr)
       -- Can the seated player reach the passenger seat?
       -- Only character in front seat can access it
       return seat == 1 or seat == 0;
     elseif chr:getVehicle() then
       -- Can't reach from inside a different vehicle.
       return false
     else
       -- Standing outside the vehicle.
       if not vehicle:isInArea(part:getArea(), chr) then return false end
       local doorPart = vehicle:getPartById("DoorFrontRight")
       if doorPart and doorPart:getDoor() and not doorPart:getDoor():isOpen() then
         return false
       end
       return true
     end
   end

The parameters are:


* ``vehicle`` is a `BaseVehicle <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/vehicles/BaseVehicle.html>`_ class
* ``part`` is a `VehiclePart <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/vehicles/VehiclePart.html>`_
* ``chr`` is an `IsoGameCharacter <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html>`_

