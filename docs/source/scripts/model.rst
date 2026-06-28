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

Sets the `animations mesh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/animationsmesh.html>`_ for the model. This is used for models that are used for entities such as the character or animals.

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

:Type: object (object: string->>float, kv: ' ', pairs: ';')
:Attributes: Can be duplicated

Sets the bone weight for the model. This is notably used for vehicle bones but it is yet documented how this actually impacts the model or animations linked to it.

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

:Type: string
:Default: ``Back``

Sets an OpenGL face culling mode for the model. By default the culling mode will be ``-1``\ , which defaults to ``Front``

``None`` supposedly disables face culling, all polygons are rendered. ``Back`` culls back-facing polygons, only renders front faces. ``Front`` culls front-facing polygons, only renders back faces.

This is likely the reason why when you have inverted normals on your model, you'll see through those inverted faces. You should keep this parameter by default however unless you actually need a model that can be seen on both sides of faces (plane models for example). This is used for muzzle flashes for guns notably.

Note that this parameter defaulting to ``Front`` sounds abnormal as the faces pointing in the direction of the normals are rendered in the game, so this suggests that something is done at some point to invert the normals or something else is going on that would render the correct faces of the model.

Allowed values:

    - ``Back``
    - ``Front``
    - ``None``

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

:Type: boolean

If set to ``true``\ , the model scale will be inverted on the X axis.

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

:Type: string

Sets post-processing steps for assimp to use when importing the model. Steps should be separated with ``;``\ , and prefixed with either ``+`` to add the step or ``-`` to remove the step (primarily used to remove a default step). Steps correspond to members of the `AiPostProcessSteps <https://github.com/assimp/assimp/blob/master/port/jassimp/jassimp/src/jassimp/AiPostProcessSteps.java>`_ enum. The default steps are ``FIND_INSTANCES``\ , ``MAKE_LEFT_HANDED``\ , ``LIMIT_BONE_WEIGHTS``\ , ``TRIANGULATE``\ , ``OPTIMIZE_MESHES``\ , ``REMOVE_REDUNDANT_MATERIALS``\ , ``JOIN_IDENTICAL_VERTICES``.

It is unclear what this is used for exactly and should probably not be modified unless you are looking into advanced model manipulation.

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

:Type: boolean

If set to ``true``\ , the model will not deform with the bones it is parented to. This is typically used for non deformable objects, which means clothings should not be static.

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

:Type: boolean
:Default: ``False``

If set to ``true``\ , the model scale will be multiplied by ``0.6666667``. This seems to be mostly used for tile models.

