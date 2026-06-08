Tile Properties
===============

Reference documentation for tile properties that define the characteristics and behavior of tiles in the game world. The field is the identifier used in the Java and Lua code for this tile property, if you ever need to refer to it in `Lua <https://pzwiki.net/wiki/Lua_(API)>`_ code.

.. _tile-property-alwaysDraw:

alwaysDraw
^^^^^^^^^^

**Field:** ``TilePropertyKey.ALWAYS_DRAW``


.. _tile-property-AmbientSound:

AmbientSound
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.AMBIENT_SOUND``


.. _tile-property-attachedCeiling:

attachedCeiling
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_CEILING``


.. _tile-property-attachedE:

attachedE
^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_E``


.. _tile-property-AttachedFloor:

AttachedFloor
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_FLOOR``


.. _tile-property-attachedN:

attachedN
^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_N``


.. _tile-property-attachedNW:

attachedNW
^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_NW``


.. _tile-property-attachedS:

attachedS
^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_S``


.. _tile-property-attachedSE:

attachedSE
^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_SE``


.. _tile-property-attachedSurface:

attachedSurface
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_SURFACE``


.. _tile-property-AttachedToGlass:

AttachedToGlass
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_TO_GLASS``


.. _tile-property-attachedW:

attachedW
^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACHED_W``


.. _tile-property-attachtostairs:

attachtostairs
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ATTACH_TO_STAIRS``


.. _tile-property-bed:

bed
^^^

**Field:** ``TilePropertyKey.BED``


.. _tile-property-BedType:

BedType
^^^^^^^

**Field:** ``TilePropertyKey.BED_TYPE``


.. _tile-property-BlockRain:

BlockRain
^^^^^^^^^

**Field:** ``TilePropertyKey.BLOCK_RAIN``


.. _tile-property-blocksight:

blocksight
^^^^^^^^^^

**Field:** ``TilePropertyKey.BLOCK_SIGHT``


.. _tile-property-BlocksPlacement:

BlocksPlacement
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.BLOCKS_PLACEMENT``


If set to ``true``\ , other tiles cannot occupy the same square as this tile.


**Type:** ``boolean``


.. _tile-property-blueprint:

blueprint
^^^^^^^^^

**Field:** ``TilePropertyKey.BLUEPRINT``


.. _tile-property-burning:

burning
^^^^^^^

**Field:** ``TilePropertyKey.BURNING``


.. _tile-property-burntOut:

burntOut
^^^^^^^^

**Field:** ``TilePropertyKey.BURNT_OUT``


.. _tile-property-BurntTile:

BurntTile
^^^^^^^^^

**Field:** ``TilePropertyKey.BURNT_TILE``


.. _tile-property-Bush:

Bush
^^^^

**Field:** ``TilePropertyKey.BUSH``


.. _tile-property-CanAttachAnimal:

CanAttachAnimal
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CAN_ATTACH_ANIMAL``


.. _tile-property-canBeCut:

canBeCut
^^^^^^^^

**Field:** ``TilePropertyKey.CAN_BE_CUT``


.. _tile-property-canBeRemoved:

canBeRemoved
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CAN_BE_REMOVED``


.. _tile-property-CanBreak:

CanBreak
^^^^^^^^

**Field:** ``TilePropertyKey.CAN_BREAK``


`PickUpTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-pickuptool>`_ will indicate what tool the player needs to use to pick up the tile, while `PlaceTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-placetool>`_ will indicate what tool the player needs to use to place the tile.

If you want to add new tools, you can usually use the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ that you add to your `item tools <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#tags>`_\ , or you can also look into the lua file ``media/Moveables/ISMoveableDefinitions.lua`` to see how they add each new tools.

The `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_ is used to determine what level in the relevant skill you need to be able to pickup the tile. For example ``Hammer`` with a PickUpLevel of 2 will require a carpentry level of 2 to pickup the tile.

The `PickUpWeight <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickupweight>`_ will determine how much the tile weights in the inventory. This value is divded by 10, so for example a weight of 200 will mean an in-game encumbrance of 20. If `ForceSingleItem <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#forcesingleitem>`_ is set to ``true``\ , this is the total weight, otherwise this is the weight of each tile as a separate item.

