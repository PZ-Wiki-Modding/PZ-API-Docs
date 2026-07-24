.. _xml-animnode:

animNode
========

The AnimNode files are used to link animation files to the game by defining different parameters for the animation. This will notably control the speed of the animation, its blending with animations played before and after, events that need to be triggered and conditions that control when that animation can be played.


File Patterns
-------------

The following file patterns are used to determine what the valid path for the XML file can be, relative to the `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ folder.

- ``**/AnimSets/**/*.xml``


.. _animnode-type_animnode:

Root Details
------------

.. attribute:: Element

   animNode

The root element is the top-level XML element that contains all other elements in the XML file.

.. attribute:: Type

   :ref:`type_AnimNode <animnode-type_animnode>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

m_Name
""""""

.. attribute:: Minimum occurence

   1

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

A unique identifier for this animation node. For example: "LoadRiffle", "Walk" etc. This is notably used to reference this animNode in other animNodes.

m_AnimName
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

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

m_BlendTime
"""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

Defines how quickly the animation will begin to play, and how the game interpolates moving the armature's bones from one animNode to another.

m_BlendOutTime
""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

Defines how quickly the animation will end, and how the game interpolates moving the armature's bones from one animState to another. It is used to create a smooth transition when the animation is stopped or changed.

m_SpeedScale
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``, ``xs:string``

No description provided.

m_SpeedScaleRandomMultiplierMin
"""""""""""""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_SpeedScaleRandomMultiplierMax
"""""""""""""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_TrackTimeToVariable
"""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_Finished
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

Looks unused.

m_Looped
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

Defines whether the animation will loop or not. If set to true, the animation will loop indefinitely until it is manually stopped or `conditions <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/animNode.html#m-conditions>`_ are no longer met.

m_AnimReverse
"""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_Priority
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:integer``

In cases of two animations that are playing at the same time, dictates which animation's bone weights or keyframes will take precedence. An example would be an idle animMask holding a glass which transitions into a drinking animation. The drinking animation takes priority over the idle drink-holding ainmMask if its priority is higher than the idle animation mask's XML. The priority value is an integer starting at 1 with high numbers taking the priority.

m_ConditionPriority
"""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:integer``

No description provided.

m_maxTorsoTwist
"""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_Scalar
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``, ``xs:string``

No description provided.

m_Scalar2
"""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``, ``xs:string``

No description provided.

m_SyncTrackingEnabled
"""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_2DBlends
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_2DBlends <animnode-type_2dblends>`

No description provided.

m_2DBlendTri
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_2DBlendTri <animnode-type_2dblendtri>`

No description provided.

m_Conditions
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_Condition <animnode-type_condition>`

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

m_Events
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_Events <animnode-type_events>`

Used to trigger different events during the animation at specific moments. This can be used to play sounds, set variables, and more. You can find a list of available events `here <https://pzwiki.net/wiki/Events#Available_events>`_.

m_Transitions
"""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_Transitions <animnode-type_transitions>`

No description provided.

m_EarlyTransitionOut
""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_StopAnimOnExit
""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_SubStateBoneWeights
"""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_SubStateBoneWeights <animnode-type_substateboneweights>`

Used to define the weight of a bone and its keyframes or descendants. By default, all bones that are not defined with this parameter have a default weight of ``1``. If you wanted to make it so an animation were to only play a specific set of bones; you would define the Dummy01 or the Bip01 bones (the parent armature bones) to have a weight of 0, and then specifically define all the bones you wish to play to have a weight value greater than 0.

m_DeferredBoneName
""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_deferredBoneAxis
""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_useDeferedRotation
""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_MatchingGrappledAnimNode
""""""""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_GrappleOffsetForward
""""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_GrappleOffsetYaw
""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:integer``

No description provided.

m_GrapplerOffsetBehaviour
"""""""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_GrappleTweenInTime
""""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

Attributes
^^^^^^^^^^

x_extends
"""""""""

.. attribute:: Type

   ``xs:string``

.. attribute:: Use

   optional

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


.. _animnode-type_2dblends:

type_2DBlends
-------------

.. attribute:: Type

   :ref:`type_2DBlends <animnode-type_2dblends>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

m_AnimName
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

No description provided.

m_XPos
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``

No description provided.

m_YPos
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``

No description provided.

m_SpeedScale
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``

No description provided.

Attributes
^^^^^^^^^^

referenceID
"""""""""""

.. attribute:: Type

   ``xs:integer``

.. attribute:: Use

   optional

No description provided.


.. _animnode-type_2dblendtri:

type_2DBlendTri
---------------

