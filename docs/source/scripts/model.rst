.. _scripts-model:

model
=====

.. attribute:: Soft Override

   Unknown

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

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`
- :ref:`vehicle <scripts-vehicle>`
- :ref:`part <scripts-part>`

This block can have the following child blocks:

- :ref:`attachment <scripts-attachment>`



ID
--

This block can have an ID.

.. attribute:: Optional

   ['part']

.. attribute:: Can have spaces

   False

.. attribute:: No ID for parents

   
* ``:ref:`vehicle <scripts-vehicle>```


Parameters
----------

.. _scripts-model-animationsmesh:

animationsMesh
^^^^^^^^^^^^^^

.. attribute:: Type

   block (block: :ref:`animationsMesh <scripts-animationsmesh>`)

Sets the `animations mesh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/animationsmesh.html>`_ for the model. This is used for models that are used for entities such as the character or animals.


.. _scripts-model-boneweight:

boneWeight
^^^^^^^^^^

.. attribute:: Type

   object (object: string->>float, kv: ' ', pairs: ';')

Sets the bone weight for the model. This is notably used for vehicle bones but it is yet documented how this actually impacts the model or animations linked to it.


.. _scripts-model-colorblue:

ColorBlue
^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-colorgreen:

ColorGreen
^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-colorred:

ColorRed
^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-cullface:

cullFace
^^^^^^^^

.. attribute:: Type

   string

.. attribute:: Default

   ``Back``

.. attribute:: Allowed values

   
* ``Back``
* ``Front``
* ``None``

Sets an OpenGL face culling mode for the model. By default the culling mode will be ``-1``\ , which defaults to ``Front``

``None`` supposedly disables face culling, all polygons are rendered. ``Back`` culls back-facing polygons, only renders front faces. ``Front`` culls front-facing polygons, only renders back faces.

This is likely the reason why when you have inverted normals on your model, you'll see through those inverted faces. You should keep this parameter by default however unless you actually need a model that can be seen on both sides of faces (plane models for example). This is used for muzzle flashes for guns notably.

Note that this parameter defaulting to ``Front`` sounds abnormal as the faces pointing in the direction of the normals are rendered in the game, so this suggests that something is done at some point to invert the normals or something else is going on that would render the correct faces of the model.


.. _scripts-model-file:

file
^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-invertx:

invertX
^^^^^^^

.. attribute:: Type

   boolean

If set to ``true``\ , the model scale will be inverted on the X axis.


.. _scripts-model-mesh:

mesh
^^^^

.. attribute:: Type

   Unknown

Path to the model file relative to the ``media/models_X`` folder. The model file can be either of ``.fbx`` or ``.glb`` but also the not recommended ``.x`` (read more `here <https://pzwiki.net/wiki/Modeling#File_types>`_\ ). The extension should not be included in the value of this parameter.

If your ``mesh`` parameter is set to ``my_model``\ , the game will expect the model to be stored in the following path:

.. code-block::

   📁 media
     📁 models_X
       📄 my_model.fbx

It is suggested to put your models in a subfolder of the ``models_X`` folder named after your mod to reduce the risk of model name conflicts with other mods.


.. _scripts-model-offset:

offset
^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-postprocess:

postProcess
^^^^^^^^^^^

.. attribute:: Type

   string

Sets post-processing steps for assimp to use when importing the model. Steps should be separated with ``;``\ , and prefixed with either ``+`` to add the step or ``-`` to remove the step (primarily used to remove a default step). Steps correspond to members of the `AiPostProcessSteps <https://github.com/assimp/assimp/blob/master/port/jassimp/jassimp/src/jassimp/AiPostProcessSteps.java>`_ enum. The default steps are ``FIND_INSTANCES``\ , ``MAKE_LEFT_HANDED``\ , ``LIMIT_BONE_WEIGHTS``\ , ``TRIANGULATE``\ , ``OPTIMIZE_MESHES``\ , ``REMOVE_REDUNDANT_MATERIALS``\ , ``JOIN_IDENTICAL_VERTICES``.

It is unclear what this is used for exactly and should probably not be modified unless you are looking into advanced model manipulation.


.. _scripts-model-scale:

scale
^^^^^

.. attribute:: Type

   float

Used to scale the model up or down. A value of ``1`` means the model is at its original size.


.. _scripts-model-shader:

shader
^^^^^^

.. attribute:: Type

   Unknown

Used to control what shader will apply on the model. The most common shaders which are used by the game are:


* ``animalEffect``
* ``door``
* ``vehicle``
* ``vehiclewheel``
* ``vehicle_multiuv``
* ``vehicle_norandom_multiuv``

The shaders are stored in the folder ``media/shaders``.


.. _scripts-model-specialkeyring:

specialKeyRing
^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-static:

static
^^^^^^

.. attribute:: Type

   boolean

If set to ``true``\ , the model will not deform with the bones it is parented to. This is typically used for non deformable objects, which means clothings should not be static.


.. _scripts-model-texture:

texture
^^^^^^^

.. attribute:: Type

   Unknown

Path to the texture file relative to the ``media/textures`` folder. The texture file should be of ``.png`` format only.

For example, if your ``texture`` parameter is set to ``my_model_texture``\ , the game will expect the texture to be stored in the following path:

.. code-block::

   📁 media
     📁 textures
       📄 my_model_texture.png

It is suggested to put your textures in a subfolder of the ``textures`` folder named after your mod to reduce the risk of texture name conflicts with other mods.


.. _scripts-model-undocorescale:

undoCoreScale
^^^^^^^^^^^^^

.. attribute:: Type

   boolean

.. attribute:: Default

   ``False``

If set to ``true``\ , the model scale will be multiplied by ``0.6666667``. This seems to be mostly used for tile models.


.. _scripts-model-attachmentparent:

attachmentParent
^^^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-attachmentself:

attachmentSelf
^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-ignorevehiclescale:

ignoreVehicleScale
^^^^^^^^^^^^^^^^^^

.. attribute:: Type

   Unknown

No description provided.


.. _scripts-model-rotate:

rotate
^^^^^^

.. attribute:: Type

   Unknown

No description provided.


