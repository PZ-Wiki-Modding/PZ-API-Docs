.. _scripts-vehicle:

vehicle
=======

:Soft Override: Unknown

Defines a vehicle.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`

This block can have the following child blocks:

- :ref:`model <scripts-model>`
- :ref:`lightbar <scripts-lightbar>`
- :ref:`passenger <scripts-passenger>`
- :ref:`area <scripts-area>`
- :ref:`part <scripts-part>`
- :ref:`attachment <scripts-attachment>`
- :ref:`sound <scripts-sound>`
- :ref:`wheel <scripts-wheel>`
- :ref:`physics <scripts-physics>`
- :ref:`skin <scripts-skin>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


Parameters
----------

.. _scripts-vehicle-animaltrailersize:

animalTrailerSize
^^^^^^^^^^^^^^^^^

:Type: float

Sets the maximum total encumbrance from animals in the animal trailer. The horsebox and livestock trailers both use 500.


.. _scripts-vehicle-brakingforce:

brakingForce
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-vehicle-carmechanicsoverlay:

carMechanicsOverlay
^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-carmodelname:

carModelName
^^^^^^^^^^^^

:Type: string

Set the `translation <https://pzwiki.net/wiki/Translation>`_ key for the car name. The translation entry needs to be stored inside the IG_UI translation file and have ``IGUI_VehicleName`` as a prefix. 

For example:

.. code-block:: cpp

   carModelName = YourCar,

With the translation entry inside ``IG_UI.json``\ :

.. code-block:: json

   {
     "IGUI_VehicleNameYourCar": "Your car model"
   }


.. _scripts-vehicle-centerofmassoffset:

centerOfMassOffset
^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-vehicle-engineforce:

engineForce
^^^^^^^^^^^

:Type: float
:Default: ``3000``

engineForce is 10x what is displayed in the mechanics menu for horsepower.


.. _scripts-vehicle-engineidlespeed:

engineIdleSpeed
^^^^^^^^^^^^^^^

:Type: float
:Default: ``750.0``

No description provided.


.. _scripts-vehicle-engineloudness:

engineLoudness
^^^^^^^^^^^^^^

:Type: integer
:Default: ``100``

No description provided.


.. _scripts-vehicle-enginequality:

engineQuality
^^^^^^^^^^^^^

:Type: integer
:Default: ``100``

No description provided.


.. _scripts-vehicle-enginerepairlevel:

engineRepairLevel
^^^^^^^^^^^^^^^^^

:Type: integer

Required `mechanics skill <https://pzwiki.net/wiki/Mechanics>`_ level for repearing the vehicle's engine.


.. _scripts-vehicle-enginerpmtype:

engineRPMType
^^^^^^^^^^^^^

:Type: string
:Default: ``jeep``

Sets the engine to a RPM type (\ `See vehicleEngineRPM block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicleenginerpm.html>`_\ ).


.. _scripts-vehicle-extents:

extents
^^^^^^^

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-extentsoffset:

extentsOffset
^^^^^^^^^^^^^

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-forcedcolor:

forcedColor
^^^^^^^^^^^

:Type: array (array of float, separator: ' ')
:Default: ``-1 -1 -1``

Sets a forced HSV color on the vehicle. The value needs to be of format ``hue sat val``.


.. _scripts-vehicle-frontenddurability:

frontEndDurability
^^^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``100``

It is unclear what that parameter does but as of 42.16.3, the game uses ``frontEndHealth`` which is a mistake.


.. _scripts-vehicle-frontendhealth:

frontEndHealth
^^^^^^^^^^^^^^

:Type: Unknown
:Deprecated: {'description': 'While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as `frontEndHealth` but as `frontEndDurability`.', 'replacedBy': 'frontEndDurability'}

No description provided.


.. _scripts-vehicle-gearratior:

gearRatioR
^^^^^^^^^^

:Type: float
:Default: ``7.09``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio1:

gearRatio1
^^^^^^^^^^

:Type: float
:Default: ``6.44``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio2:

gearRatio2
^^^^^^^^^^

:Type: Unknown
:Default: ``4.1``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio3:

gearRatio3
^^^^^^^^^^

:Type: Unknown
:Default: ``2.29``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio4:

gearRatio4
^^^^^^^^^^

:Type: Unknown
:Default: ``1.47``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio5:

gearRatio5
^^^^^^^^^^

:Type: Unknown
:Default: ``1.0``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio6:

gearRatio6
^^^^^^^^^^

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio7:

gearRatio7
^^^^^^^^^^

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio8:

gearRatio8
^^^^^^^^^^

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratiocount:

gearRatioCount
^^^^^^^^^^^^^^

:Type: integer
:Default: ``4``

`gearRatioCount <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratiocount>`_ will set the number of gear ratios the car can have. The vanilla cars use 4, while sport cars use 5. 

A maximum of 9 ratios can be set with the parameters:


* `gearRatioR <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratiocount>`_ (the reverse gear ratio)
* `gearRatio1 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio1>`_
* `gearRatio2 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio2>`_
* `gearRatio3 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio3>`_
* `gearRatio4 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio4>`_
* `gearRatio5 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio5>`_
* `gearRatio6 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio6>`_
* `gearRatio7 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio7>`_
* `gearRatio8 <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-gearratio8>`_

Those ratios take floats


.. _scripts-vehicle-haslighter:

hasLighter
^^^^^^^^^^

:Type: boolean
:Default: ``True``

Sets whenever this car has a lighter to light a cigarette.


.. _scripts-vehicle-hassiren:

hasSiren
^^^^^^^^

:Type: boolean
:Is useless: True

No description provided.


.. _scripts-vehicle-issmallvehicle:

isSmallVehicle
^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

No description provided.


.. _scripts-vehicle-mass:

mass
^^^^

:Type: float
:Default: ``800``

Sets the mass of the vehicle which will notably be used for various physic calculations. 

By default is equal to 800. As a reference, a car has a mass of around 800, pickup trucks have around 1100, a simple trailer around 200, a burnt vehicle 400 or 500. See the game scripts for more examples. Values in excess of 1400 can cause vehicle wheels to start sinking into the ground and be unable to move.


.. _scripts-vehicle-maxspeed:

maxSpeed
^^^^^^^^

:Type: float
:Default: ``20.0``

No description provided.


.. _scripts-vehicle-maxspeedreverse:

maxSpeedReverse
^^^^^^^^^^^^^^^

:Type: float
:Default: ``40.0``

No description provided.


.. _scripts-vehicle-maxsuspensiontravelcm:

maxSuspensionTravelCm
^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``500.0``

No description provided.


.. _scripts-vehicle-mechanictype:

mechanicType
^^^^^^^^^^^^

:Type: integer
:Allowed values: 
* ``1``
* ``2``
* ``3``

Defines what class the vehicle is, that is 1 for standard, 2 for heavy-duty and 3 for performance.


.. _scripts-vehicle-neverspawnkey:

neverSpawnKey
^^^^^^^^^^^^^

:Type: boolean

Sets whenever this vehicle will never have a key spawning in buildings or on zombies spawning around the vehicle.


.. _scripts-vehicle-notkillcrops:

notKillCrops
^^^^^^^^^^^^

:Type: boolean

Sets whenever the vehicle will destroy crops it is driving on.


.. _scripts-vehicle-offroadefficiency:

offRoadEfficiency
^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

Affects horsepower reduction when offroad (Higher = less horsepower reduction when offroad.)


.. _scripts-vehicle-physicschassisshape:

physicsChassisShape
^^^^^^^^^^^^^^^^^^^

:Type: array (array of float, separator: ' ')

Defines the hitbox of the vehicle. The value should be three numbers defining the dimensions of a box:

.. code-block::

   physicsChassisShape = height width length,

For example:

.. code-block::

   physicsChassisShape = height width length,

When setting `useChassisPhysicsCollision <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-usechassisphysicscollision>`_ to ``false``\ , it will instead use `physics <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/physics.html>`_ for the hitbox of the vehicle.


.. _scripts-vehicle-playerdamageprotection:

playerDamageProtection
^^^^^^^^^^^^^^^^^^^^^^

:Type: float

Multiplier applied to the amount of damage the player takes when crashing in the car. A value of 1 doesn't change the damage, but a lower value reduces it and a higher value increases it.


.. _scripts-vehicle-rearenddurability:

rearEndDurability
^^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``100``

It is unclear what that parameter does but as of 42.16.3, the game uses ``rearEndHealth`` which is a mistake.


.. _scripts-vehicle-rearendhealth:

rearEndHealth
^^^^^^^^^^^^^

:Type: Unknown
:Deprecated: {'description': 'While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as `rearEndHealth` but as `rearEndDurability`.', 'replacedBy': 'rearEndDurability'}

No description provided.


.. _scripts-vehicle-rollinfluence:

rollInfluence
^^^^^^^^^^^^^

:Type: float
:Default: ``0.1``

No description provided.


.. _scripts-vehicle-seats:

seats
^^^^^

:Type: integer
:Default: ``2``

Sets the number of seats this vehicle can have. A seat `part <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/part.html>`_ needs to be created which will hold a `container <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/container.html#container>`_ block with a parameter `seat <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/container.html#container-seat>`_


.. _scripts-vehicle-shadowextents:

shadowExtents
^^^^^^^^^^^^^

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-shadowoffset:

shadowOffset
^^^^^^^^^^^^

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-specialkeyring:

specialKeyRing
^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

``specialKeyRing`` needs to reference a keyring item to spawn. ``specialKeyRingChance`` is used to set the chance to spawn this keyring.


.. _scripts-vehicle-specialkeyringchance:

specialKeyRingChance
^^^^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`specialKeyRing <scripts-vehicle-specialkeyring>`.


.. _scripts-vehicle-speciallootchance:

specialLootChance
^^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``8``

No description provided.


.. _scripts-vehicle-steeringclamp:

steeringClamp
^^^^^^^^^^^^^

:Type: float
:Default: ``0.4``

Maximum angle you can turn the front wheels left/right


.. _scripts-vehicle-steeringincrement:

steeringIncrement
^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``0.04``

No description provided.


.. _scripts-vehicle-stoppingmovementforce:

stoppingMovementForce
^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

A drag factor applied to the vehicle at all times


.. _scripts-vehicle-storagecapacity:

storageCapacity
^^^^^^^^^^^^^^^

:Type: integer
:Is useless: True
:Default: ``100``

No description provided.


.. _scripts-vehicle-suspensioncompression:

suspensionCompression
^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``4.4``

No description provided.


.. _scripts-vehicle-suspensiondamping:

suspensionDamping
^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``2.3``

No description provided.


.. _scripts-vehicle-suspensionrestlength:

suspensionRestLength
^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``0.6``

No description provided.


.. _scripts-vehicle-suspensionstiffness:

suspensionStiffness
^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``20.0``

No description provided.


.. _scripts-vehicle-template:

template
^^^^^^^^

:Type: Unknown

Uses a template script data for this vehicle.


.. _scripts-vehicle-template!:

template!
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-vehicle-texturedamage1overlay:

textureDamage1Overlay
^^^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage1shell:

textureDamage1Shell
^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage2overlay:

textureDamage2Overlay
^^^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage2shell:

textureDamage2Shell
^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturelights:

textureLights
^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturemask:

textureMask
^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-texturemaskenable:

textureMaskEnable
^^^^^^^^^^^^^^^^^

:Type: boolean
:Is useless: True

No description provided.


.. _scripts-vehicle-texturerust:

textureRust
^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-textureshadow:

textureShadow
^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-vehicle-usechassisphysicscollision:

useChassisPhysicsCollision
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

By default ``true`` which makes the vehicle use the `physicsChassisShape <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-physicschassisshape>`_ for its hitbox. If set to false, it will instead use the `physics <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/physics.html>`_ blocks as the hitbox of the vehicle.


.. _scripts-vehicle-wheelfriction:

wheelFriction
^^^^^^^^^^^^^

:Type: float
:Default: ``800.0``

It is 1.2 to 1.9 for all vanilla vehicles and controls turning and stopping (but not acceleration) tire friction limits, with 1.4 being the most common. Values over 1.8 can cause vehicles to flip in sharp turns. (Likely depends somewhat on center of mass)


.. _scripts-vehicle-zombietype:

zombieType
^^^^^^^^^^

:Type: array (array of string, separator: ';')

Used to chose what zombie may spawn around the vehicle and is likely to have the key of the vehicle.