.. attribute:: Type

   :ref:`type_2DBlendTri <animnode-type_2dblendtri>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

node1
"""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:integer``

No description provided.

node2
"""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:integer``

No description provided.

node3
"""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:integer``

No description provided.


.. _animnode-type_condition:

type_Condition
--------------

.. attribute:: Type

   :ref:`type_Condition <animnode-type_condition>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

m_Name
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

No description provided.

m_Type
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`rule_Type <animnode-rule_type>`

No description provided.

m_Condition
"""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

No description provided.

m_Value
"""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

No description provided.

m_IntValue
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:integer``

No description provided.

m_FloatValue
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:float``

No description provided.

m_BoolValue
"""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:boolean``

No description provided.

m_StringValue
"""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

No description provided.

Attributes
^^^^^^^^^^

x_name
""""""

.. attribute:: Type

   ``xs:string``

.. attribute:: Use

   optional

This is unused by the game but it seems to be a simple identifier (often a `GUID <https://pzwiki.net/wiki/GUID>`_\ ) used by the unreleased `AnimZed <https://pzwiki.net/wiki/AnimZed>`_.


.. _animnode-type_events:

type_Events
-----------

.. attribute:: Type

   :ref:`type_Events <animnode-type_events>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

m_EventName
"""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

The name of the event to trigger. This can be a custom name but there's also available events that will trigger specific actions. You can find a list of available events `here <https://pzwiki.net/wiki/Events#Available_events>`_.

m_Time
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   :ref:`rule_Time <animnode-rule_time>`

The moment during the animation when the event will be triggered. This can be set to Start or End.

m_TimePc
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   :ref:`rule_TimePc <animnode-rule_timepc>`

The moment during the animation when the event will be triggered. This uses a normalized time, so ``0`` is the start and ``1`` is the end. In comparison to ``m_Time``\ , this allows for more precision of when to trigger the event.

m_ParameterValue
""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

The value to pass to the event when it is triggered. This can be used to specify which sound to play, which variable to set, and more, depending on the event being triggered.

Attributes
^^^^^^^^^^

x_name
""""""

.. attribute:: Type

   ``xs:string``

.. attribute:: Use

   optional

This is unused by the game but it seems to be a simple identifier (often a `GUID <https://pzwiki.net/wiki/GUID>`_\ ) used by the unreleased `AnimZed <https://pzwiki.net/wiki/AnimZed>`_.


.. _animnode-type_transitions:

type_Transitions
----------------

.. attribute:: Type

   :ref:`type_Transitions <animnode-type_transitions>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

m_Target
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   ``xs:string``

The name of the target animNode to transition to. This is the value of the ``m_Name`` field in the target animNode.

m_AnimName
""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

m_blendInTime
"""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_blendOutTime
""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_speedScale
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.

m_Conditions
""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   unbounded

.. attribute:: Type

   :ref:`type_Condition <animnode-type_condition>`

No description provided.


.. _animnode-type_substateboneweights:

type_SubStateBoneWeights
------------------------

.. attribute:: Type

   :ref:`type_SubStateBoneWeights <animnode-type_substateboneweights>`

.. attribute:: Composition

   all

Elements
^^^^^^^^

boneName
""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:string``

No description provided.

includeDescendants
""""""""""""""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:boolean``

No description provided.

weight
""""""

.. attribute:: Minimum occurence

   0

.. attribute:: Maximum occurence

   1

.. attribute:: Type

   ``xs:float``

No description provided.


.. _animnode-rule_type:

rule_Type
---------

.. attribute:: Type

   :ref:`rule_Type <animnode-rule_type>`

.. attribute:: Composition

   all

Restrictions
^^^^^^^^^^^^

.. attribute:: Base

   ``xs:string``

.. attribute:: Enumeration

   

* ``STRING``
* ``BOOL``
* ``INT``
* ``FLOAT``
* ``OR``
* ``EQU``
* ``NEQ``
* ``STRNEQ``
* ``GTR``
* ``LESS``

.. _animnode-rule_time:

rule_Time
---------

.. attribute:: Type

   :ref:`rule_Time <animnode-rule_time>`

.. attribute:: Composition

   all

Restrictions
^^^^^^^^^^^^

.. attribute:: Base

   ``xs:string``

.. attribute:: Enumeration

   

* ``Start``
* ``End``

.. _animnode-rule_timepc:

rule_TimePc
-----------

.. attribute:: Type

   :ref:`rule_TimePc <animnode-rule_timepc>`

.. attribute:: Composition

   all

Restrictions
^^^^^^^^^^^^

.. attribute:: Base

   ``xs:float``


