.. _scripts-fluid:

fluid
=====

:Soft Override: Unknown

Create a new fluid definition. Different properties can be provided for the fluid v ia the use of different children blocks:


* `Properties <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/properties.html>`_ is used to indicate the various stats change that drinking this fluid would cause to the player.
* `Categories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/categories.html>`_ act as tags for the fluid, to easily identify it.
* `BlendWhiteList <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html>`_ and `BlendBlackList <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendblacklist.html>`_ are used to provide rules for the blending of this fluid with other fluids.
* `Poison <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/poison.html>`_ is used to define poison properties for the fluid.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`

This block can have the following child blocks:

- :ref:`BlendWhiteList <scripts-blendwhitelist>`
- :ref:`Poison <scripts-poison>`
- :ref:`Categories <scripts-categories>`
- :ref:`Properties <scripts-properties>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


Parameters
----------

.. _scripts-fluid-colorreference:

ColorReference
^^^^^^^^^^^^^^

:Type: Unknown

A reference to a color defined in the Colors class. You can find a full list of the colors available in the `Colors <https://pz-wiki-modding.github.io/PZ-API-Docs/java/colors.html>`_ documentation.

For example, to use the color ``Azure`` from the documentation:

.. code-block:: cpp

   fluid yourFluid
   {
     ColorReference = Azure,
     ...
   }


.. _scripts-fluid-displayname:

DisplayName
^^^^^^^^^^^

:Type: Unknown

The name of the fluid that will be displayed in the game. The value corresponds to the key for the fluid's name in the `Fluids.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#fluids>`_ translation file. The translation keys for the fluid usually have the prefix ``Fluid_Name_`` but this is technically not required.

For example:

.. code-block:: cpp

   fluid yourFluid
   {
     DisplayName = Fluid_Name_YourFluid,
     ...
   }

And in the translation file of your mod:

.. code-block:: cpp

   {
     "Fluid_Name_YourFluid": "Your Fluid"
   }


