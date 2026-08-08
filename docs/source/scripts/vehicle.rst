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

- :ref:`physics <scripts-physics>`
- :ref:`attachment <scripts-attachment>`
- :ref:`part <scripts-part>`
- :ref:`passenger <scripts-passenger>`
- :ref:`wheel <scripts-wheel>`
- :ref:`model <scripts-model>`
- :ref:`lightbar <scripts-lightbar>`
- :ref:`sound <scripts-sound>`
- :ref:`area <scripts-area>`
- :ref:`skin <scripts-skin>`



ID
--

This block can have an ID.

:Optional: False

:Can have spaces: False


Parameters
----------

.. _scripts-vehicle-animaltrailersize:

.. attribute:: animalTrailerSize
   :noindex:

:Type: float

Sets the maximum total encumbrance from animals in the animal trailer. The horsebox and livestock trailers both use 500.


.. _scripts-vehicle-brakingforce:

.. attribute:: brakingForce
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-vehicle-carmechanicsoverlay:

.. attribute:: carMechanicsOverlay
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-carmodelname:

.. attribute:: carModelName
   :noindex:

:Type: string

Set the `translation <https://pzwiki.net/wiki/Translation>`_ key for the car name. The translation entry needs to be stored inside the `IG_UI <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#ig-ui>`_ translation file and have ``IGUI_VehicleName`` as a prefix. For example:

.. code-block:: cpp

   carModelName = YourCar,

With the translation entry inside ``IG_UI.json``\ :

.. code-block:: json

   {
     "IGUI_VehicleNameYourCar": "Your car model"
   }


.. _scripts-vehicle-centerofmassoffset:

.. attribute:: centerOfMassOffset
   :noindex:

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-engineforce:

.. attribute:: engineForce
   :noindex:

:Type: float

:Default: ``3000``

``engineForce`` is 10x what is displayed in the mechanics menu for horsepower.


.. _scripts-vehicle-engineidlespeed:

.. attribute:: engineIdleSpeed
   :noindex:

:Type: float

:Default: ``750.0``

No description provided.


.. _scripts-vehicle-engineloudness:

.. attribute:: engineLoudness
   :noindex:

:Type: integer

:Default: ``100``

No description provided.


.. _scripts-vehicle-enginequality:

.. attribute:: engineQuality
   :noindex:

:Type: integer

:Default: ``100``

No description provided.


.. _scripts-vehicle-enginerepairlevel:

.. attribute:: engineRepairLevel
   :noindex:

:Type: integer

Required `mechanics skill <https://pzwiki.net/wiki/Mechanics>`_ level for repearing the vehicle's engine.


.. _scripts-vehicle-enginerpmtype:

.. attribute:: engineRPMType
   :noindex:

:Type: string

:Default: ``jeep``

Sets the engine to a RPM type (\ `See vehicleEngineRPM block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicleenginerpm.html>`_\ ).


.. _scripts-vehicle-extents:

.. attribute:: extents
   :noindex:

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-extentsoffset:

.. attribute:: extentsOffset
   :noindex:

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-forcedcolor:

.. attribute:: forcedColor
   :noindex:

:Type: array (array of float, separator: ' ')

:Default: ``-1 -1 -1``

Sets a forced HSV color on the vehicle. The value needs to be of format ``hue sat val``.


.. _scripts-vehicle-frontenddurability:

.. attribute:: frontEndDurability
   :noindex:

:Type: integer

:Default: ``100``

It is unclear what that parameter does but as of 42.16.3, the game uses ``frontEndHealth`` which is a mistake.


.. _scripts-vehicle-frontendhealth:

.. attribute:: frontEndHealth
   :noindex:

:Type: Unknown

:Deprecated: {'description': 'While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as `frontEndHealth` but as `frontEndDurability`.', 'replacedBy': 'frontEndDurability'}

No description provided.


.. _scripts-vehicle-gearratio1:

.. attribute:: gearRatio1
   :noindex:

:Type: float

:Default: ``6.44``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio2:

.. attribute:: gearRatio2
   :noindex:

:Type: Unknown

:Default: ``4.1``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio3:

.. attribute:: gearRatio3
   :noindex:

:Type: Unknown

:Default: ``2.29``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio4:

.. attribute:: gearRatio4
   :noindex:

:Type: Unknown

:Default: ``1.47``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio5:

.. attribute:: gearRatio5
   :noindex:

:Type: Unknown

:Default: ``1.0``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio6:

.. attribute:: gearRatio6
   :noindex:

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio7:

.. attribute:: gearRatio7
   :noindex:

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratio8:

.. attribute:: gearRatio8
   :noindex:

