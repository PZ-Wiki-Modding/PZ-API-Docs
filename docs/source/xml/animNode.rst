animNode
========

The AnimNode files are used to link animation files to the game by defining different parameters for the animation. This will notably control the speed of the animation, its blending with animations played before and after, events that need to be triggered and conditions that control when that animation can be played.

File Patterns
-------------

- ``**/AnimSets/**/*.xml``

Root Element
------------

:Element: ``<animNode>``
:Type: ``type_AnimNode``

Structure
---------

The root element uses a **choice** composition, meaning it can contain any combination of the following elements:

- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````
- :ref:`<> <animNode.type_AnimNode.>` (optional): ````

**Attributes:**

- :ref:` <animNode.type_AnimNode.>`: ```` (optional)

Root Type Details
-----------------

.. _animNode.type_AnimNode:

type_AnimNode
-------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

A unique identifier for this animation node. For example: "LoadRiffle", "Walk" etc. This is notably used to reference this animNode in other animNodes.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Name of the animation clip to play. This is the name of the animation file without the extension. The animation clip needs to be stored inside the ``anims_X`` folder and inside a subfolder which matches the character the animation is for. For the player, that subfolder needs to be ``Bob``.

For example, take the animation file ``Bob_Reload_Rifle_Load.glb`` with the following folder structure:

.. code-block::

   📁 media
     📁 anims_X
       📁 Bob
         📄 Bob_Reload_Rifle_Load.glb

To reference it in the animNode, you would use:

.. code-block:: xml

   <m_AnimName>Bob_Reload_Rifle_Load</m_AnimName>

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Defines how quickly the animation will begin to play, and how the game interpolates moving the armature's bones from one animNode to another.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Defines how quickly the animation will end, and how the game interpolates moving the armature's bones from one animState to another. It is used to create a smooth transition when the animation is stopped or changed.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Defines whether the animation will loop or not. If set to true, the animation will loop indefinitely until it is manually stopped or `conditions <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/animNode.html#m-conditions>`_ are no longer met.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

In cases of two animations that are playing at the same time, dictates which animation's bone weights or keyframes will take precedence. An example would be an idle animMask holding a glass which transitions into a drinking animation. The drinking animation takes priority over the idle drink-holding ainmMask if its priority is higher than the idle animation mask's XML. The priority value is an integer starting at 1 with high numbers taking the priority.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Used to specify conditions that will allow an animation node to be chosen. If the conditions are not met, the node will not be chosen. These are often combined with the function `setVariable <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html#setVariable(java.lang.String,java.lang.String>`_\ ) (which exists in many forms) to set a specific condition.

This can notably be used to trigger an animation by setting that condition to be valid, which will make the animation node eligible to be chosen by the game, as long as other conditions are also met.

The syntax is as follows for the most common cases:

.. code-block:: xml

   <m_Conditions>
     <m_Name>VariableName</m_Name>
     <m_Type>STRING</m_Type>
     <m_Value>value</m_Value>
   </m_Conditions>

In the following example, the variable ``WeaponReloadType`` is set by the game, using the parameter of the same name in the `item script <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weaponreloadtype>`_\ :

.. code-block:: xml

   <m_Conditions>
       <m_Name>WeaponReloadType</m_Name>
       <m_Type>STRING</m_Type>
       <m_Value>revolver</m_Value>
   </m_Conditions>

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Used to trigger different events during the animation at specific moments. This can be used to play sounds, set variables, and more. You can find a list of available events `here <https://pzwiki.net/wiki/Events#Available_events>`_.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Used to define the weight of a bone and its keyframes or descendants. By default, all bones that are not defined with this parameter have a default weight of ``1``. If you wanted to make it so an animation were to only play a specific set of bones; you would define the Dummy01 or the Bip01 bones (the parent armature bones) to have a weight of 0, and then specifically define all the bones you wish to play to have a weight value greater than 0.

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Attributes
~~~~~~~~~~

.. _animNode.type_AnimNode.unknown:

unknown
^^^^^^^

:Type: ``unknown``
:Use: Optional

Import another relative animNode file into this one. Needs to be the file name so for the following example folder structure: 

.. code-block::

   📁 media
     📁 AnimSets
       📁 Rifle
         📄 LoadRifle.xml
         📄 LoadRifle_Alt.xml

The LoadRifle_Alt.xml file can import the LoadRifle.xml file by using:

.. code-block:: xml

   <animNode x_extends="LoadRifle.xml"></animNode>


Types
-----

.. _animNode.enum_Type:

enum_Type
---------

:Type: Simple
.. _animNode.type_2DBlendTri:

type_2DBlendTri
---------------

:Type: Complex

Elements
~~~~~~~~

.. _animNode.type_2DBlendTri.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlendTri.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlendTri.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlends:

type_2DBlends
-------------

:Type: Complex

Elements
~~~~~~~~

.. _animNode.type_2DBlends.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlends.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlends.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_2DBlends.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Attributes
~~~~~~~~~~

.. _animNode.type_2DBlends.unknown:

unknown
^^^^^^^

:Type: ``unknown``
:Use: Optional

.. _animNode.type_Condition:

type_Condition
--------------

:Type: Complex

Elements
~~~~~~~~

.. _animNode.type_Condition.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Condition.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Condition.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Condition.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Attributes
~~~~~~~~~~

.. _animNode.type_Condition.unknown:

unknown
^^^^^^^

:Type: ``unknown``
:Use: Optional

This is unused by the game but it seems to be a simple identifier (often a `GUID <https://pzwiki.net/wiki/GUID>`_\ ) used by the unreleased `AnimZed <https://pzwiki.net/wiki/AnimZed>`_.

.. _animNode.type_Events:

type_Events
-----------

:Type: Complex

Elements
~~~~~~~~

.. _animNode.type_Events.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The name of the event to trigger. This can be a custom name but there's also available events that will trigger specific actions. You can find a list of available events `here <https://pzwiki.net/wiki/Events#Available_events>`_.

.. _animNode.type_Events.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The moment during the animation when the event will be triggered. This can be set to Start or End.

.. _animNode.type_Events.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The moment during the animation when the event will be triggered. This uses a normalized time, so ``0`` is the start and ``1`` is the end. In comparison to ``m_Time``\ , this allows for more precision of when to trigger the event.

.. _animNode.type_Events.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The value to pass to the event when it is triggered. This can be used to specify which sound to play, which variable to set, and more, depending on the event being triggered.

Attributes
~~~~~~~~~~

.. _animNode.type_Events.unknown:

unknown
^^^^^^^

:Type: ``unknown``
:Use: Optional

This is unused by the game but it seems to be a simple identifier (often a `GUID <https://pzwiki.net/wiki/GUID>`_\ ) used by the unreleased `AnimZed <https://pzwiki.net/wiki/AnimZed>`_.

.. _animNode.type_SubStateBoneWeights:

type_SubStateBoneWeights
------------------------

:Type: Complex

Elements
~~~~~~~~

.. _animNode.type_SubStateBoneWeights.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_SubStateBoneWeights.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_SubStateBoneWeights.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Transitions:

type_Transitions
----------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The name of the target animNode to transition to. This is the value of the ``m_Name`` field in the target animNode.

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _animNode.type_Transitions.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

