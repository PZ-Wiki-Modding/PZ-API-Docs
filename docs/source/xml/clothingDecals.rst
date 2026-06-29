clothingDecals
==============

Define decal groups for clothing items to use. Seems to be only used for shirts in the vanilla game and it is unknown if they can be used for other clothing items. The decal groups are linked to clothing items via the `m_DecalGroup <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-decalgroup>`_ parameter. They can also be linked to other decal groups via the `group <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingDecals.html#group>`_ parameter, allowing a decal group to use decals from another decal group.

The file needs to exactly stored at the path ``media/clothing/clothingDecals.xml`` for the game to recognize it. It won't clash with other mods or the vanilla game file. The syntax of this file should be as follows:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <clothingDecals>
     <group>
       <name>MyDecalGroup</name>
       <decal>myDecal</decal>
       <decal>anotherDecal</decal>
     </group>
     <group>
       <name>MyOtherDecalGroup</name>
       <group>MyDecalGroup</group>
     </group>
     <group>
       <name>MyThirdDecalGroup</name>
       <decal>thirdDecal</decal>
       <group>MyOtherDecalGroup</group>
     </group>
   </clothingDecals>


File Patterns
-------------

The following file patterns are used to determine what the valid path for the XML file can be, relative to the `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ folder.

- ``**/clothing/clothingDecals.xml``


.. _clothingdecals-type_clothingdecals:

Root Details
------------

:Element: clothingDecals

The root element is the top-level XML element that contains all other elements in the XML file.

:Type: ``type_clothingDecals``
:Composition: all

Elements
^^^^^^^^

group
"""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: :ref:`type_clothingDecalGroup <clothingdecals-type_clothingdecalgroup>`

Defines a decal group, that is a collection of decals associated to a name for referencing.


.. _clothingdecals-type_clothingdecalgroup:

type_clothingDecalGroup
-----------------------

:Type: ``type_clothingDecalGroup``
:Composition: all

Elements
^^^^^^^^

name
""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

A unique identifier for the decal group.

decal
"""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:string``

Refers to a texture file stored inside the folder ``media/textures/shirtdecals/``. The value needs to be the name of the file without the extension (which needs to be ``.png``\ ). Alternatively, it seems the game also accepts decals inside texture packs.

For example, for the following file structure:

.. code-block::

   📁 MyMod
     📁 media
       📁 textures
         📁 shirtdecals
           📄 myDecal.png
           📄 anotherDecal.png

The decal parameter should have this following syntax:

.. code-block::

   <decal>myDecal</decal>
   <decal>anotherDecal</decal>

group
"""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: ``xs:string``

Refers to another `group <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingDecals.html#group>`_. This allows that group to use decals of the referenced group.