`CanBreak <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#canbreak>`_ can be used to indicate that the tile has a chance to break when being picked up. The chance gets smaller based on the `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_.


**Type:** ``boolean``


.. _tile-property-canPathN:

canPathN
^^^^^^^^

**Field:** ``TilePropertyKey.CAN_PATH_N``


.. _tile-property-canPathW:

canPathW
^^^^^^^^

**Field:** ``TilePropertyKey.CAN_PATH_W``


.. _tile-property-CanScrap:

CanScrap
^^^^^^^^

**Field:** ``TilePropertyKey.CAN_SCRAP``


.. _tile-property-CantClimb:

CantClimb
^^^^^^^^^

**Field:** ``TilePropertyKey.CANT_CLIMB``


.. _tile-property-CarSlowFactor:

CarSlowFactor
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CAR_SLOW_FACTOR``


.. _tile-property-chairE:

chairE
^^^^^^

**Field:** ``TilePropertyKey.CHAIR_E``


.. _tile-property-chairN:

chairN
^^^^^^

**Field:** ``TilePropertyKey.CHAIR_N``


.. _tile-property-chairS:

chairS
^^^^^^

**Field:** ``TilePropertyKey.CHAIR_S``


.. _tile-property-chairW:

chairW
^^^^^^

**Field:** ``TilePropertyKey.CHAIR_W``


.. _tile-property-climbSheetE:

climbSheetE
^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_E``


.. _tile-property-climbSheetN:

climbSheetN
^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_N``


.. _tile-property-climbSheetS:

climbSheetS
^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_S``


.. _tile-property-climbSheetTopE:

climbSheetTopE
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_TOP_E``


.. _tile-property-climbSheetTopN:

climbSheetTopN
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_TOP_N``


.. _tile-property-climbSheetTopS:

climbSheetTopS
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_TOP_S``


.. _tile-property-climbSheetTopW:

climbSheetTopW
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_TOP_W``


.. _tile-property-climbSheetW:

climbSheetW
^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLIMB_SHEET_W``


.. _tile-property-CloseSneakBonus:

CloseSneakBonus
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CLOSE_SNEAK_BONUS``


.. _tile-property-collideN:

collideN
^^^^^^^^

**Field:** ``TilePropertyKey.COLLIDE_N``


.. _tile-property-collideW:

collideW
^^^^^^^^

**Field:** ``TilePropertyKey.COLLIDE_W``


.. _tile-property-connectX:

connectX
^^^^^^^^

**Field:** ``TilePropertyKey.CONNECT_X``


.. _tile-property-connectY:

connectY
^^^^^^^^

**Field:** ``TilePropertyKey.CONNECT_Y``


.. _tile-property-container:

container
^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER``


.. _tile-property-ContainerCapacity:

ContainerCapacity
^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_CAPACITY``


.. _tile-property-ContainerCloseSound:

ContainerCloseSound
^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_CLOSE_SOUND``


.. _tile-property-ContainerOpenSound:

ContainerOpenSound
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_OPEN_SOUND``


.. _tile-property-ContainerPosition:

ContainerPosition
^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_POSITION``


.. _tile-property-ContainerPutSound:

ContainerPutSound
^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_PUT_SOUND``


.. _tile-property-ContainerTakeSound:

ContainerTakeSound
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CONTAINER_TAKE_SOUND``


.. _tile-property-CornerNorthWall:

CornerNorthWall
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CORNER_NORTH_WALL``


.. _tile-property-CornerWestWall:

CornerWestWall
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CORNER_WEST_WALL``


.. _tile-property-curtainE:

curtainE
^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_E``


.. _tile-property-curtainN:

curtainN
^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_N``


.. _tile-property-CurtainOffset:

CurtainOffset
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_OFFSET``


.. _tile-property-curtainS:

curtainS
^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_S``


.. _tile-property-CurtainSound:

CurtainSound
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_SOUND``


.. _tile-property-curtainW:

curtainW
^^^^^^^^

**Field:** ``TilePropertyKey.CURTAIN_W``


.. _tile-property-CustomItem:

CustomItem
^^^^^^^^^^

**Field:** ``TilePropertyKey.CUSTOM_ITEM``


.. _tile-property-CustomName:

CustomName
^^^^^^^^^^

**Field:** ``TilePropertyKey.CUSTOM_NAME``


Used to define the item name, which will show as `GroupName <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#groupname>`_ + `CustomName <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#customname>`_. For example if CustomName is set to ``Bed`` and GroupName is set to ``Fancy``\ , it will show as ``Fancy Bed`` in the game. ``GroupName`` is used as a sub-category description of the object, such as its color, shape, name or quality.

Those properties need to be the same for multi-tile objects.


**Type:** ``string``


.. _tile-property-CutawayHint:

CutawayHint
^^^^^^^^^^^

**Field:** ``TilePropertyKey.CUTAWAY_HINT``


.. _tile-property-cutN:

cutN
^^^^

**Field:** ``TilePropertyKey.CUT_N``


.. _tile-property-cutW:

cutW
^^^^

**Field:** ``TilePropertyKey.CUT_W``


.. _tile-property-DamagedSprite:

DamagedSprite
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.DAMAGED_SPRITE``


.. _tile-property-diamondFloor:

diamondFloor
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.DIAMOND_FLOOR``


.. _tile-property-doorFrN:

doorFrN
^^^^^^^

**Field:** ``TilePropertyKey.DOOR_FR_N``


.. _tile-property-doorFrW:

doorFrW
^^^^^^^

**Field:** ``TilePropertyKey.DOOR_FR_W``


.. _tile-property-doorN:

doorN
^^^^^

**Field:** ``TilePropertyKey.DOOR_N``


.. _tile-property-DoorSound:

DoorSound
^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_SOUND``


.. _tile-property-doorTrans:

doorTrans
^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_TRANS``


.. _tile-property-doorW:

doorW
^^^^^

**Field:** ``TilePropertyKey.DOOR_W``


.. _tile-property-DoorWallN:

DoorWallN
^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_N``


.. _tile-property-DoorWallNTrans:

DoorWallNTrans
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_N_TRANS``


.. _tile-property-DoorWallNW:

DoorWallNW
^^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_NW``


.. _tile-property-DoorWallNWTrans:

DoorWallNWTrans
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_NW_TRANS``


.. _tile-property-DoorWallW:

DoorWallW
^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_W``


.. _tile-property-DoorWallWTrans:

DoorWallWTrans
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.DOOR_WALL_W_TRANS``


.. _tile-property-DoubleDoor:

DoubleDoor
^^^^^^^^^^

**Field:** ``TilePropertyKey.DOUBLE_DOOR``


