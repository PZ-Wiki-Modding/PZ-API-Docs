ScriptsDocs
===========

This section provides detailed documentation for all available `script <https://pzwiki.net/wiki/Scripts>`_ blocks.

Documentation Instructions
--------------------------

Each script block has its own documentation page. These will each contain metadata about the block (soft overides, is variant etc), a description and a few sections:
* Explaining the block's hierarchy in relation to other blocks (parents, children, mandatory children)
* About the block's ID
* A list of all parameters

A variant block means it is a block that will have completely different behavior from the original block and other variants based on conditions. These conditions are usually the ID of the block.

Each parameters will contain the following information based on what is provided by the game and the currently documented data from `pz-scripts-data <https://github.com/PZ-Wiki-Modding/pz-scripts-data>`_:
* The type of the parameter, which can be a simple type (string, number, boolean), a block type (which will link to the block's documentation), an array type (with a separator), or an object type (with key and value types, and separators)
* If the parameter is deprecated or not
* If the parameter is required or not
* If the parameter can be empty or not
* The default value of the parameter, if any
* The minimum and maximum values of the parameter, if any
* A list of allowed values for the parameter, if any

The type will always be provided, and if not yet documented it will show as `Unknown`. The other ones may not be provided due to a lack of information or these simply don't exist for the parameter.

Contributing
------------

You can contribute to this documentation by editing the `pz-scripts-data <https://github.com/PZ-Wiki-Modding/pz-scripts-data>`_ repository. You can read more about it `here <https://github.com/PZ-Wiki-Modding/pz-scripts-data/blob/main/CONTRIBUTING.md>`_.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 4
   scripts/_component_block
   scripts/alias
   scripts/anim
   scripts/animation
   scripts/animationsmesh
   scripts/area
   scripts/attachment
   scripts/blend
   scripts/blendblacklist
   scripts/blendwhitelist
   scripts/box
   scripts/categories
   scripts/character_profession_definition
   scripts/character_trait_definition
   scripts/clip
   scripts/clock
   scripts/colors
   scripts/component
   scripts/component/component-contextmenuconfig
   scripts/component/component-craftbench
   scripts/component/component-craftbenchsounds
   scripts/component/component-craftrecipe
   scripts/component/component-dryingcraftlogic
   scripts/component/component-durability
   scripts/component/component-fluidcontainer
   scripts/component/component-resources
   scripts/component/component-spriteconfig
   scripts/component/component-spriteoverlayconfig
   scripts/component/component-uiconfig
   scripts/component/component-wallcoveringconfig
   scripts/components
   scripts/container
   scripts/contextentry
   scripts/copyframe
   scripts/copyframes
   scripts/craftrecipe
   scripts/crawlthroughwheel
   scripts/cylinder
   scripts/data
   scripts/door
   scripts/energy
   scripts/entity
   scripts/evolvedrecipe
   scripts/face
   scripts/fixing
   scripts/fluid
   scripts/fluids
   scripts/group
   scripts/hand
   scripts/imports
   scripts/inputs
   scripts/isbasecomponentpanel
   scripts/istablelayoutcell
   scripts/item
   scripts/itemmapper
   scripts/layer
   scripts/layers
   scripts/lightbar
   scripts/lua
   scripts/mannequin
   scripts/maps
   scripts/model
   scripts/mods
   scripts/module
   scripts/option
   scripts/outputs
   scripts/overlaymapper
   scripts/part
   scripts/passenger
   scripts/physics
   scripts/physicshitreaction
   scripts/physicsshape
   scripts/poison
   scripts/polygon
   scripts/position
   scripts/progress
   scripts/properties
   scripts/properties
   scripts/ragdoll
   scripts/root-blends
   scripts/root-default
   scripts/root-mapbasexml
   scripts/root-mapinfo
   scripts/root-modinfo
   scripts/root-rules
   scripts/root-sandboxoptions
   scripts/root-scripts
   scripts/root-spritemodels
   scripts/root-tilegeometry
   scripts/root-tmxconfig
   scripts/rule
   scripts/skin
   scripts/sound
   scripts/soundtimeline
   scripts/spritemodel
   scripts/style
   scripts/switchseat
   scripts/table
   scripts/template
   scripts/tile
   scripts/tilegeometry
   scripts/tileset
   scripts/timedaction
   scripts/vehicle
   scripts/vehicleenginerpm
   scripts/wheel
   scripts/whitelist
   scripts/window
   scripts/xuiskin
