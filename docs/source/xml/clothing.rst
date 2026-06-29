.. _xml-clothing:

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

The following file patterns are used to determine what the valid path for the XML file can be, relative to the `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ folder.

- ``**/clothing/clothing.xml``


.. _clothing-type_clothing:

Root Details
------------

:Element: outfitManager

The root element is the top-level XML element that contains all other elements in the XML file.

:Type: :ref:`type_clothing <clothing-type_clothing>`
:Composition: all

Elements
^^^^^^^^

m_FemaleOutfits
"""""""""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: :ref:`type_outfit <clothing-type_outfit>`

Define an outfit with `m_FemaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-femaleoutfits>`_ and `m_MaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-maleoutfits>`_ respectively for the female and male characters. If one of the two is not defined, it won't spawn naturally on the other gender in the game. Both male and female outfits can (and probably should) keep the same `m_Name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-name>`_ and `m_Guid <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-guid>`_ values.

m_MaleOutfits
"""""""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: :ref:`type_outfit <clothing-type_outfit>`

Define an outfit with `m_FemaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-femaleoutfits>`_ and `m_MaleOutfits <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-maleoutfits>`_ respectively for the female and male characters. If one of the two is not defined, it won't spawn naturally on the other gender in the game. Both male and female outfits can (and probably should) keep the same `m_Name <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-name>`_ and `m_Guid <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-guid>`_ values.


.. _clothing-type_outfit:

type_outfit
-----------

:Type: :ref:`type_outfit <clothing-type_outfit>`
:Composition: all

Elements
^^^^^^^^

m_Name
""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The unique identifier for the outfit. Preferably keep it the same for the male and female variants.

m_Guid
""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `GUID <https://pzwiki.net/wiki/GUID>`_ of the outfit.

m_Top
"""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

If set to ``true``\ , the outfit will spawn with random pants or shirts, respectivement for the parameters `m_Pants <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-pants>`_ and `m_Top <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-top>`_. When those two parameters are not set, they default to ``true``.

m_Pants
"""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

No description provided.

m_AllowPantsHue
"""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

No description provided.

m_AllowTopTint
""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

No description provided.

m_AllowPantsTint
""""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

No description provided.

m_AllowTShirtDecal
""""""""""""""""""

:Minimum occurence: 0
:Maximum occurence: 1
:Type: ``xs:boolean``

No description provided.

m_items
"""""""

:Minimum occurence: 1
:Maximum occurence: unbounded
:Type: :ref:`type_item <clothing-type_item>`

No description provided.


.. _clothing-type_item:

type_item
---------

:Type: :ref:`type_item <clothing-type_item>`
:Composition: all

Elements
^^^^^^^^

probability
"""""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:float``

The probability of the item being selected for the outfit. Needs to be a value between 0.0 and 1.0.

itemGUID
""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.

subItems
""""""""

:Minimum occurence: 0
:Maximum occurence: unbounded
:Type: :ref:`type_subItem <clothing-type_subitem>`

Define a sub-item for a specific clothing item used in the outfit, so other items can also be picked.


.. _clothing-type_subitem:

type_subItem
------------

:Type: :ref:`type_subItem <clothing-type_subitem>`
:Composition: all

Elements
^^^^^^^^

itemGUID
""""""""

:Minimum occurence: 1
:Maximum occurence: 1
:Type: ``xs:string``

The `GUID <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothingItem.html#m-guid>`_ of the clothing item that should be part of the outfit. You can define extra outfits thanks to the `subItems <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/clothing.html#m-subitems>`_ parameter.