.. _tile-property-DoubleDoor1:

DoubleDoor1
^^^^^^^^^^^

**Field:** ``TilePropertyKey.DOUBLE_DOOR_1``


.. _tile-property-DoubleDoor2:

DoubleDoor2
^^^^^^^^^^^

**Field:** ``TilePropertyKey.DOUBLE_DOOR_2``


.. _tile-property-EntityScript:

EntityScript
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ENTITY_SCRIPT``


.. _tile-property-EntityScriptName:

EntityScriptName
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.ENTITY_SCRIPT_NAME``


.. _tile-property-Eoffset:

Eoffset
^^^^^^^

**Field:** ``TilePropertyKey.E_OFFSET``


.. _tile-property-exterior:

exterior
^^^^^^^^

**Field:** ``TilePropertyKey.EXTERIOR``


.. _tile-property-Facing:

Facing
^^^^^^

**Field:** ``TilePropertyKey.FACING``


The direction the object is facing. This is not the orientation, but the direction the objects front looks towards. If the value is ``South``\ , it means the tile has a north orientation and thus would be facing south.

You can find an image which shows the directions of the game `here <https://pzwiki.net/wiki/Tile_properties#Directions>`_.


**Possible values:**

- ``North``
- ``East``
- ``South``
- ``West``

.. _tile-property-FasciaEdge:

FasciaEdge
^^^^^^^^^^

**Field:** ``TilePropertyKey.FASCIA_EDGE``


.. _tile-property-FasciaEdgeReversible:

FasciaEdgeReversible
^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FASCIA_EDGE_REVERSIBLE``


.. _tile-property-FenceTypeHigh:

FenceTypeHigh
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FENCE_TYPE_HIGH``


.. _tile-property-FenceTypeLow:

FenceTypeLow
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FENCE_TYPE_LOW``


.. _tile-property-firerequirement:

firerequirement
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FIRE_REQUIREMENT``


.. _tile-property-FloorAttachmentE:

FloorAttachmentE
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_ATTACHMENT_E``


.. _tile-property-FloorAttachmentN:

FloorAttachmentN
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_ATTACHMENT_N``


.. _tile-property-FloorAttachmentS:

FloorAttachmentS
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_ATTACHMENT_S``


.. _tile-property-FloorAttachmentW:

FloorAttachmentW
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_ATTACHMENT_W``


.. _tile-property-FloorHeight:

FloorHeight
^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_HEIGHT``


.. _tile-property-FloorHeightOneThird:

FloorHeightOneThird
^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_HEIGHT_ONE_THIRD``


.. _tile-property-FloorHeightTwoThirds:

FloorHeightTwoThirds
^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_HEIGHT_TWO_THIRDS``


.. _tile-property-FloorMaterial:

FloorMaterial
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_MATERIAL``


.. _tile-property-FloorOverlay:

FloorOverlay
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FLOOR_OVERLAY``


.. _tile-property-FootstepMaterial:

FootstepMaterial
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FOOTSTEP_MATERIAL``


.. _tile-property-ForceAmbient:

ForceAmbient
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FORCE_AMBIENT``


.. _tile-property-forcedLocked:

forcedLocked
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FORCED_LOCKED``


.. _tile-property-forceFade:

forceFade
^^^^^^^^^

**Field:** ``TilePropertyKey.FORCE_FADE``


.. _tile-property-forceLocked:

forceLocked
^^^^^^^^^^^

**Field:** ``TilePropertyKey.FORCE_LOCKED``


.. _tile-property-forceRender:

forceRender
^^^^^^^^^^^

**Field:** ``TilePropertyKey.FORCE_RENDER``


.. _tile-property-ForceSingleItem:

ForceSingleItem
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FORCE_SINGLE_ITEM``


Forces the object to be a single item in inventory even when it is made up of multiple tiles.



.. _tile-property-Freezer:

Freezer
^^^^^^^

**Field:** ``TilePropertyKey.FREEZER``


.. _tile-property-FreezerCapacity:

FreezerCapacity
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FREEZER_CAPACITY``


.. _tile-property-FreezerPosition:

FreezerPosition
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.FREEZER_POSITION``


.. _tile-property-fuelAmount:

fuelAmount
^^^^^^^^^^

**Field:** ``TilePropertyKey.FUEL_AMOUNT``


.. _tile-property-GarageDoor:

GarageDoor
^^^^^^^^^^

**Field:** ``TilePropertyKey.GARAGE_DOOR``


.. _tile-property-GeneratorSound:

GeneratorSound
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.GENERATOR_SOUND``


.. _tile-property-GenericCraftingSurface:

GenericCraftingSurface
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.GENERIC_CRAFTING_SURFACE``


.. _tile-property-GlassRemovedOffset:

GlassRemovedOffset
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.GLASS_REMOVED_OFFSET``


.. _tile-property-grassFloor:

grassFloor
^^^^^^^^^^

**Field:** ``TilePropertyKey.GRASS_FLOOR``


.. _tile-property-GrimeType:

GrimeType
^^^^^^^^^

**Field:** ``TilePropertyKey.GRIME_TYPE``


.. _tile-property-GroupName:

GroupName
^^^^^^^^^

**Field:** ``TilePropertyKey.GROUP_NAME``


