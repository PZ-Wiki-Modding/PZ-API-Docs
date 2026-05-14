.. _attachment:

attachment
==========

Defines an attachment point on a `model <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html>`_ or `vehicle <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html>`_ block. The ID is the attachment name, it can be a custom ID or an existing one often used to define specific attachments. While manually modifying the attachment block is definitely possible, it is recommended to use the `attachment editor <https://pzwiki.net/wiki/Attachment_Editor>`_ to create and edit those attachments.

The syntax of this block should be as follows:

.. code-block:: cpp

   model upperScriptDefinition
   {
       ...
       attachment attachmentPointName
       {
           ...
       }
       ...
   }

For example:

.. code-block:: cpp

   model Burger
   {
       mesh = Burger,

       attachment Bip01_Prop2
       {
           offset = 0.0142 0.0401 0.0000,
           rotate = -23.3606 21.2788 37.5386,
           scale = 0.8280,
       }
   }

Here is a list of attachment points provided by the game:


* 1schoolbaglefthand
* 1schoolbagrighthand
* AnkleHolster
* Bip01_Prop1
* Bip01_Prop2
* ShoulderHolster
* axe_back
* back
* back_guitar
* back_guitar_acoustic
* backpack_left
* bedroll_bottom
* bedroll_bottom_alice
* bedroll_bottom_big
* belt_left
* belt_left_screwdriver
* belt_left_upside
* belt_right
* belt_right_screwdriver
* belt_right_upside
* belt_rotated_left
* belt_rotated_right
* big_blade_back_bag
* big_w_back
* big_w_back_bag
* bighikingbaglefthand
* bighikingbagrighthand
* blade_back
* crowbar_back
* duffelbaglefthand
* duffelbagrighthand
* fryingpan_back
* fryingpan_back_bag
* hikingbaglefthand
* hikingbagrighthand
* holster_left
* holster_right
* knife_belt_back
* knife_belt_front
* knife_head
* knife_in_back
* knife_left_leg
* knife_right_leg
* knife_shoulder
* knife_stomach
* meatcleaver_in_back
* meatcleaver_left
* meatcleaver_right
* nightstick_left
* nightstick_right
* racket_back
* racket_back_bag
* rifle_back
* rifle_back_bag
* saucepan_back
* saucepan_back_bag
* shovel_back
* shovel_back_bag
* stomach
* walkie_belt_left
* walkie_belt_right
* webbing_left_knife
* webbing_left_walkie
* webbing_left_knife
* webbing_left_walkie
* wrench_left
* wrench_right


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`vehicle`
- :ref:`model`
- :ref:`template`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _attachment-bone:

bone
^^^^

:Type: Any

.. code-block::

   The name of the bone to which the model is attached to. 


.. code-block:: cpp

    bone = Bip01_L_Hand,

.. _attachment-offset:

offset
^^^^^^

:Type: array (array of float, separator: ' ')

The position offset of the model relative to the bone. This is a vector in the format ``x y z``. 

.. code-block:: cpp

   offset = -0.0300 -0.1020 0.1210,

.. _attachment-rotate:

rotate
^^^^^^

:Type: array (array of float, separator: ' ')

The rotation of the model relative to the bone. This is a vector in the format ``x y z``. The values are degrees.

.. code-block:: cpp

   rotate = -60.0000 -49.0000 -3.0000,

.. _attachment-scale:

scale
^^^^^

:Type: float

The scale multiplier applied to the model attached to this attachment point.

.. code-block:: cpp

   scale = 0.5,

.. _attachment-zoffset:

zoffset
^^^^^^^

:Type: Any

No description

