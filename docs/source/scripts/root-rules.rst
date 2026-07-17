.. _scripts-root-rules:

ROOT-Rules
==========

:Soft Override: Unknown
:Is Root: True

The ``Rules.txt`` file is used in the `mapping tools <https://pzwiki.net/wiki/Mapping#Mapping_tools>`_ to define new `BMP to TMX <https://pzwiki.net/wiki/BMP_to_TMX>`_ conversion rules. You can store this file anywhere on your computer and you need to reference it in the BMP Tool settings.

A reference image containing the exact pixel colors you need to use for your BMP can be found `here <https://github.com/Unofficial-PZ-Mapping-Discord/B42-Colors/tree/main>`_.


Hierarchy
---------

This block can have the following child blocks:

- :ref:`rule <scripts-rule>`
- :ref:`alias <scripts-alias>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-root-rules-version:

version
^^^^^^^

:Type: integer

Version of the rules file. Should be 1 for now.