Used to define the item name, which will show as `GroupName <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#groupname>`_ + `CustomName <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#customname>`_. For example if CustomName is set to ``Bed`` and GroupName is set to ``Fancy``\ , it will show as ``Fancy Bed`` in the game. ``GroupName`` is used as a sub-category description of the object, such as its color, shape, name or quality.

Those properties need to be the same for multi-tile objects.


**Type:** ``string``


.. _tile-property-halfheight:

halfheight
^^^^^^^^^^

**Field:** ``TilePropertyKey.HALF_HEIGHT``


.. _tile-property-HasLightOnSprite:

HasLightOnSprite
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.HAS_LIGHT_ON_SPRITE``


.. _tile-property-HasRaindrop:

HasRaindrop
^^^^^^^^^^^

**Field:** ``TilePropertyKey.HAS_RAINDROP``


.. _tile-property-HasRainSplashes:

HasRainSplashes
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.HAS_RAIN_SPLASHES``


.. _tile-property-hidewalls:

hidewalls
^^^^^^^^^

**Field:** ``TilePropertyKey.HIDE_WALLS``


.. _tile-property-HitByCar:

HitByCar
^^^^^^^^

**Field:** ``TilePropertyKey.HIT_BY_CAR``


.. _tile-property-HoppableN:

HoppableN
^^^^^^^^^

**Field:** ``TilePropertyKey.HOPPABLE_N``


.. _tile-property-HoppableW:

HoppableW
^^^^^^^^^

**Field:** ``TilePropertyKey.HOPPABLE_W``


.. _tile-property-IgnoreSurfaceSnap:

IgnoreSurfaceSnap
^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IGNORE_SURFACE_SNAP``


.. _tile-property-interior:

interior
^^^^^^^^

**Field:** ``TilePropertyKey.INTERIOR``


.. _tile-property-InteriorSide:

InteriorSide
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.INTERIOR_SIDE``


.. _tile-property-invisible:

invisible
^^^^^^^^^

**Field:** ``TilePropertyKey.INVISIBLE``


.. _tile-property-IsClosedState:

IsClosedState
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_CLOSED_STATE``


.. _tile-property-isEave:

isEave
^^^^^^

**Field:** ``TilePropertyKey.IS_EAVE``


.. _tile-property-IsFloorAttached:

IsFloorAttached
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_FLOOR_ATTACHED``


.. _tile-property-IsFridge:

IsFridge
^^^^^^^^

**Field:** ``TilePropertyKey.IS_FRIDGE``


.. _tile-property-IsGridExtensionTile:

IsGridExtensionTile
^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_GRID_EXTENSION_TILE``


.. _tile-property-IsHigh:

IsHigh
^^^^^^

**Field:** ``TilePropertyKey.IS_HIGH``


Indicates the tile is high, which means the tile only oocupies the upper half of the height, like a painting or wall shelf.


**Type:** ``boolean``


.. _tile-property-IsLow:

IsLow
^^^^^

**Field:** ``TilePropertyKey.IS_LOW``


Indicates the tile is low, which means the tile only oocupies the lower half of the height, like a bed or counter.


**Type:** ``boolean``


.. _tile-property-IsMirror:

IsMirror
^^^^^^^^

**Field:** ``TilePropertyKey.IS_MIRROR``


.. _tile-property-IsMoveAble:

IsMoveAble
^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_MOVE_ABLE``


Indicates the tile can be moved by the player. This will notably provide a `moveable item <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_. `MoveType <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#movetype>`_ allows you to set the type of moveable the tile is.


**Type:** ``boolean``


.. _tile-property-isMoveAbleObject:

isMoveAbleObject
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_MOVE_ABLE_OBJECT``


.. _tile-property-IsoType:

IsoType
^^^^^^^

**Field:** ``TilePropertyKey.ISO_TYPE``


Used to select the class the tile will be. IsoObject is the default but based on your choice there will different behaviors and interactions with the tile.


**Type:** ``string``

**Possible values:**

- ``IsoObject``
- ``IsoBarbecue``
- ``IsoBrokenGlass``
- ``IsoClothingDryer``
- ``IsoClothingWasher``
- ``IsoCombinationWasherDryer``
- ``IsoFireplace``
- ``IsoMannequin``
- ``IsoRadio``
- ``IsoJukebox``
- ``IsoStove``
- ``IsoTelevision``
- ``IsoMultiMedia``

.. _tile-property-IsPaintable:

IsPaintable
^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_PAINTABLE``


.. _tile-property-IsStackable:

IsStackable
^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_STACKABLE``


.. _tile-property-IsSurfaceOffset:

IsSurfaceOffset
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_SURFACE_OFFSET``


Indicates the object is offset by the `Surface <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#surface>`_ value when on a tabletop.


**Type:** ``boolean``


.. _tile-property-IsTable:

IsTable
^^^^^^^

**Field:** ``TilePropertyKey.IS_TABLE``


Will treat the tile as a table surface.



.. _tile-property-IsTableTop:

IsTableTop
^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_TABLE_TOP``


Will allow you to place tiles on top of this tile.



.. _tile-property-IsTrashCan:

IsTrashCan
^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_TRASH_CAN``


.. _tile-property-IsWaterCollector:

IsWaterCollector
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.IS_WATER_COLLECTOR``


.. _tile-property-ItemHeight:

ItemHeight
^^^^^^^^^^

**Field:** ``TilePropertyKey.ITEM_HEIGHT``

**Type:** ``integer``

**Default:** ``0``


.. _tile-property-jukebox:

jukebox
^^^^^^^

