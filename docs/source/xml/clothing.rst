clothing
========

Define outfits for the male and female characters that can be used on zombies or the player. Items are provided with a probability value to define how likely they are to appear in the outfit.

The file should be stored at the exact path ``media/clothing/clothing.xml`` and won't clash with other mods or the vanilla game file. The syntax of this file should be as follows:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <outfitManager>
     <m_FemaleOutfits>
       <m_Name>MyOutfit</m_Name>
       <m_Guid>my-outfit-guid</m_Guid>
       <m_items>
         <item>
           <probability>0.5</probability>
           <itemGUID>my-clothing-item-guid</itemGUID>
         </item>
         <item>
           <probability>0.5</probability>
           <itemGUID>my-other-clothing-item-guid</itemGUID>
           <subItems>
             <subItem>
               <itemGUID>my-sub-clothing-item-guid</itemGUID>
             </subItem>
           </subItems>
         </item>
       </m_items>
     </m_MaleOutfits>
       <m_Name>MyOutfit</m_Name>
       <m_Guid>my-outfit-guid</m_Guid>
       <m_items>
         <item>
           <probability>0.5</probability>
           <itemGUID>my-clothing-item-guid</itemGUID>
         </item>
         <item>
           <probability>0.5</probability>
           <itemGUID>my-other-clothing-item-guid</itemGUID>
           <subItems>
             <subItem>
               <itemGUID>my-sub-clothing-item-guid</itemGUID>
             </subItem>
           </subItems>
         </item>
       </m_items>
     </m_MaleOutfits>
   </outfitManager>

File Patterns
-------------

- ``**/clothing/clothing.xml``

Root Element
------------

:Element: ``<outfitManager>``
:Type: ``type_clothing``

Structure
---------

The root element uses a **choice** composition, meaning it can contain any combination of the following elements:

- :ref:`<> <clothing.type_clothing.>` (optional): ````
- :ref:`<> <clothing.type_clothing.>` (optional): ````

Root Type Details
-----------------

.. _clothing.type_clothing:

type_clothing
-------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_clothing.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Define an outfit with `m_FemaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-femaleoutfits>`_ and `m_MaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-maleoutfits>`_ respectively for the female and male characters. If one of the two is not defined, it won't spawn naturally on the other gender in the game. Both male and female outfits can (and probably should) keep the same `m_Name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-name>`_ and `m_Guid <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-guid>`_ values.

.. _clothing.type_clothing.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Define an outfit with `m_FemaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-femaleoutfits>`_ and `m_MaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-maleoutfits>`_ respectively for the female and male characters. If one of the two is not defined, it won't spawn naturally on the other gender in the game. Both male and female outfits can (and probably should) keep the same `m_Name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-name>`_ and `m_Guid <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-guid>`_ values.


Types
-----

.. _clothing.type_item:

type_item
---------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_item.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The probability of the item being selected for the outfit. Needs to be a value between 0.0 and 1.0.

.. _clothing.type_item.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.

.. _clothing.type_item.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

Define a sub-item for a specific clothing item used in the outfit, so other items can also be picked.

.. _clothing.type_outfit:

type_outfit
-----------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The unique identifier for the outfit. Preferably keep it the same for the male and female variants.

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The `GUID <https://pzwiki.net/wiki/GUID>`_ of the outfit. This is the GUID associated to the clothing in the `fileGuidTable <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/fileGuidTable.html#guid>`_ and `clothingItem <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ files.

To use a vanilla clothing item in your outfit, you need to redefine it in your own mod's fileGuidTable.xml file, otherwise the game will not recognize it.

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

If set to ``true``\ , the outfit will spawn with random pants or shirts, respectivement for the parameters `m_Pants <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-pants>`_ and `m_Top <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-top>`_. When those two parameters are not set, they default to ``true``.

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_outfit.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

.. _clothing.type_subItem:

type_subItem
------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_subItem.unknown:

unknown
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``unknown``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.

