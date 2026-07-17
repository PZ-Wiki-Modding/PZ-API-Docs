.. _xml-clothingitem:

clothingItem
============

Clothing items are first defined with an `item <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ script block, but a lot of their properties are defined in the clothing item XML files. Some of these properties include masks, textures, shaders, and models. The clothing items are linked to these files via the `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ parameter.

The clothing item XML files need to be stored in the path ``media/clothing/clothingItems/`` for the game to recognize them.


File Patterns
-------------

The following file patterns are used to determine what the valid path for the XML file can be, relative to the `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ folder.

- ``**/clothing/clothingItems/**/*.xml``


.. _clothingitem-type_clothingitem:

Root Details
------------

:Element: clothingItem

The root element is the top-level XML element that contains all other elements in the XML file.

:Type: :ref:`type_clothingItem <clothingitem-type_clothingitem>`
:Composition: all

Elements
^^^^^^^^

m_MaleModel
"""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `m_MaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-malemodel>`_ and `m_FemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-femalemodel>`_ are used to specify what model file will be used for the clothing item. Those parameters **should** be left empty when the clothing item is a body texture.

The model file are accessed relatively to the parent folder of `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ and relative to the models_X folder, but preferably should be stored in ``media/models_X`` and accessed relative to it.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 models_X
       📁 MyAwesomeClothing
         📄 myClothing.fbx

These parameters should have this following syntax:

.. code-block::

   <m_MaleModel>MyAwesomeClothing/myClothing</m_MaleModel>

The path separators can be either unix with ``/`` or ``\\``\ , both are valid. Make sure to not add the extension.

`m_AltMaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altmalemodel>`_ and `m_AltFemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altfemalemodel>`_ are used to define alternative models for clothing items that share the same `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#bodylocation>`_ slot as another clothing item. Alternative models relationship between BodyLocations are set in the Lua (in ``media/lua/shared/NPCs/BodyLocations.lua`` for the vanilla game).

m_FemaleModel
"""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `m_MaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-malemodel>`_ and `m_FemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-femalemodel>`_ are used to specify what model file will be used for the clothing item. Those parameters **should** be left empty when the clothing item is a body texture.

The model file are accessed relatively to the parent folder of `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ and relative to the models_X folder, but preferably should be stored in ``media/models_X`` and accessed relative to it.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 models_X
       📁 MyAwesomeClothing
         📄 myClothing.fbx

These parameters should have this following syntax:

.. code-block::

   <m_MaleModel>MyAwesomeClothing/myClothing</m_MaleModel>

The path separators can be either unix with ``/`` or ``\\``\ , both are valid. Make sure to not add the extension.

`m_AltMaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altmalemodel>`_ and `m_AltFemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altfemalemodel>`_ are used to define alternative models for clothing items that share the same `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#bodylocation>`_ slot as another clothing item. Alternative models relationship between BodyLocations are set in the Lua (in ``media/lua/shared/NPCs/BodyLocations.lua`` for the vanilla game).

m_AltMaleModel
""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:string``

The `m_MaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-malemodel>`_ and `m_FemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-femalemodel>`_ are used to specify what model file will be used for the clothing item. Those parameters **should** be left empty when the clothing item is a body texture.

The model file are accessed relatively to the parent folder of `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ and relative to the models_X folder, but preferably should be stored in ``media/models_X`` and accessed relative to it.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 models_X
       📁 MyAwesomeClothing
         📄 myClothing.fbx

These parameters should have this following syntax:

.. code-block::

   <m_MaleModel>MyAwesomeClothing/myClothing</m_MaleModel>

The path separators can be either unix with ``/`` or ``\\``\ , both are valid. Make sure to not add the extension.

`m_AltMaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altmalemodel>`_ and `m_AltFemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altfemalemodel>`_ are used to define alternative models for clothing items that share the same `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#bodylocation>`_ slot as another clothing item. Alternative models relationship between BodyLocations are set in the Lua (in ``media/lua/shared/NPCs/BodyLocations.lua`` for the vanilla game).

m_AltFemaleModel
""""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:string``

The `m_MaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-malemodel>`_ and `m_FemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-femalemodel>`_ are used to specify what model file will be used for the clothing item. Those parameters **should** be left empty when the clothing item is a body texture.

The model file are accessed relatively to the parent folder of `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ and relative to the models_X folder, but preferably should be stored in ``media/models_X`` and accessed relative to it.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 models_X
       📁 MyAwesomeClothing
         📄 myClothing.fbx

These parameters should have this following syntax:

.. code-block::

   <m_MaleModel>MyAwesomeClothing/myClothing</m_MaleModel>

The path separators can be either unix with ``/`` or ``\\``\ , both are valid. Make sure to not add the extension.

`m_AltMaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altmalemodel>`_ and `m_AltFemaleModel <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-altfemalemodel>`_ are used to define alternative models for clothing items that share the same `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#bodylocation>`_ slot as another clothing item. Alternative models relationship between BodyLocations are set in the Lua (in ``media/lua/shared/NPCs/BodyLocations.lua`` for the vanilla game).

m_GUID
""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `GUID <https://pzwiki.net/wiki/GUID>`_ of the clothing item. This needs to be the same as the one inside the `fileGuidTable <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/fileGuidTable.html#guid>`_ file for the clothing item to be recognized by the game.