**Field:** ``TilePropertyKey.JUKEBOX``


.. _tile-property-lightB:

lightB
^^^^^^

**Field:** ``TilePropertyKey.LIGHT_B``


.. _tile-property-LightFilterB:

LightFilterB
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_FILTER_B``


.. _tile-property-LightFilterG:

LightFilterG
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_FILTER_G``


.. _tile-property-LightFilterIntensity:

LightFilterIntensity
^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_FILTER_INTENSITY``


.. _tile-property-LightFilterMix:

LightFilterMix
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_FILTER_MIX``


.. _tile-property-LightFilterR:

LightFilterR
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_FILTER_R``


.. _tile-property-lightG:

lightG
^^^^^^

**Field:** ``TilePropertyKey.LIGHT_G``


.. _tile-property-lightR:

lightR
^^^^^^

**Field:** ``TilePropertyKey.LIGHT_R``


.. _tile-property-LightRadius:

LightRadius
^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHT_RADIUS``


.. _tile-property-lightswitch:

lightswitch
^^^^^^^^^^^

**Field:** ``TilePropertyKey.LIGHTSWITCH``


.. _tile-property-LinkedLocIs:

LinkedLocIs
^^^^^^^^^^^

**Field:** ``TilePropertyKey.LINKED_LOC_IS``


.. _tile-property-LinkedOffset:

LinkedOffset
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.LINKED_OFFSET``


.. _tile-property-livingRoom:

livingRoom
^^^^^^^^^^

**Field:** ``TilePropertyKey.LIVING_ROOM``


.. _tile-property-makeWindowInvincible:

makeWindowInvincible
^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.MAKE_WINDOW_INVINCIBLE``


.. _tile-property-Material:

Material
^^^^^^^^

**Field:** ``TilePropertyKey.MATERIAL``


.. _tile-property-Material2:

Material2
^^^^^^^^^

**Field:** ``TilePropertyKey.MATERIAL_2``


.. _tile-property-Material3:

Material3
^^^^^^^^^

**Field:** ``TilePropertyKey.MATERIAL_3``


.. _tile-property-MaterialType:

MaterialType
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.MATERIAL_TYPE``


.. _tile-property-Microwave:

Microwave
^^^^^^^^^

**Field:** ``TilePropertyKey.MICROWAVE``


.. _tile-property-MinimumCarSpeedDmg:

MinimumCarSpeedDmg
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.MINIMUM_CAR_SPEED_DMG``


.. _tile-property-Movement:

Movement
^^^^^^^^

**Field:** ``TilePropertyKey.MOVEMENT``


.. _tile-property-MoveType:

MoveType
^^^^^^^^

**Field:** ``TilePropertyKey.MOVE_TYPE``


Sets the type of moveable the tile will be. This seems to be only related to the icon of item. There are also signs in the game code that when set to WallObject it will slightly impact the shape of the tile for physic interactions.


**Type:** ``string``

**Possible values:**

- ``Normal``
- ``WallObject``
- ``WindowObject``
- ``Window``
- ``FloorTile``
- ``FloorRug``
- ``Vegitation``

.. _tile-property-MoveWithWind:

MoveWithWind
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.MOVE_WITH_WIND``


.. _tile-property-name:

name
^^^^

**Field:** ``TilePropertyKey.NAME``


.. _tile-property-natureFloor:

natureFloor
^^^^^^^^^^^

**Field:** ``TilePropertyKey.NATURE_FLOOR``


.. _tile-property-NeverCutaway:

NeverCutaway
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.NEVER_CUTAWAY``


.. _tile-property-Noffset:

Noffset
^^^^^^^

**Field:** ``TilePropertyKey.N_OFFSET``


.. _tile-property-NoFreezer:

NoFreezer
^^^^^^^^^

**Field:** ``TilePropertyKey.NO_FREEZER``


.. _tile-property-noStart:

noStart
^^^^^^^

**Field:** ``TilePropertyKey.NO_START``


.. _tile-property-NoWallLighting:

NoWallLighting
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.NO_WALL_LIGHTING``


.. _tile-property-OpaquePixelsOnly:

OpaquePixelsOnly
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.OPAQUE_PIXELS_ONLY``

**Type:** ``boolean``


.. _tile-property-open:

open
^^^^

**Field:** ``TilePropertyKey.OPEN``


.. _tile-property-OpenTileOffset:

OpenTileOffset
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.OPEN_TILE_OFFSET``


.. _tile-property-PaintingType:

PaintingType
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.PAINTING_TYPE``


.. _tile-property-PhysicsMesh:

PhysicsMesh
^^^^^^^^^^^

**Field:** ``TilePropertyKey.PHYSICS_MESH``


.. _tile-property-PhysicsShape:

PhysicsShape
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.PHYSICS_SHAPE``


.. _tile-property-PickUpLevel:

PickUpLevel
^^^^^^^^^^^

**Field:** ``TilePropertyKey.PICK_UP_LEVEL``


`PickUpTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-pickuptool>`_ will indicate what tool the player needs to use to pick up the tile, while `PlaceTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-placetool>`_ will indicate what tool the player needs to use to place the tile.

If you want to add new tools, you can usually use the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ that you add to your `item tools <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#tags>`_\ , or you can also look into the lua file ``media/Moveables/ISMoveableDefinitions.lua`` to see how they add each new tools.

