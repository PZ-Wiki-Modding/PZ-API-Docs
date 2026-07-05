.. _scripts-sound:

sound
=====

:Soft Override: Unknown

Makes one or more sound clips available for use in the game. Multiple clips can be added to a sound script, and the game will randomly select one of them to play when the sound is triggered.

.. code-block:: cpp

   module yourModule {
     sound yourSound {
       category = Animal,
       loop = true,
       is3D = true,
       clip {
         file = media/sound/RideOfTheValkyries.ogg,
         distanceMin = 20,
         distanceMax = 650,
         reverbFactor = 0.1,
         volume = 0.7,
       }
     }
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`
- :ref:`vehicle <scripts-vehicle>`
- :ref:`template <scripts-template>`

This block can have the following child blocks:

- :ref:`clip <scripts-clip>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False
:No ID for parents: 
* ``:ref:`vehicle <scripts-vehicle>```
* ``:ref:`template <scripts-template>```


Parameters
----------

.. _scripts-sound-alarm:

alarm
^^^^^

:Type: array (array of string, separator: ' ')

No description provided.


.. _scripts-sound-alarmloop:

alarmLoop
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-sound-backsignal:

backSignal
^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-sound-category:

category
^^^^^^^^

:Type: string

Unclear what this parameter is for.


.. _scripts-sound-engine:

engine
^^^^^^

:Type: string

No description provided.


.. _scripts-sound-enginestart:

engineStart
^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-sound-engineturnoff:

engineTurnOff
^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-sound-handbrake:

handBrake
^^^^^^^^^

:Type: string

No description provided.


.. _scripts-sound-horn:

horn
^^^^

:Type: string

No description provided.


.. _scripts-sound-ignitionfail:

ignitionFail
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-sound-ignitionfailnopower:

ignitionFailNoPower
^^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-sound-is3d:

is3D
^^^^

:Type: boolean

Whenever this is set to ``false``\ , the distance to the sound will not impact its volume. This parameter doesn't impact the sound directionality.


.. _scripts-sound-loop:

loop
^^^^

:Type: boolean

Whether the sound should loop or not. The sound plays until turned off manually via Lua code or the emitter is destroyed.


.. _scripts-sound-master:

master
^^^^^^

:Type: string
:Default: ``Primary``
:Allowed values: 
* ``Primary``
* ``Ambient``
* ``Music``
* ``VehicleEngine``

Links the sound to a sound handling setting, which controls the volume of all sounds linked to it. This doesn't seems to be working properly, as some methods that call sounds will simply not take into account the current sound settings. You can find a relevant request about this issue on the #mod_portal channel of the official Discord `here <https://discord.com/channels/136501320340209664/1476602902607954043/1505634480939860119>`_.


.. _scripts-sound-maxinstancesperemitter:

maxInstancesPerEmitter
^^^^^^^^^^^^^^^^^^^^^^

:Type: integer

Specifies how many of this sound the sound emitter can play at the same time.


