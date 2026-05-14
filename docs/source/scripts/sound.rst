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

:Type: array
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

No description

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
:Attributes: Useless

This parameter looks unused.

.. _sound-loop:

loop
^^^^

:Type: boolean

Whether the sound should loop or not. The sound plays until turned off or the emitter is destroyed.

.. _sound-master:

master
^^^^^^

:Type: string

Links the sound to a master sound category, which controls the volume of all sounds linked to it.

Allowed values:

    - ``Primary``
    - ``Ambient``
    - ``Music``
    - ``VehicleEngine``

.. _sound-maxinstancesperemitter:

maxInstancesPerEmitter
^^^^^^^^^^^^^^^^^^^^^^

:Type: integer

No description

