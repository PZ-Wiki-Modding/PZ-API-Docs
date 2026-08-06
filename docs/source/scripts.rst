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

Each parameter will contain the following information based on what is provided by the game and the currently documented data from `pz-scripts-data <https://github.com/PZ-Wiki-Modding/pz-scripts-data>`_:

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

Root Files
----------

.. toctree::
   :maxdepth: 4
   :titlesonly:
   :glob:

   scripts/roots/*


Table of Contents
-----------------

.. toctree::
   :maxdepth: 4
   :titlesonly:
   :glob:

   scripts/*
