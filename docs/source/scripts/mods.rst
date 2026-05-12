.. _mods:

mods
====

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

**Valid Parent Blocks:**

- :ref:`root-default`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _mods-mod:

mod
^^^

    Type: string
    Can be duplicated: ✓

The mod ID of the mod to load, which can be found in the `mod.info <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root-modinfo.html>`_ file of the mod.