The `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_ is used to determine what level in the relevant skill you need to be able to pickup the tile. For example ``Hammer`` with a PickUpLevel of 2 will require a carpentry level of 2 to pickup the tile.

The `PickUpWeight <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickupweight>`_ will determine how much the tile weights in the inventory. This value is divded by 10, so for example a weight of 200 will mean an in-game encumbrance of 20. If `ForceSingleItem <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#forcesingleitem>`_ is set to ``true``\ , this is the total weight, otherwise this is the weight of each tile as a separate item.

`CanBreak <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#canbreak>`_ can be used to indicate that the tile has a chance to break when being picked up. The chance gets smaller based on the `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_.


**Type:** ``integer``


.. _tile-property-PickUpTool:

PickUpTool
^^^^^^^^^^

**Field:** ``TilePropertyKey.PICK_UP_TOOL``


`PickUpTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-pickuptool>`_ will indicate what tool the player needs to use to pick up the tile, while `PlaceTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-placetool>`_ will indicate what tool the player needs to use to place the tile.

If you want to add new tools, you can usually use the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ that you add to your `item tools <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#tags>`_\ , or you can also look into the lua file ``media/Moveables/ISMoveableDefinitions.lua`` to see how they add each new tools.

The `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_ is used to determine what level in the relevant skill you need to be able to pickup the tile. For example ``Hammer`` with a PickUpLevel of 2 will require a carpentry level of 2 to pickup the tile.

The `PickUpWeight <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickupweight>`_ will determine how much the tile weights in the inventory. This value is divded by 10, so for example a weight of 200 will mean an in-game encumbrance of 20. If `ForceSingleItem <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#forcesingleitem>`_ is set to ``true``\ , this is the total weight, otherwise this is the weight of each tile as a separate item.

`CanBreak <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#canbreak>`_ can be used to indicate that the tile has a chance to break when being picked up. The chance gets smaller based on the `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_.


**Type:** ``string``

**Possible values:**

- ``None``
- ``Hammer``
- ``Crowbar``
- ``Electrician``
- ``Cutter``
- ``Shovel``
- ``Wrench``

.. _tile-property-PickUpWeight:

PickUpWeight
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.PICK_UP_WEIGHT``


`PickUpTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-pickuptool>`_ will indicate what tool the player needs to use to pick up the tile, while `PlaceTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-placetool>`_ will indicate what tool the player needs to use to place the tile.

If you want to add new tools, you can usually use the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ that you add to your `item tools <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#tags>`_\ , or you can also look into the lua file ``media/Moveables/ISMoveableDefinitions.lua`` to see how they add each new tools.

The `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_ is used to determine what level in the relevant skill you need to be able to pickup the tile. For example ``Hammer`` with a PickUpLevel of 2 will require a carpentry level of 2 to pickup the tile.

The `PickUpWeight <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickupweight>`_ will determine how much the tile weights in the inventory. This value is divded by 10, so for example a weight of 200 will mean an in-game encumbrance of 20. If `ForceSingleItem <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#forcesingleitem>`_ is set to ``true``\ , this is the total weight, otherwise this is the weight of each tile as a separate item.

`CanBreak <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#canbreak>`_ can be used to indicate that the tile has a chance to break when being picked up. The chance gets smaller based on the `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_.


**Type:** ``integer``


.. _tile-property-PlaceTool:

PlaceTool
^^^^^^^^^

**Field:** ``TilePropertyKey.PLACE_TOOL``


`PickUpTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-pickuptool>`_ will indicate what tool the player needs to use to pick up the tile, while `PlaceTool <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-placetool>`_ will indicate what tool the player needs to use to place the tile.

If you want to add new tools, you can usually use the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ that you add to your `item tools <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#tags>`_\ , or you can also look into the lua file ``media/Moveables/ISMoveableDefinitions.lua`` to see how they add each new tools.

The `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_ is used to determine what level in the relevant skill you need to be able to pickup the tile. For example ``Hammer`` with a PickUpLevel of 2 will require a carpentry level of 2 to pickup the tile.

The `PickUpWeight <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickupweight>`_ will determine how much the tile weights in the inventory. This value is divded by 10, so for example a weight of 200 will mean an in-game encumbrance of 20. If `ForceSingleItem <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#forcesingleitem>`_ is set to ``true``\ , this is the total weight, otherwise this is the weight of each tile as a separate item.

`CanBreak <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#canbreak>`_ can be used to indicate that the tile has a chance to break when being picked up. The chance gets smaller based on the `PickUpLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#pickuplevel>`_.


**Type:** ``string``


.. _tile-property-propaneTank:

propaneTank
^^^^^^^^^^^

**Field:** ``TilePropertyKey.PROPANE_TANK``


.. _tile-property-radio:

radio
^^^^^

**Field:** ``TilePropertyKey.RADIO``


.. _tile-property-RenderLayer:

RenderLayer
^^^^^^^^^^^

**Field:** ``TilePropertyKey.RENDER_LAYER``


.. _tile-property-RoofGroup:

RoofGroup
^^^^^^^^^

**Field:** ``TilePropertyKey.ROOF_GROUP``


.. _tile-property-RoofWallStart:

RoofWallStart
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.UNUSROOF_WALL_STARTD``


.. _tile-property-ScrapSize:

ScrapSize
^^^^^^^^^

**Field:** ``TilePropertyKey.SCRAP_SIZE``


.. _tile-property-ScrapToolUseOverride:

ScrapToolUseOverride
^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SCRAP_TOOL_USE_OVERRIDE``


