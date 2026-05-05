.. _clip:

clip
====

Defines a clip to be used in a `sound script <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_\ , which is a single sound file with properties that determine how it is played in the game.

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

- :ref:`sound`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _clip-distancemax:

distanceMax
^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

.. _clip-distancemin:

distanceMin
^^^^^^^^^^^

   Type: ``{'main': 'integer'}``

No description

.. _clip-event:

event
^^^^^

   Type: ``{'main': 'string'}``

No description

.. _clip-file:

file
^^^^

   Type: ``{'main': 'string'}``

No description

.. _clip-pitch:

pitch
^^^^^

   Type: ``{'main': 'float'}``

No description

.. _clip-reverbfactor:

reverbFactor
^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

.. _clip-reverbmaxrange:

reverbMaxRange
^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

.. _clip-stopimmediate:

stopImmediate
^^^^^^^^^^^^^

   Type: ``Any``

No description

.. _clip-volume:

volume
^^^^^^

   Type: ``{'main': 'float'}``

No description