:Type: Unknown

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-gearratiocount:

.. attribute:: gearRatioCount
   :noindex:

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


.. _scripts-vehicle-gearratior:

.. attribute:: gearRatioR
   :noindex:

:Type: float

:Default: ``7.09``

See parameter :ref:`gearRatioCount <scripts-vehicle-gearratiocount>`.


.. _scripts-vehicle-haslighter:

.. attribute:: hasLighter
   :noindex:

:Type: boolean

:Default: ``True``

Sets whenever this car has a lighter to light a cigarette.


.. _scripts-vehicle-hassiren:

.. attribute:: hasSiren
   :noindex:

:Type: boolean

:Is useless: True

This is unused by the game.


.. _scripts-vehicle-issmallvehicle:

.. attribute:: isSmallVehicle
   :noindex:

:Type: boolean

:Default: ``True``

If the vehicle a small vehicle, the zombies will bang on the windows differently. If set to false they will thump by banging while if set to true, they will thump with their shoulder.


.. _scripts-vehicle-mass:

.. attribute:: mass
   :noindex:

:Type: float

:Default: ``800``

Sets the mass of the vehicle which will notably be used for various physic calculations. 

By default is equal to 800. As a reference, cars have a mass of around 800, pickup trucks have around 1100, a simple trailer around 200, a burnt vehicle 400 or 500. See the game scripts for more examples. Values in excess of 1400 can cause vehicle wheels to start sinking into the ground and be unable to move.


.. _scripts-vehicle-maxspeed:

.. attribute:: maxSpeed
   :noindex:

:Type: float

:Default: ``20.0``

No description provided.


.. _scripts-vehicle-maxspeedreverse:

.. attribute:: maxSpeedReverse
   :noindex:

:Type: float

:Default: ``40.0``

No description provided.


.. _scripts-vehicle-maxsuspensiontravelcm:

.. attribute:: maxSuspensionTravelCm
   :noindex:

:Type: float

:Default: ``500.0``

No description provided.


.. _scripts-vehicle-mechanictype:

.. attribute:: mechanicType
   :noindex:

:Type: integer

:Allowed values:    ``1`` | ``2`` | ``3``

Defines what class the vehicle is, that is 1 for standard, 2 for heavy-duty and 3 for performance.


.. _scripts-vehicle-neverspawnkey:

.. attribute:: neverSpawnKey
   :noindex:

:Type: boolean

Sets whenever this vehicle will never have a key spawning in buildings or on zombies spawning around the vehicle.


.. _scripts-vehicle-notkillcrops:

.. attribute:: notKillCrops
   :noindex:

:Type: boolean

Sets whenever the vehicle will destroy crops it is driving on.


.. _scripts-vehicle-offroadefficiency:

.. attribute:: offRoadEfficiency
   :noindex:

:Type: float

:Default: ``1.0``

Affects horsepower reduction when offroad (Higher = less horsepower reduction when offroad.)


.. _scripts-vehicle-physicschassisshape:

.. attribute:: physicsChassisShape
   :noindex:

:Type: array (array of float, separator: ' ')

Defines the hitbox of the vehicle. The value should be three numbers defining the dimensions of a box:

.. code-block::

   physicsChassisShape = height width length,

For example:

.. code-block::

   physicsChassisShape = height width length,

When setting `useChassisPhysicsCollision <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-usechassisphysicscollision>`_ to ``false``\ , it will instead use `physics <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/physics.html>`_ for the hitbox of the vehicle.


.. _scripts-vehicle-playerdamageprotection:

.. attribute:: playerDamageProtection
   :noindex:

:Type: float

Multiplier applied to the amount of damage the player takes when crashing in the car. A value of 1 doesn't change the damage, but a lower value reduces it and a higher value increases it.


.. _scripts-vehicle-rearenddurability:

.. attribute:: rearEndDurability
   :noindex:

:Type: integer

:Default: ``100``

It is unclear what that parameter does but as of 42.16.3, the game uses ``rearEndHealth`` which is a mistake.


.. _scripts-vehicle-rearendhealth:

.. attribute:: rearEndHealth
   :noindex:

:Type: Unknown

:Deprecated: {'description': 'While that parameter is present in vanilla scripts as of 42.16.3, it actually does nothing because it is not parsed as `rearEndHealth` but as `rearEndDurability`.', 'replacedBy': 'rearEndDurability'}

No description provided.


.. _scripts-vehicle-rollinfluence:

.. attribute:: rollInfluence
   :noindex:

:Type: float

:Default: ``0.1``

No description provided.


.. _scripts-vehicle-seats:

.. attribute:: seats
   :noindex:

:Type: integer

