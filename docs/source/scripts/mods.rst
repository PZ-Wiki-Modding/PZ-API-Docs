.. _scripts-mods:

mods
====

:Soft Override: Unknown

A list of mods in the `default.txt <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-default.html>`_ file. The `mod ID <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-modinfo.html#root-modinfo-id>`_ should be used to reference the mods.

It should use the following syntax:

.. code-block::

   mods
   {
     mod = mod1,
     mod = mod2,
     ...
   }


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`ROOT-Default <scripts-root-default>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-mods-mod:

mod
^^^

:Type: string

The mod ID of the mod to load, which can be found in the `mod.info <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-modinfo.html>`_ file of the mod.


