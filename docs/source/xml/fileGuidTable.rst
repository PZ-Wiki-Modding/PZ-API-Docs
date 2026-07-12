fileGuidTable
=============

Associate `clothingItem <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html>`_ files to a GUID for access in the `clothing <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html>`_ file. Whenever you want to use vanilla clothing in your clothing.xml file, you have to redefine them in your own mod's fileGuidTable.xml file, otherwise the game will not recognize them.

An example file would look like this:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <fileGuidTable>
     <files>
       <path>media/clothing/clothingItems/MyClothingItem.xml</path>
       <guid>YOUR_RANDOM_CLOTHING_ITEM_GUID_HERE</guid>
     </files>
     <files>
       <path>media/clothing/clothingItems/MyOtherClothingItem.xml</path>
       <guid>YOUR_OTHER_RANDOM_CLOTHING_ITEM_GUID_HERE</guid>
     </files>
   </fileGuidTable>

File Patterns
-------------

- ``**/media/fileGuidTable.xml``

Root Element
------------

:Element: ``<fileGuidTable>``
:Type: ``type_fileGuidTable``

Structure
---------

The root element uses a **choice** composition, meaning it can contain any combination of the following elements:

- :ref:`<> <fileGuidTable.type_fileGuidTable.>` (optional): ````

Root Type Details
-----------------

.. _fileGuidTable.type_fileGuidTable:

type_fileGuidTable
------------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _fileGuidTable.type_fileGuidTable.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Define a `clothingItem <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html>`_ file and GUID association.

For example for a clothingItem with the following file structure:

.. code-block::

   📁 media
     📁 clothing
       📁 clothingItems
         📄 MyClothingItem.xml

You should have the following parameters:

.. code-block:: xml

   <files>
     <path>media/clothing/clothingItems/MyClothingItem.xml</path>
     <guid>YOUR_RANDOM_CLOTHING_ITEM_GUID_HERE</guid>
   </files>


Types
-----

.. _fileGuidTable.type_fileGuidTable_files:

type_fileGuidTable_files
------------------------

:Type: Complex
:Composition: sequence

Elements
~~~~~~~~

.. _fileGuidTable.type_fileGuidTable_files.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The path to the `clothingItem <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html>`_ file. This path is relative to the upper folder of ``media``\ , for example for the following structure:

.. code-block::

   📁 MyMod
     📁 media
       📁 clothing
         📁 clothingItems
           📄 MyClothingItem.xml

You need the following parameter:

.. code-block:: xml

   <path>media/clothing/clothingItems/MyClothingItem.xml</path>

.. _fileGuidTable.type_fileGuidTable_files.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The `GUID <https://pzwiki.net/wiki/GUID>`_ of the clothing item. This needs to be the same as the one inside the `clothingItem <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ file for the clothing item to be recognized by the game.

