.. _scripts-clip:

clip
====

.. attribute:: Soft Override

   Unknown

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

This block can be a child of the following blocks:

- :ref:`sound <scripts-sound>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-clip-event:

event
^^^^^

.. attribute:: Type

   string

Specifies an event that will trigger the playback of a specific sound. Used for sounds from FMOD sound banks (vanilla sound files).


.. _scripts-clip-distancemax:

distanceMax
^^^^^^^^^^^

.. attribute:: Type

   integer

`distanceMax <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/clip.html#distanceMax>`_ and `distanceMin <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/clip.html#distanceMin>`_ respectively set the maximum and minimum distances between which the sound will gradually decrease in volume.


.. _scripts-clip-file:

file
^^^^

.. attribute:: Type

   string

The path to the sound file to be played, relative to the folder above the ``media`` folder. For the following file path:

.. code-block::

   📁 MyMod
     📁 media
       📁 sound
         📄 my_sound.ogg

This parameter will be:

.. code-block:: cpp

   file = media/sound/my_sound.ogg

A file can be both of file format ``.ogg`` or ``.wav``\ , but ``.ogg`` is recommended for its smaller file size and better compression.


.. _scripts-clip-distancemin:

distanceMin
^^^^^^^^^^^

.. attribute:: Type

   integer

See parameter :ref:`distanceMax <scripts-clip-distancemax>`.


.. _scripts-clip-volume:

volume
^^^^^^

.. attribute:: Type

   float

Adjusts the volume of the sound. Preferably your sound file should be properly normalized to a volume of 1.0.


.. _scripts-clip-reverbfactor:

reverbFactor
^^^^^^^^^^^^

.. attribute:: Type

   float

`reverbFactor <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/clip.html#reverbFactor>`_ sets the amount of reverb applied to the sound while `reverbMaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/clip.html#reverbMaxRange>`_ sets the maximum distance at which the reverb will be applied.


.. _scripts-clip-pitch:

pitch
^^^^^

.. attribute:: Type

   float

The pitch of the sound.


.. _scripts-clip-reverbmaxrange:

reverbMaxRange
^^^^^^^^^^^^^^

.. attribute:: Type

   float

See parameter :ref:`reverbFactor <scripts-clip-reverbfactor>`.


.. _scripts-clip-stopimmediate:

stopImmediate
^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