.. _tile-property-ScrapUseSkill:

ScrapUseSkill
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SCRAP_USE_SKILL``


.. _tile-property-ScrapUseTool:

ScrapUseTool
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SCRAP_USE_TOOL``


.. _tile-property-SeatMaterial:

SeatMaterial
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SEAT_MATERIAL``


.. _tile-property-signal:

signal
^^^^^^

**Field:** ``TilePropertyKey.SIGNAL``


.. _tile-property-SinkType:

SinkType
^^^^^^^^

**Field:** ``TilePropertyKey.SINK_TYPE``


.. _tile-property-SlopedSurfaceDirection:

SlopedSurfaceDirection
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SLOPED_SURFACE_DIRECTION``

**Type:** ``string``

**Possible values:**

- ``N``
- ``E``
- ``S``
- ``W``
- ``NE``
- ``NW``
- ``SE``
- ``SW``

.. _tile-property-SlopedSurfaceHeightMax:

SlopedSurfaceHeightMax
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SLOPED_SURFACE_HEIGHT_MAX``

**Type:** ``integer``

**Min:** ``0``

**Max:** ``100``

**Default:** ``0``


.. _tile-property-SlopedSurfaceHeightMin:

SlopedSurfaceHeightMin
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SLOPED_SURFACE_HEIGHT_MIN``

**Type:** ``integer``

**Min:** ``0``

**Max:** ``100``

**Default:** ``0``


.. _tile-property-SmashedTileOffset:

SmashedTileOffset
^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SMASHED_TILE_OFFSET``


.. _tile-property-smoke:

smoke
^^^^^

**Field:** ``TilePropertyKey.SMOKE``


.. _tile-property-SnowTile:

SnowTile
^^^^^^^^

**Field:** ``TilePropertyKey.SNOW_TILE``


.. _tile-property-Soffset:

Soffset
^^^^^^^

**Field:** ``TilePropertyKey.S_OFFSET``


.. _tile-property-solid:

solid
^^^^^

**Field:** ``TilePropertyKey.SOLID``


.. _tile-property-solidfloor:

solidfloor
^^^^^^^^^^

**Field:** ``TilePropertyKey.SOLID_FLOOR``


.. _tile-property-solidtrans:

solidtrans
^^^^^^^^^^

**Field:** ``TilePropertyKey.SOLID_TRANS``


.. _tile-property-SpearOnlyAttackThrough:

SpearOnlyAttackThrough
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SPEAR_ONLY_ATTACK_THROUGH``


.. _tile-property-SpriteGridLevel:

SpriteGridLevel
^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SPRITE_GRID_LEVEL``


.. _tile-property-SpriteGridPos:

SpriteGridPos
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.SPRITE_GRID_POS``


Used to specify the position the tile occupies when it is part of multi-tile objects. The first coordinates is in the direction X while the second is in the direction Y. The positive X direction is pointing towards the bottom right, while the positive Y direction is pointing towards the bottom left.

You can find an image which demonstrates the coordinates based on the positions `here <https://pzwiki.net/wiki/Tile_properties#Directions>`_.



.. _tile-property-StackReplaceTileOffset:

StackReplaceTileOffset
^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.STACK_REPLACE_TILE_OFFSET``

**Type:** ``integer``

**Default:** ``0``


.. _tile-property-stairsBN:

stairsBN
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_BN``


.. _tile-property-stairsBW:

stairsBW
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_BW``


.. _tile-property-stairsMN:

stairsMN
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_MN``


.. _tile-property-stairsMW:

stairsMW
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_MW``


.. _tile-property-stairsTN:

stairsTN
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_TN``


.. _tile-property-stairsTW:

stairsTW
^^^^^^^^

**Field:** ``TilePropertyKey.STAIRS_TW``


.. _tile-property-StopCar:

StopCar
^^^^^^^

**Field:** ``TilePropertyKey.STOP_CAR``


.. _tile-property-streetlight:

streetlight
^^^^^^^^^^^

**Field:** ``TilePropertyKey.STREETLIGHT``


.. _tile-property-Surface:

Surface
^^^^^^^

**Field:** ``TilePropertyKey.SURFACE``


The surface position of the tile when an object is on a tabletop surface like a counter or table. Requires `IsSurfaceOffset <https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/tile_properties.html#issurfaceoffset>`_ set to ``true``.


**Type:** ``integer``

**Default:** ``0``


.. _tile-property-tableN:

tableN
^^^^^^

**Field:** ``TilePropertyKey.TABLE_N``


.. _tile-property-taintedWater:

taintedWater
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TAINTED_WATER``


.. _tile-property-TallHoppableN:

TallHoppableN
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TALL_HOPPABLE_N``


.. _tile-property-TallHoppableW:

TallHoppableW
^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TALL_HOPPABLE_W``


.. _tile-property-ThumpSound:

ThumpSound
^^^^^^^^^^

**Field:** ``TilePropertyKey.THUMP_SOUND``


.. _tile-property-TieSheetRope:

TieSheetRope
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TIE_SHEET_ROPE``


.. _tile-property-TileOverlay:

TileOverlay
^^^^^^^^^^^

**Field:** ``TilePropertyKey.TILE_OVERLAY``


.. _tile-property-trans:

trans
^^^^^

**Field:** ``TilePropertyKey.TRANS``


.. _tile-property-Translucent:

Translucent
^^^^^^^^^^^

