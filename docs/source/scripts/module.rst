.. _module:

module
======

A module serves as a namespace for your scripts and is the barebone for most scripts you will create in your mod. The game's namespace is ``Base``\ , and while you can insert in it, it is recommended to use your own module for your mod's scripts to avoid conflicts with the game and other mods.

To define a module, you need to create a block as follows, by changing the ID to a unique name for your mods:

.. code-block:: cpp

   module yourID
   {
     ...
   }

Most scripts that are defined in a module will need to be refered to by their 'full type', that is ``module.id``\ , but this is a bit inconsistent as some places where a script block needs to be refered to require no module reference. For example, for an item, you can refer to it by its full type ``yourModule.yourItemID``.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-scripts`

**Possible Child Blocks:**

- :ref:`animation`
- :ref:`animationsmesh`
- :ref:`character_profession_definition`
- :ref:`character_trait_definition`
- :ref:`clock`
- :ref:`craftrecipe`
- :ref:`energy`
- :ref:`entity`
- :ref:`evolvedrecipe`
- :ref:`fixing`
- :ref:`fluid`
- :ref:`imports`
- :ref:`item`
- :ref:`mannequin`
- :ref:`model`
- :ref:`physicshitreaction`
- :ref:`physicsshape`
- :ref:`ragdoll`
- :ref:`sound`
- :ref:`template`
- :ref:`timedaction`
- :ref:`vehicle`
- :ref:`vehicleenginerpm`
- :ref:`xuiskin`


ID Properties
-------------

This block should have an ID.

