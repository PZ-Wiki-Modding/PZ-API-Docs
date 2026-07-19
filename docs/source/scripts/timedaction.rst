.. _scripts-timedaction:

timedAction
===========

.. attribute:: Soft Override

   Unknown

The timedAction script block is used to define an action which can be used in `craftRecipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_. You can specify the animation played, props in hands during the action, the sound played. Also define its impact on the player character, including effects on calories burned and body heat generation.

Below are a few examples of ``timedAction`` blocks from the vanilla game:

.. code-block:: cpp

   timedAction UseLathe
   {
       metabolics      = Default,
       actionAnim      = UseLathe,
   }

.. code-block:: cpp

   timedAction BuildCairn
   {
       metabolics      = HeavyWork,
       actionAnim      = Loot,
       animVarKey      = LootPosition,
       animVarVal      = Low,
       sound           = BuildingGeneric,
       completionSound = BuildFenceCairn,
       muscleStrainFactor = 0.0025,
       muscleStrainSkill = Strength,
       muscleStrainParts = Neck,
   }

.. code-block:: cpp

   timedAction BuildBarbedWireFence
   {
       metabolics      = HeavyWork,
       actionAnim      = Loot,
       animVarKey      = LootPosition,
       animVarVal      = Low,
       sound           = BuildingGeneric,
       completionSound = BuildMetalStructureSmallWiredFence,
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

.. attribute:: Optional

   False

.. attribute:: Can have spaces

   False


Parameters
----------

.. _scripts-timedaction-actionanim:

actionAnim
^^^^^^^^^^

.. attribute:: Type

   string

The actionAnim parameter is used to define the animation played during a timed action. It links to a `PerformingAction <https://pzwiki.net/wiki/PerformingAction>`_ define in the action `AnimSets <https://pzwiki.net/wiki/AnimSet>`_ of the player.


.. _scripts-timedaction-animvarkey:

animVarKey
^^^^^^^^^^

.. attribute:: Type

   Unknown

The `animVarKey <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#animVarKey>`_ and `animVarVal <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#animVarVal>`_ parameters are used together to link to a specific `AnimNode Conditions <https://pzwiki.net/wiki/Conditions>`_. ``animVarKey`` will correspond to the ``m_Name`` field and ``animVarVal`` to the ``m_Value`` field.

This allows for easy swapping between variants of `actionAnim <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#actionAnim>`_. For example, for the AnimNode:

.. code-block:: cpp

   <?xml version="1.0" encoding="utf-8"?>
   <animNode x_extends="Loot.xml">
     <m_Name>LootHigh</m_Name>
     <m_AnimName>Bob_IdleLooting_High</m_AnimName>
     <m_Conditions />
     <m_Conditions />
     <m_Conditions>
       <m_Name>LootPosition</m_Name>
       <m_Type>STRING</m_Type>
       <m_StringValue>High</m_StringValue>
     </m_Conditions>
   </animNode>

You can define those parameters in the timedAction as follows:

.. code-block:: cpp

   actionAnim      = Loot,
   animVarKey      = LootPosition,
   animVarVal      = Low,


.. _scripts-timedaction-animvarval:

animVarVal
^^^^^^^^^^

.. attribute:: Type

   Unknown

See parameter :ref:`animVarKey <scripts-timedaction-animvarkey>`.


.. _scripts-timedaction-completionsound:

completionSound
^^^^^^^^^^^^^^^

.. attribute:: Type

   block (block: :ref:`sound <scripts-sound>`)

Defines the sound played at the end of the action.


.. _scripts-timedaction-metabolics:

metabolics
^^^^^^^^^^

.. attribute:: Type

   Unknown

The metabolics parameter is used to define the impact of the action on the player character's metabolics, such as the calories burn rate or body heat generation. It uses predefined enumeration values to specify the multiplier on the metabolism. You can find a list of metabolic types and their associated values in the `Metabolics <https://pz-wiki-modding.github.io/PZ-API-Docs/java/metabolics.html>`_ documentation.


.. _scripts-timedaction-musclestrainfactor:

muscleStrainFactor
^^^^^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

Muscle strain is an effect which applies to the character limbs, simulating the fatigue and strain of performing certain actions. A timedAction script can be set to apply muscle strain to specific limbs and based on the level of the character in a specific skill.

`muscleStrainFactor <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#muscleStrainFactor>`_ serves as a parameter of how much muscle strain will be gained.

`muscleStrainParts <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#muscleStrainParts>`_ will indicate the limbs affected by the muscle strain, which needs to be an array of `BodyPartType <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/BodyDamage/BodyPartType.html#enum-constant-summary>`_.

If `muscleStrainSkill <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/timedaction.html#muscleStrainSkill>`_ is provided, the skill will be used to reduce the muscle strain when the player gets better at something.

.. code-block::

   strain = deltaTime * muscleStrainFactor * (1 - skillLevel * 0.5)


.. _scripts-timedaction-musclestrainparts:

muscleStrainParts
^^^^^^^^^^^^^^^^^

.. attribute:: Type

   array (array of string, separator: ';')

See parameter :ref:`muscleStrainFactor <scripts-timedaction-musclestrainfactor>`.


.. _scripts-timedaction-musclestrainskill:

muscleStrainSkill
^^^^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

See parameter :ref:`muscleStrainFactor <scripts-timedaction-musclestrainfactor>`.


.. _scripts-timedaction-prop1:

prop1
^^^^^

.. attribute:: Type

   block (block: :ref:`model <scripts-model>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-timedaction-prop2:

prop2
^^^^^

.. attribute:: Type

   block (block: :ref:`model <scripts-model>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-timedaction-sound:

sound
^^^^^

.. attribute:: Type

   block (block: :ref:`sound <scripts-sound>`)

Defines the sound played during the action.


.. _scripts-timedaction-soundtime:

soundTime
^^^^^^^^^

.. attribute:: Type

   string

.. attribute:: Is useless

   True

.. attribute:: Default

   ``action_start``

This parameter is used in the Lua to indicate when the sound should be played during the timed action. This is notably used to play a sound at the end or the start of the action during `crafting <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftRecipe.html#timedAction>`_.

By itself, this doesn't do anything and requires implementation in `Lua <https://pzwiki.net/wiki/Lua_(API>`_\ ). For example inside ``ISHandcraftAction``.

For a full list of the accepted events, see `this <https://pz-wiki-modding.github.io/PZ-API-Docs/java/action_sound_time.html>`_.