**Field:** ``TilePropertyKey.TRANSLUCENT``


.. _tile-property-transparentFloor:

transparentFloor
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TRANSPARENT_FLOOR``


.. _tile-property-transparentN:

transparentN
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TRANSPARENT_N``


.. _tile-property-transparentW:

transparentW
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TRANSPARENT_W``


.. _tile-property-TreatAsWallOrder:

TreatAsWallOrder
^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.TREAT_AS_WALL_ORDER``


.. _tile-property-tree:

tree
^^^^

**Field:** ``TilePropertyKey.TREE``


.. _tile-property-TV:

TV
^^

**Field:** ``TilePropertyKey.TV``


.. _tile-property-UnbreakableWindowN:

UnbreakableWindowN
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.UNBREAKABLE_WINDOW_N``


.. _tile-property-UnbreakableWindowNW:

UnbreakableWindowNW
^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.UNBREAKABLE_WINDOW_NW``


.. _tile-property-UnbreakableWindowW:

UnbreakableWindowW
^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.UNBREAKABLE_WINDOW_W``


.. _tile-property-unflammable:

unflammable
^^^^^^^^^^^

**Field:** ``TilePropertyKey.UNFLAMMABLE``


.. _tile-property-unlit:

unlit
^^^^^

**Field:** ``TilePropertyKey.UNLIT``


.. _tile-property-UseObjectDepthTexture:

UseObjectDepthTexture
^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.USE_OBJECT_DEPTH_TEXTURE``


Makes the tile use the tile depth of the tile it overlays. For example an overlay adding items on a shelf will use the shelf tile depth.


**Type:** ``boolean``


.. _tile-property-vegitation:

vegitation
^^^^^^^^^^

**Field:** ``TilePropertyKey.VEGITATION``


.. _tile-property-wall:

wall
^^^^

**Field:** ``TilePropertyKey.WALL``


.. _tile-property-WallN:

WallN
^^^^^

**Field:** ``TilePropertyKey.WALL_N``


.. _tile-property-WallNTrans:

WallNTrans
^^^^^^^^^^

**Field:** ``TilePropertyKey.WALL_N_TRANS``


.. _tile-property-WallNW:

WallNW
^^^^^^

**Field:** ``TilePropertyKey.WALL_NW``


.. _tile-property-WallNWTrans:

WallNWTrans
^^^^^^^^^^^

**Field:** ``TilePropertyKey.WALL_NW_TRANS``


.. _tile-property-WallObjectAllowDoorframe:

WallObjectAllowDoorframe
^^^^^^^^^^^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.WALL_OBJECT_ALLOW_DOORFRAME``


.. _tile-property-WallOverlay:

WallOverlay
^^^^^^^^^^^

**Field:** ``TilePropertyKey.WALL_OVERLAY``


.. _tile-property-WallSE:

WallSE
^^^^^^

**Field:** ``TilePropertyKey.WALL_SE``


.. _tile-property-WallType:

WallType
^^^^^^^^

**Field:** ``TilePropertyKey.WALL_TYPE``


.. _tile-property-WallW:

WallW
^^^^^

**Field:** ``TilePropertyKey.WALL_W``


.. _tile-property-WallWTrans:

WallWTrans
^^^^^^^^^^

**Field:** ``TilePropertyKey.WALL_W_TRANS``


.. _tile-property-water:

water
^^^^^

**Field:** ``TilePropertyKey.WATER``


.. _tile-property-waterAmount:

waterAmount
^^^^^^^^^^^

**Field:** ``TilePropertyKey.WATER_AMOUNT``


.. _tile-property-waterMaxAmount:

waterMaxAmount
^^^^^^^^^^^^^^

**Field:** ``TilePropertyKey.WATER_MAX_AMOUNT``


.. _tile-property-waterPiped:

waterPiped
^^^^^^^^^^

**Field:** ``TilePropertyKey.WATER_PIPED``


.. _tile-property-WestRoofB:

WestRoofB
^^^^^^^^^

**Field:** ``TilePropertyKey.WEST_ROOF_B``


.. _tile-property-WestRoofM:

WestRoofM
^^^^^^^^^

**Field:** ``TilePropertyKey.WEST_ROOF_M``


.. _tile-property-WestRoofT:

WestRoofT
^^^^^^^^^

**Field:** ``TilePropertyKey.WEST_ROOF_T``


.. _tile-property-WheelieBin:

WheelieBin
^^^^^^^^^^

**Field:** ``TilePropertyKey.WHEELIE_BIN``


.. _tile-property-windowFN:

windowFN
^^^^^^^^

**Field:** ``TilePropertyKey.WINDOW_FN``


.. _tile-property-windowFW:

windowFW
^^^^^^^^

**Field:** ``TilePropertyKey.WINDOW_FW``


.. _tile-property-WindowLocked:

WindowLocked
^^^^^^^^^^^^

**Field:** ``TilePropertyKey.WINDOW_LOCKED``


.. _tile-property-WindowN:

WindowN
^^^^^^^

**Field:** ``TilePropertyKey.WINDOW_N``


.. _tile-property-WindowW:

WindowW
^^^^^^^

**Field:** ``TilePropertyKey.WINDOW_W``


.. _tile-property-WindType:

WindType
^^^^^^^^

**Field:** ``TilePropertyKey.WIND_TYPE``


.. _tile-property-Woffset:

Woffset
^^^^^^^

**Field:** ``TilePropertyKey.W_OFFSET``


