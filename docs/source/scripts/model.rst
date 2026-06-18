.. _model:

model
=====

Used to define a model properties so it can be used in other elements of the game, most notably in `items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ and `vehicles <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html>`_. The basic structure of a model block is as follows:

.. code-block:: cpp

   module YourModule {
     model YourModel {
       mesh = your_model,
       texture = your_model_texture,
     }
   }

`Attachments <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/attachment.html>`_ blocks can also be added to the model definition to specify how the model should be placed, rotated and scaled when attached to a parent model.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`
- :ref:`vehicle`
- :ref:`part`

**Possible Child Blocks:**

- :ref:`attachment`


ID Properties
-------------

This block should have an ID.

**Incompatible Parents:**

- vehicle


Parameters
----------

.. _model-animationsmesh:

animationsMesh
^^^^^^^^^^^^^^

:Type: block (block: :ref:`animationsMesh`)

No description

.. _model-attachmentparent:

attachmentParent
^^^^^^^^^^^^^^^^

:Type: Any

No description

.. _model-attachmentself:

attachmentSelf
^^^^^^^^^^^^^^

:Type: Any

No description

.. _model-boneweight:

boneWeight
^^^^^^^^^^

:Type: Any

No description

.. _model-colorblue:

ColorBlue
^^^^^^^^^

:Type: Any

No description

.. _model-colorgreen:

ColorGreen
^^^^^^^^^^

:Type: Any

No description

.. _model-colorred:

ColorRed
^^^^^^^^

:Type: Any

No description

.. _model-cullface:

cullFace
^^^^^^^^

:Type: Any

No description

.. _model-file:

file
^^^^

:Type: Any

No description

.. _model-ignorevehiclescale:

ignoreVehicleScale
^^^^^^^^^^^^^^^^^^

:Type: Any

No description

.. _model-invertx:

invertX
^^^^^^^

:Type: Any

No description

.. _model-mesh:

mesh
^^^^

:Type: Any

Path to the model file relative to the ``media/models_X`` folder. The model file can be either of ``.fbx`` or ``.glb`` but also the not recommended ``.x`` (read more `here <https://pzwiki.net/wiki/Modeling#File_types>`_\ ). The extension should not be included in the value of this parameter.

If your ``mesh`` parameter is set to ``my_model``\ , the game will expect the model to be stored in the following path:

.. code-block::

   📁 media
     📁 models_X
       📄 my_model.fbx

It is suggested to put your models in a subfolder of the ``models_X`` folder named after your mod to reduce the risk of model name conflicts with other mods.

.. _model-offset:

offset
^^^^^^

:Type: Any

No description

.. _model-postprocess:

postProcess
^^^^^^^^^^^

:Type: Any

No description

.. _model-rotate:

rotate
^^^^^^

:Type: Any

No description

.. _model-scale:

scale
^^^^^

:Type: float

Used to scale the model up or down. A value of ``1`` means the model is at its original size.

.. _model-shader:

shader
^^^^^^

:Type: Any

Used to control what shader will apply on the model. The most common shaders which are used by the game are:


* ``animalEffect``
* ``door``
* ``vehicle``
* ``vehiclewheel``
* ``vehicle_multiuv``
* ``vehicle_norandom_multiuv``

The shaders are stored in the folder ``media/shaders``.

.. _model-specialkeyring:

specialKeyRing
^^^^^^^^^^^^^^

:Type: Any

No description

.. _model-static:

static
^^^^^^

:Type: Any

No description

.. _model-texture:

texture
^^^^^^^

:Type: Any

Path to the texture file relative to the ``media/textures`` folder. The texture file should be of ``.png`` format only.

For example, if your ``texture`` parameter is set to ``my_model_texture``\ , the game will expect the texture to be stored in the following path:

.. code-block::

   📁 media
     📁 textures
       📄 my_model_texture.png

It is suggested to put your textures in a subfolder of the ``textures`` folder named after your mod to reduce the risk of texture name conflicts with other mods.

.. _model-undocorescale:

undoCoreScale
^^^^^^^^^^^^^

:Type: Any

No description

