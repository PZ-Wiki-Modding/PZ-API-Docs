.. _scripts-root-tmxconfig:

ROOT-TMXconfig
==============

:Soft Override: Unknown

:Is Root: True

:No comma: True

:Root patterns:    ``TMXconfig\.txt$``

The ``TMXconfig.txt`` file is used to configure the default layers which will be created in the TMX file.


Hierarchy
---------

This block can have the following child blocks:

- :ref:`layers <scripts-layers>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-root-tmxconfig-revision:

.. attribute:: revision
   :noindex:

:Type: integer

Revision of the TMXconfig file. Keep it to 11 for now.


.. _scripts-root-tmxconfig-version:

.. attribute:: version
   :noindex:

:Type: integer

Version of the TMXconfig file. Should be 1 for now.


