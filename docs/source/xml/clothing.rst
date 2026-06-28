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

- :ref:`<m_FemaleOutfits> <clothing.type_clothing.m_FemaleOutfits>` (optional): :ref:`type_outfit <clothing.type_outfit>`
- :ref:`<m_MaleOutfits> <clothing.type_clothing.m_MaleOutfits>` (optional): :ref:`type_outfit <clothing.type_outfit>`

Root Type Details
-----------------

.. _clothing.type_clothing:

type_clothing
-------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_clothing.m_FemaleOutfits:

m_FemaleOutfits
^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: :ref:`type_outfit <clothing.type_outfit>`

Define an outfit with `m_FemaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-femaleoutfits>`_ and `m_MaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-maleoutfits>`_ respectively for the female and male characters. If one of the two is not defined, it won't spawn naturally on the other gender in the game. Both male and female outfits can (and probably should) keep the same `m_Name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-name>`_ and `m_Guid <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-guid>`_ values.

.. _clothing.type_clothing.m_MaleOutfits:

m_MaleOutfits
^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: :ref:`type_outfit <clothing.type_outfit>`

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

.. _clothing.type_item.probability:

probability
^^^^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:float``

The probability of the item being selected for the outfit. Needs to be a value between 0.0 and 1.0.

.. _clothing.type_item.itemGUID:

itemGUID
^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.

.. _clothing.type_item.subItems:

subItems
^^^^^^^^

:Occurrence: Zero or more
:Type: :ref:`type_subItem <clothing.type_subItem>`

Define a sub-item for a specific clothing item used in the outfit, so other items can also be picked.

.. _clothing.type_outfit:

type_outfit
-----------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_outfit.m_Name:

m_Name
^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

The unique identifier for the outfit. Preferably keep it the same for the male and female variants.

.. _clothing.type_outfit.m_Guid:

m_Guid
^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

The `GUID <https://pzwiki.net/wiki/GUID>`_ of the outfit.

.. _clothing.type_outfit.m_Top:

m_Top
^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

If set to ``true``\ , the outfit will spawn with random pants or shirts, respectivement for the parameters `m_Pants <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-pants>`_ and `m_Top <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-top>`_. When those two parameters are not set, they default to ``true``.

.. _clothing.type_outfit.m_Pants:

m_Pants
^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _clothing.type_outfit.m_AllowPantsHue:

m_AllowPantsHue
^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _clothing.type_outfit.m_AllowTopTint:

m_AllowTopTint
^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _clothing.type_outfit.m_AllowPantsTint:

m_AllowPantsTint
^^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _clothing.type_outfit.m_AllowTShirtDecal:

m_AllowTShirtDecal
^^^^^^^^^^^^^^^^^^

:Occurrence: Optional (0 or 1)
:Type: ``xs:boolean``

.. _clothing.type_outfit.m_items:

m_items
^^^^^^^

:Occurrence: One or more
:Type: :ref:`type_item <clothing.type_item>`

.. _clothing.type_subItem:

type_subItem
------------

:Type: Complex
:Composition: choice

Elements
~~~~~~~~

.. _clothing.type_subItem.itemGUID:

itemGUID
^^^^^^^^

:Occurrence: Required (exactly once)
:Type: ``xs:string``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.

