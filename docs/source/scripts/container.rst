.. _scripts-container:

container
=========

.. attribute:: Soft Override

   Unknown




Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`part <scripts-part>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-container-capacity:

capacity
^^^^^^^^

.. attribute:: Type

   integer

No description provided.


.. _scripts-container-conditionaffectscapacity:

conditionAffectsCapacity
^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: Type

   boolean

Sets whenever the condition of the part will impact the `capacity <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/container.html#container-capacity>`_. A lower condition will negatively impact the container's capacity.


.. _scripts-container-contenttype:

contentType
^^^^^^^^^^^

.. attribute:: Type

   string

Unclear how this parameter works exactly. The game uses it to define the "content" of tires and gas tanks by providing the string keys ``Gasoline`` or ``Air``. It seems to simply remove any item container being used as the container for this part.


.. _scripts-container-seat:

seat
^^^^

.. attribute:: Type

   string

The seat ID of this container. When present, this container can be used as a seat for a vehicle.


.. _scripts-container-soundmap:

soundMap
^^^^^^^^

.. attribute:: Type

   object (object: string->>block, kv: ' ', pairs: ';')

Register a sound script associated to a type of sound for this container. The syntax should be as follows:

.. code-block:: cpp

   soundMap = key soundRef

The ``key`` can be one of the following:


* ``ContainerClose`` when closing the container
* ``ContainerOpen`` when opening the container
* ``ContainerPut`` when putting an item in the container
* ``ContainerTake`` when taking an item out of the container

The ``soundRef`` should be a reference to a `sound block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_.


.. _scripts-container-test:

test
^^^^

.. attribute:: Type

   string

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


