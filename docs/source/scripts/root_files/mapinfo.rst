.. _scripts-root-mapinfo:

ROOT-MapInfo
============

:Soft Override: Unknown

:Is Root: True

:No comma: True

:Root patterns:    ``media\/maps\/[\s\S]+\/map\.info$``

The ``map.info`` file is used to define the map's information. It is used by the game to display the map in the map selection screen and to load the map into the world.
It needs to be located in:

.. code-block::

   📁 media
       📁maps
           📁 <map folder>
               📄 map.info


Parameters
----------

.. _scripts-root-mapinfo-demovideo:

.. attribute:: demoVideo
   :noindex:

:Type: Unknown

`Video file <https://pzwiki.net/wiki/File_formats#Video_format>`_ used to showcase the map when selecting it.


.. _scripts-root-mapinfo-description:

.. attribute:: description
   :noindex:

:Type: Unknown

Description of the map.


.. _scripts-root-mapinfo-fixed2x:

.. attribute:: fixed2x
   :noindex:

:Type: Unknown

Boolean which fixes rendering issues. Leave it as ``true`` if you are not sure.


.. _scripts-root-mapinfo-lots:

.. attribute:: lots
   :noindex:

:Type: Unknown

Refers to the world map the map will be loaded into. For a map which is inside the vanilla world map, use ``lots=Muldraugh, KY``.


.. _scripts-root-mapinfo-title:

.. attribute:: title
   :noindex:

:Type: Unknown

Title of the map.


.. _scripts-root-mapinfo-zooms:

.. attribute:: zoomS
   :noindex:

:Type: Unknown

Zoom parameter used to define the position of the camera on the world map when chosing the map to spawn in.


.. _scripts-root-mapinfo-zoomx:

.. attribute:: zoomX
   :noindex:

:Type: Unknown

Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.


.. _scripts-root-mapinfo-zoomy:

.. attribute:: zoomY
   :noindex:

:Type: Unknown

Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.


