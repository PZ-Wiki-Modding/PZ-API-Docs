.. _sound:

sound
=====

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

**Valid Parent Blocks:**

- :ref:`module`
- :ref:`vehicle`
- :ref:`template`

**Possible Child Blocks:**

- :ref:`clip`


ID Properties
-------------

This block should have an ID.

**Incompatible Parents:**

- vehicle
- template


Parameters
----------

.. _sound-alarm:

alarm
^^^^^

:Type: array (array of string, separator: ' ')
:Needs: ``unknown``

No description

.. _sound-alarmloop:

alarmLoop
^^^^^^^^^

:Type: Any
:Needs: ``unknown``

No description

.. _sound-backsignal:

backSignal
^^^^^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-category:

category
^^^^^^^^

:Type: string

Unclear what this parameter is for.

.. _sound-engine:

engine
^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-enginestart:

engineStart
^^^^^^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-engineturnoff:

engineTurnOff
^^^^^^^^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-handbrake:

handBrake
^^^^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-horn:

horn
^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-ignitionfail:

ignitionFail
^^^^^^^^^^^^

:Type: Any
:Needs: ``unknown``

No description

.. _sound-ignitionfailnopower:

ignitionFailNoPower
^^^^^^^^^^^^^^^^^^^

:Type: string
:Needs: ``unknown``

No description

.. _sound-is3d:

is3D
^^^^

:Type: boolean

Whenever this is set to ``false``\ , the distance to the sound will not impact its volume. This parameter doesn't impact the sound directionality.

.. _sound-loop:

loop
^^^^

:Type: boolean

Whether the sound should loop or not. The sound plays until turned off manually via Lua code or the emitter is destroyed.

.. _sound-master:

master
^^^^^^

:Type: string
:Default: ``Primary``

Links the sound to a sound handling setting, which controls the volume of all sounds linked to it. This doesn't seems to be working properly, as some methods that call sounds will simply not take into account the current sound settings. You can find a relevant request about this issue on the #mod_portal channel of the official Discord `here <https://discord.com/channels/136501320340209664/1476602902607954043/1505634480939860119>`_.

Allowed values:

    - ``Primary``
    - ``Ambient``
    - ``Music``
    - ``VehicleEngine``

.. _sound-maxinstancesperemitter:

maxInstancesPerEmitter
^^^^^^^^^^^^^^^^^^^^^^

:Type: integer

Specifies how many of this sound the sound emitter can play at the same time.

