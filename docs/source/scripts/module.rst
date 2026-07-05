.. _scripts-module:

module
======

:Soft Override: Unknown

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

This block can be a child of the following blocks:

- :ref:`ROOT-Scripts <scripts-root-scripts>`

This block can have the following child blocks:

- :ref:`model <scripts-model>`
- :ref:`entity <scripts-entity>`
- :ref:`ragdoll <scripts-ragdoll>`
- :ref:`evolvedrecipe <scripts-evolvedrecipe>`
- :ref:`energy <scripts-energy>`
- :ref:`physicsShape <scripts-physicsshape>`
- :ref:`clock <scripts-clock>`
- :ref:`timedAction <scripts-timedaction>`
- :ref:`physicsHitReaction <scripts-physicshitreaction>`
- :ref:`fixing <scripts-fixing>`
- :ref:`item <scripts-item>`
- :ref:`character_profession_definition <scripts-character_profession_definition>`
- :ref:`vehicle <scripts-vehicle>`
- :ref:`vehicleEngineRPM <scripts-vehicleenginerpm>`
- :ref:`template <scripts-template>`
- :ref:`animationsMesh <scripts-animationsmesh>`
- :ref:`soundTimeline <scripts-soundtimeline>`
- :ref:`animation <scripts-animation>`
- :ref:`fluid <scripts-fluid>`
- :ref:`character_trait_definition <scripts-character_trait_definition>`
- :ref:`sound <scripts-sound>`
- :ref:`xuiSkin <scripts-xuiskin>`
- :ref:`craftRecipe <scripts-craftrecipe>`
- :ref:`imports <scripts-imports>`
- :ref:`mannequin <scripts-mannequin>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


Parameters
----------

This block has no parameters.

