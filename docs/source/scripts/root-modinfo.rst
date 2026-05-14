.. _root-modinfo:

ROOT-ModInfo
============

The mod.info file, which contains all the information about a mod.


Hierarchy
---------

This block does not require a parent block.


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _root-modinfo-author:

author
^^^^^^

:Type: string

Name of the author(s) of the mod. Multiple authors are often separated by commas but no convention exists.

.. _root-modinfo-category:

category
^^^^^^^^

:Type: string

Category is used for filtering mods in the in-game ModManager. Known categories are "map", "vehicle", "features", "modpack". Using other terms will not generate a new filter category.

.. _root-modinfo-description:

description
^^^^^^^^^^^

:Type: string

Description of your mod, which shows up in the mod manager. The description supports `ISRichTextPanel <https://pzwiki.net/wiki/ISRichTextPanel>`_ tags. A translation can be provided in the `Mod.json translation file <https://pzwiki.net/wiki/Translation>`_.

.. _root-modinfo-icon:

icon
^^^^

:Type: string

Image which will be used in the mod manager to put next to the name of the mod in the list of available mods. This image will be small and while you can use a full image size, you do not need it. You can set your poster as the icon too to not ship two images if desired.

.. _root-modinfo-id:

id
^^

:Type: string

The unique identifier of the mod, used in a mod list of the user or
servers to activate the mod. Make sure to use something unique which isn't shared
between mods. 

**Note:** This is not the same as the `Workshop ID <https://pzwiki.net/wiki/Workshop_ID>`_.

.. _root-modinfo-incompatible:

incompatible
^^^^^^^^^^^^

:Type: string

Mods that cannot be enabled at the same time as this mod. When enabled, the other mods will be unselectable. This mod will also become unselectable if any of the other mods are enabled.

Example:

.. code-block::

   incompatible=theUnwantedMod,theOtherOne

.. _root-modinfo-loadmodafter:

loadModAfter
^^^^^^^^^^^^

:Type: string

Loads the mod only after the set of mods listed.

Example:

.. code-block::

   loadModAfter=someMod,anotherMod

.. _root-modinfo-loadmodbefore:

loadModBefore
^^^^^^^^^^^^^

:Type: string

Loads the mod before the set of mods listed.

Example:

.. code-block::

   loadModBefore=someMod,anotherMod

.. _root-modinfo-modversion:

modversion
^^^^^^^^^^

:Type: string

Version of the mod.

.. _root-modinfo-name:

name
^^^^

:Type: string

The displayed name for your mod in the game's mod manager. A translation can be provided in the `Mod.json translation file <https://pzwiki.net/wiki/Translation>`_.

.. _root-modinfo-pack:

pack
^^^^

:Type: string

Name of pack files that need to be loaded by the game. Notably used for `Texture pack <https://pzwiki.net/wiki/Texture_pack>`_ and `Tile pack <https://pzwiki.net/wiki/Mapping>`_.

.. _root-modinfo-poster:

poster
^^^^^^

:Type: string
:Attributes: Can be duplicated

Image which will show up in the mod manager as the mod image. Multiple posters can be used to show multiple images, but the first one will be used as the main poster in the mod manager. The rest will be in a list of images of the mod that users can click on to view.

Example:

.. code-block::

   poster=poster.png
   poster=showcase.png
   poster=flying_chickens.png
   poster=credits.png

If you have multiple versions of your mod (e.g., 42.12 and 42.13) and don't want to copy your images, you can leave them in the common folder and use the following (but use unique names for these images since it will use the pool of all mods and their images in the common folder):

.. code-block::

   poster=../common/mymodname_poster.png
   poster=../common/mymodname_showcase.png
   poster=../common/mymodname_flying_chickens.png
   poster=../common/mymodname_credits.png

.. _root-modinfo-require:

require
^^^^^^^

:Type: string

Mods required to run this mod. Multiple mods can be specified separated by commas.

Example:

.. code-block::

   require=theNeededMod,theOtherOne

.. _root-modinfo-tiledef:

tiledef
^^^^^^^

:Type: string

Name of the tiledef with its ID that are added by the mod. You can find a community managed list of already used tiledef IDs in `Tiledefs used by mods <https://pzwiki.net/wiki/Tiledefs_used_by_mods>`_.

Example:

.. code-block::

   tiledef=Excavation 2112

If you upload your mod with a new tiledef ID, you can update the list to reduce the chance of incompatibility with other mods adding tile packs.

.. _root-modinfo-url:

url
^^^

:Type: string

Shows a URL link in the mod manager on the page of your mod for users to click on to open in their internet browser. The parameter appears as "Homepage" in the mod manager. For a list of valid links, see `URL <https://pzwiki.net/wiki/URL>`_.

.. _root-modinfo-versionmax:

versionMax
^^^^^^^^^^

:Type: string

The maximum version of the game the mod can be used on. This number needs to be in the format ``build.major`` at the very least, and not just ``build`` or it won't work. Example ``42.12``.

.. _root-modinfo-versionmin:

versionMin
^^^^^^^^^^

:Type: string

The minimum version of the game the mod can be used on. This number needs to be in the format ``build.major`` at the very least, and not just ``build`` or it won't work. Example ``42.0``.

