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

- ``**/clothing/clothingDecals.xml``

Root Element
------------

:Element: ``<clothingDecals>``
:Type: ``type_clothingDecals``

Structure
---------

The root element uses a **choice** composition, meaning it can contain any combination of the following elements:

- :ref:`<> <clothingDecals.type_clothingDecals.>` (optional): ````

Root Type Details
-----------------

.. _clothingDecals.type_clothingDecals:

type_clothingDecals
-------------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothingDecals.type_clothingDecals.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Defines a decal group, that is a collection of decals associated to a name for referencing.


Types
-----

.. _clothingDecals.type_clothingDecalGroup:

type_clothingDecalGroup
-----------------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothingDecals.type_clothingDecalGroup.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

A unique identifier for the decal group.

.. _clothingDecals.type_clothingDecalGroup.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Refers to a texture file stored inside the folder ``media/textures/shirtdecals/``. The value needs to be the name of the file without the extension (which needs to be ``.png``\ ). Alternatively, it seems the game also accepts decals inside texture packs.

For example, for the following file structure:

.. code-block::

   📁 media
     📁 textures
       📁 shirtdecals
         📄 myDecal.png
         📄 anotherDecal.png

The decal parameter should have this following syntax:

.. code-block::

   <decal>myDecal</decal>
   <decal>anotherDecal</decal>

.. _clothingDecals.type_clothingDecalGroup.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Refers to another `group <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingDecals.html#group>`_. This allows that group to use decals of the referenced group.