:Default: ``2``

Sets the number of seats this vehicle can have. A seat `part <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/part.html>`_ needs to be created which will hold a `container <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/container.html#container>`_ block with a parameter `seat <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/container.html#container-seat>`_.


.. _scripts-vehicle-shadowextents:

.. attribute:: shadowExtents
   :noindex:

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-shadowoffset:

.. attribute:: shadowOffset
   :noindex:

:Type: array (array of float, separator: ' ')

No description provided.


.. _scripts-vehicle-specialkeyring:

.. attribute:: specialKeyRing
   :noindex:

:Type: array (array of string, separator: ';')

`specialKeyRing <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-specialkeyring>`_ needs to reference a keyring item to spawn. `specialKeyRingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-specialkeyringchance>`_ is used to set the chance to spawn this keyring.


.. _scripts-vehicle-specialkeyringchance:

.. attribute:: specialKeyRingChance
   :noindex:

:Type: integer

See parameter :ref:`specialKeyRing <scripts-vehicle-specialkeyring>`.


.. _scripts-vehicle-speciallootchance:

.. attribute:: specialLootChance
   :noindex:

:Type: integer

:Default: ``8``

No description provided.


.. _scripts-vehicle-steeringclamp:

.. attribute:: steeringClamp
   :noindex:

:Type: float

:Default: ``0.4``

Maximum angle you can turn the front wheels left/right


.. _scripts-vehicle-steeringincrement:

.. attribute:: steeringIncrement
   :noindex:

:Type: float

:Default: ``0.04``

No description provided.


.. _scripts-vehicle-stoppingmovementforce:

.. attribute:: stoppingMovementForce
   :noindex:

:Type: float

:Default: ``1.0``

A drag factor applied to the vehicle at all times


.. _scripts-vehicle-storagecapacity:

.. attribute:: storageCapacity
   :noindex:

:Type: integer

:Is useless: True

:Default: ``100``

No description provided.


.. _scripts-vehicle-suspensioncompression:

.. attribute:: suspensionCompression
   :noindex:

:Type: float

:Default: ``4.4``

No description provided.


.. _scripts-vehicle-suspensiondamping:

.. attribute:: suspensionDamping
   :noindex:

:Type: float

:Default: ``2.3``

No description provided.


.. _scripts-vehicle-suspensionrestlength:

.. attribute:: suspensionRestLength
   :noindex:

:Type: float

:Default: ``0.6``

No description provided.


.. _scripts-vehicle-suspensionstiffness:

.. attribute:: suspensionStiffness
   :noindex:

:Type: float

:Default: ``20.0``

No description provided.


.. _scripts-vehicle-template:

.. attribute:: template
   :noindex:

:Type: Unknown

Uses a template script data for this vehicle.


.. _scripts-vehicle-template!:

.. attribute:: template!
   :noindex:

:Type: Unknown

See parameter :ref:`template <scripts-vehicle-template>`.


.. _scripts-vehicle-texturedamage1overlay:

.. attribute:: textureDamage1Overlay
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage1shell:

.. attribute:: textureDamage1Shell
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage2overlay:

.. attribute:: textureDamage2Overlay
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturedamage2shell:

.. attribute:: textureDamage2Shell
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturelights:

.. attribute:: textureLights
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturemask:

.. attribute:: textureMask
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-texturemaskenable:

.. attribute:: textureMaskEnable
   :noindex:

:Type: boolean

:Is useless: True

No description provided.


.. _scripts-vehicle-texturerust:

.. attribute:: textureRust
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-textureshadow:

.. attribute:: textureShadow
   :noindex:

:Type: string

No description provided.


.. _scripts-vehicle-usechassisphysicscollision:

.. attribute:: useChassisPhysicsCollision
   :noindex:

:Type: boolean

:Default: ``True``

By default ``true`` which makes the vehicle use the `physicsChassisShape <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html#vehicle-physicschassisshape>`_ for its hitbox. If set to false, it will instead use the `physics <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/physics.html>`_ blocks as the hitbox of the vehicle.


.. _scripts-vehicle-wheelfriction:

.. attribute:: wheelFriction
   :noindex:

:Type: float

:Default: ``800.0``

It is 1.2 to 1.9 for all vanilla vehicles and controls turning and stopping (but not acceleration) tire friction limits, with 1.4 being the most common. Values over 1.8 can cause vehicles to flip in sharp turns. (Likely depends somewhat on center of mass).


.. _scripts-vehicle-zombietype:

.. attribute:: zombieType
   :noindex:

:Type: array (array of string, separator: ';')

Used to chose what zombie may spawn around the vehicle and is likely to have the key of the vehicle.