m_Static
""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:boolean``

If ``true``\ , the clothing item won't deform with the character's body. This is used for items like backpacks or hats that should not change shape with the character's body.

m_AllowRandomHue
""""""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:boolean``

When `m_AllowRandomHue <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-allowrandomhue>`_ or `m_AllowRandomTint <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-allowrandomtint>`_ are set to ``true``\ , the clothing item will respectively have a random hue or tint applied to it. m_AllowRandomHue doesn't seem to be impactful on the clothing item as much as m_AllowRandomTint, which will apply the random color on white areas of the clothing item.

m_AllowRandomTint
"""""""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:boolean``

When `m_AllowRandomHue <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-allowrandomhue>`_ or `m_AllowRandomTint <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-allowrandomtint>`_ are set to ``true``\ , the clothing item will respectively have a random hue or tint applied to it. m_AllowRandomHue doesn't seem to be impactful on the clothing item as much as m_AllowRandomTint, which will apply the random color on white areas of the clothing item.

m_AttachBone
""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

Specifies a bone to attach the clothing item to. Mostly notably used for hats and some arm protection items. To attach to the head, use ``Bip01_Head``.

m_Shader
""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

Specifies a shader to use for the clothing item. The default shader used by clothing items is ``basicEffect``. The value needs to be the filename of the shader inside the folder ``media/shaders``.

textureChoices
""""""""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:string``

`textureChoices <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#texturechoices>`_ sets the texture used by the clothing item. Many of those can be provided as random choices for the clothing item. The textures need to be stored in the folder ``media/textures``.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 textures
       📁 CoolMod
         📄 texture1.png
         📄 texture2.png

You'd have:

.. code-block:: xml

   <textureChoices>CoolMod/texture1</textureChoices>
   <textureChoices>CoolMod/texture2</textureChoices>

`m_BaseTextures <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-basetextures>`_ is used specifically for 2D clothing items that are applied on the character's body directly (tshirts, pants, socks...). The folder structure is the same as for `textureChoices <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#texturechoices>`_.

m_BaseTextures
""""""""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:string``

`textureChoices <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#texturechoices>`_ sets the texture used by the clothing item. Many of those can be provided as random choices for the clothing item. The textures need to be stored in the folder ``media/textures``.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 textures
       📁 CoolMod
         📄 texture1.png
         📄 texture2.png

You'd have:

.. code-block:: xml

   <textureChoices>CoolMod/texture1</textureChoices>
   <textureChoices>CoolMod/texture2</textureChoices>

`m_BaseTextures <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-basetextures>`_ is used specifically for 2D clothing items that are applied on the character's body directly (tshirts, pants, socks...). The folder structure is the same as for `textureChoices <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#texturechoices>`_.

m_Masks
"""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:integer``

`m_Masks <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-masks>`_ when set to a specific integer value will hide specific elements of the character's body model. This is notably used to remove clipping with body parts that are hidden by the clothing item. For example, a jacket will hide the torso and arms, so to reduce risks of clipping you may want to hide these.

You can find a list of the values and their corresponding body parts in the Project Zomboid Modding Archives `here <https://github.com/PZ-Wiki-Modding/Archive.Project-Zomboid-Modding/blob/main/Clothing/Masks/Mask.png>`_.

You can insert as many of these as you want, for example:

.. code-block:: xml

   <m_Masks>12</m_Masks>
   <m_Masks>13</m_Masks>
   <m_Masks>14</m_Masks>
   <m_Masks>3</m_Masks>
   <m_Masks>5</m_Masks>

`m_UnderlayMasksFolder <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-underlaymasksfolder>`_ supposedly is used to add a texture folder in which you have modified versions of these masks if you ever need to adjust the masks for your own clothing items without clashing with other mods custom masks.

m_MasksFolder
"""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

Default value is ``media/textures/Body/Masks``. Some clothing behaviors seem to be hardcoded to this path. You can notably use it to deactivate masks by setting the value to ``media/textures/Clothes/Hat/Masks``\ , but it will also deactivate damage (holes) and blood effects.

m_UnderlayMasksFolder
"""""""""""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

Default value is ``media/textures/Body/UnderlayMasks``. Some clothing behaviors seem to be hardcoded to this path.

m_HatCategory
"""""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

Seems to be used to specify if a hat will hide the hair and beard. Notable values are:


* ``default``
* ``nohairnobeard``
* ``nobeard``
* ``nohair``

Then values ``Group`` followed by a number ``01``\ , ``02``\ , etc are also used.

m_SpawnWith
"""""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:string``

Link to other items that this clothingItem should spawn with. This is for example used to make left and right elbow pads spawn together. The value needs to be the `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the other clothing item.

To add multiple items, you can add multiple ``<m_SpawnWith>`` elements:

.. code-block:: xml

   <m_SpawnWith>GUID1</m_SpawnWith>
   <m_SpawnWith>GUID2</m_SpawnWith>
   <m_SpawnWith>GUID3</m_SpawnWith>
   ...

m_DecalGroup
""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:string``

Refers to the `name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingDecals.html#name>`_ parameter of a decal group defined in the `clothingDecals.xml <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingDecals.html>`_ file. The clothing decals are used to add additional textures on top of the clothing item. This is most notably used to add logos on t-shirts, and it is possible to add multiple logos on a single decal group.


