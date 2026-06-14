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

- :ref:`<m_Name> <animNode.type_AnimNode.m_Name>` (required): ``xs:string``
- :ref:`<m_AnimName> <animNode.type_AnimNode.m_AnimName>` (required): ``xs:string``
- :ref:`<m_BlendTime> <animNode.type_AnimNode.m_BlendTime>` (optional): ``xs:float``
- :ref:`<m_blendOutTime> <animNode.type_AnimNode.m_blendOutTime>` (optional): ``xs:float``
- :ref:`<m_SpeedScale> <animNode.type_AnimNode.m_SpeedScale>` (optional): ``xs:float`` | ``xs:string``
- :ref:`<m_Priority> <animNode.type_AnimNode.m_Priority>` (optional): ``xs:integer``
- :ref:`<m_maxTorsoTwist> <animNode.type_AnimNode.m_maxTorsoTwist>` (optional): ``xs:float``
- :ref:`<m_Scalar> <animNode.type_AnimNode.m_Scalar>` (optional): ``xs:float`` | ``xs:string``
- :ref:`<m_SyncTrackingEnabled> <animNode.type_AnimNode.m_SyncTrackingEnabled>` (optional): ``xs:boolean``
- :ref:`<m_2DBlends> <animNode.type_AnimNode.m_2DBlends>` (optional): :ref:`type_2DBlends <animNode.type_2DBlends>`
- :ref:`<m_2DBlendTri> <animNode.type_AnimNode.m_2DBlendTri>` (optional): :ref:`type_2DBlendTri <animNode.type_2DBlendTri>`
- :ref:`<m_Conditions> <animNode.type_AnimNode.m_Conditions>` (optional): :ref:`type_Condition <animNode.type_Condition>`
- :ref:`<m_Events> <animNode.type_AnimNode.m_Events>` (optional): :ref:`type_Events <animNode.type_Events>`
- :ref:`<m_Transitions> <animNode.type_AnimNode.m_Transitions>` (optional): :ref:`type_Transitions <animNode.type_Transitions>`
- :ref:`<m_SubStateBoneWeights> <animNode.type_AnimNode.m_SubStateBoneWeights>` (optional): :ref:`type_SubStateBoneWeights <animNode.type_SubStateBoneWeights>`

**Attributes:**

- :ref:`x_extends <animNode.type_AnimNode.x_extends>`: ``xs:string`` (optional)

Root Type Details
-----------------

.. _animNode.type_AnimNode:

type_AnimNode
~~~~~~~~~~~~~

:Type: Complex
:Composition: choice

Elements
^^^^^^^^

.. _animNode.type_AnimNode.m_Name:

m_Name
^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

A unique identifier for this animation node. For example: "LoadRiffle", "Walk" etc. This is notably used to reference this animNode in other animNodes.

.. _animNode.type_AnimNode.m_AnimName:

m_AnimName
^^^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

Name of the animation clip to play. This is the name of the animation file without the extension. The animation clip needs to be stored inside the ``anims_X`` folder and inside a subfolder which matches the character the animation is for. For the player, that subfolder needs to be ``Bob``.

For example, take the animation file ``Bob_Reload_Rifle_Load.glb`` with the following folder structure:

.. code-block::

   anims_X/
     Bob/
       Bob_Reload_Rifle_Load.glb

To reference it in the animNode, you would use:

.. code-block:: xml

   <m_AnimName>Bob_Reload_Rifle_Load</m_AnimName>

.. _animNode.type_AnimNode.m_BlendTime:

m_BlendTime
^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

Defines how quickly the animation will begin to play, and how the game interpolates moving the armature's bones from one animNode to another.

.. _animNode.type_AnimNode.m_blendOutTime:

m_blendOutTime
^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

Defines how quickly the animation will end, and how the game interpolates moving the armature's bones from one animState to another. It is used to create a smooth transition when the animation is stopped or changed.

.. _animNode.type_AnimNode.m_SpeedScale:

m_SpeedScale
^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float`` | ``xs:string``

.. _animNode.type_AnimNode.m_Priority:

m_Priority
^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:integer``

In cases of two animations that are playing at the same time, dictates which animation's bone weights or keyframes will take precedence. An example would be an idle animMask holding a glass which transitions into a drinking animation. The drinking animation takes priority over the idle drink-holding ainmMask if its priority is higher than the idle animation mask's XML. The priority value is an integer starting at 1 with high numbers taking the priority.

.. _animNode.type_AnimNode.m_maxTorsoTwist:

m_maxTorsoTwist
^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

.. _animNode.type_AnimNode.m_Scalar:

m_Scalar
^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float`` | ``xs:string``

.. _animNode.type_AnimNode.m_SyncTrackingEnabled:

m_SyncTrackingEnabled
^^^^^^^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _animNode.type_AnimNode.m_2DBlends:

m_2DBlends
^^^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_2DBlends <animNode.type_2DBlends>`

.. _animNode.type_AnimNode.m_2DBlendTri:

m_2DBlendTri
^^^^^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_2DBlendTri <animNode.type_2DBlendTri>`

.. _animNode.type_AnimNode.m_Conditions:

m_Conditions
^^^^^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_Condition <animNode.type_Condition>`

.. _animNode.type_AnimNode.m_Events:

m_Events
^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_Events <animNode.type_Events>`

Used to trigger different events during the animation at specific moments. This can be used to play sounds, set variables, and more.

.. _animNode.type_AnimNode.m_Transitions:

m_Transitions
^^^^^^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_Transitions <animNode.type_Transitions>`

.. _animNode.type_AnimNode.m_SubStateBoneWeights:

m_SubStateBoneWeights
^^^^^^^^^^^^^^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_SubStateBoneWeights <animNode.type_SubStateBoneWeights>`

Attributes
^^^^^^^^^^

.. _animNode.type_AnimNode.x_extends:

x_extends
^^^^^^^^^

:Type: ``xs:string``
:Use: Optional

Import another relative animNode file into this one. Needs to be the file name so for the following example folder structure: 

.. code-block::

   AnimSets/
       Rifle/
           LoadRifle.xml
           LoadRifle_Alt.xml

The LoadRifle_Alt.xml file can import the LoadRifle.xml file by using:

.. code-block:: xml

   <animNode x_extends="LoadRifle.xml"></animNode>


Schema Reference
----------------

.. _animNode.enum_Type:

enum_Type
~~~~~~~~~

:Type: Simple
:Base Type: ``xs:string``

Allowed Values
^^^^^^^^^^^^^^

- ``STRING``
- ``BOOL``
- ``INT``
- ``FLOAT``

.. _animNode.type_2DBlendTri:

type_2DBlendTri
~~~~~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_2DBlendTri.node1:

node1
^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:integer``

.. _animNode.type_2DBlendTri.node2:

node2
^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:integer``

.. _animNode.type_2DBlendTri.node3:

node3
^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:integer``

.. _animNode.type_2DBlends:

type_2DBlends
~~~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_2DBlends.m_AnimName:

m_AnimName
^^^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

.. _animNode.type_2DBlends.m_XPos:

m_XPos
^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

.. _animNode.type_2DBlends.m_YPos:

m_YPos
^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

.. _animNode.type_2DBlends.m_SpeedScale:

m_SpeedScale
^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

Attributes
^^^^^^^^^^

.. _animNode.type_2DBlends.referenceID:

referenceID
^^^^^^^^^^^

:Type: ``xs:integer``
:Use: Optional

.. _animNode.type_Condition:

type_Condition
~~~~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_Condition.m_Name:

m_Name
^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

.. _animNode.type_Condition.m_Type:

m_Type
^^^^^^

:Occurrence: Optional (0 or 1)
:Type: :ref:`enum_Type <animNode.enum_Type>`

.. _animNode.type_Condition.m_Condition:

m_Condition
^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

.. _animNode.type_Condition.m_Value:

m_Value
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

Attributes
^^^^^^^^^^

.. _animNode.type_Condition.x_name:

x_name
^^^^^^

:Type: ``xs:string``
:Use: Optional

This is unused by the game but it seems to be a simple identifier (often a `GUID <https://pzwiki.net/wiki/GUID>`_\ ) used by the unreleased `AnimZed <https://pzwiki.net/wiki/AnimZed>`_.

.. _animNode.type_Events:

type_Events
~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_Events.m_EventName:

m_EventName
^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

The name of the event to trigger. This can be a custom name but there's also available events that will trigger specific actions. You can find a list of available events `here <https://pzwiki.net/wiki/Events#Available_events>`_.

.. _animNode.type_Events.m_Time:

m_Time
^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

The moment during the animation when the event will be triggered. This can be set to Start or End.

.. _animNode.type_Events.m_TimePc:

m_TimePc
^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

The moment during the animation when the event will be triggered. This uses a normalized time, so ``0`` is the start and ``1`` is the end. In comparison to ``m_Time``\ , this allows for more precision of when to trigger the event.

.. _animNode.type_Events.m_ParameterValue:

m_ParameterValue
^^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

The value to pass to the event when it is triggered. This can be used to specify which sound to play, which variable to set, and more, depending on the event being triggered.

Attributes
^^^^^^^^^^

.. _animNode.type_Events.x_name:

x_name
^^^^^^

:Type: ``xs:string``
:Use: Optional

.. _animNode.type_SubStateBoneWeights:

type_SubStateBoneWeights
~~~~~~~~~~~~~~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_SubStateBoneWeights.boneName:

boneName
^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

.. _animNode.type_SubStateBoneWeights.includeDescendants:

includeDescendants
^^^^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _animNode.type_Transitions:

type_Transitions
~~~~~~~~~~~~~~~~

:Type: Complex

Elements
^^^^^^^^

.. _animNode.type_Transitions.m_Target:

m_Target
^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

The name of the target animNode to transition to. This is the value of the ``m_Name`` field in the target animNode.

.. _animNode.type_Transitions.m_AnimName:

m_AnimName
^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:string``

.. _animNode.type_Transitions.m_blendInTime:

m_blendInTime
^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

.. _animNode.type_Transitions.m_blendOutTime:

m_blendOutTime
^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

.. _animNode.type_Transitions.m_speedScale:

m_speedScale
^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:float``

