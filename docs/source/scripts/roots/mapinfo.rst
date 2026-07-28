.. _scripts-mapinfo:

ROOT-MapInfo
============

.. attribute:: Soft Override

   Unknown

.. attribute:: Is Root

   True

.. attribute:: No comma

   True

The ``map.info`` file is used to define the map's information. It is used by the game to display the map in the map selection screen and to load the map into the world.
It needs to be located in:

.. code-block::

   📁 media
       📁maps
           📁 <map folder>
               📄 map.info


ID
--

This block should have no ID.


Parameters
----------

.. _scripts-root-mapinfo-title:

title
^^^^^

.. attribute:: Type

   Unknown

Title of the map.


.. _scripts-root-mapinfo-description:

description
^^^^^^^^^^^

.. attribute:: Type

   Unknown

Description of the map.


.. _scripts-root-mapinfo-lots:

lots
^^^^

.. attribute:: Type

   Unknown

Refers to the world map the map will be loaded into. For a map which is inside the vanilla world map, use ``lots=Muldraugh, KY``.


.. _scripts-root-mapinfo-fixed2x:

fixed2x
^^^^^^^

.. attribute:: Type

   Unknown

Boolean which fixes rendering issues. Leave it as ``true`` if you are not sure.


.. _scripts-root-mapinfo-zoomx:

zoomX
^^^^^

.. attribute:: Type

   Unknown

Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.


.. _scripts-root-mapinfo-zoomy:

zoomY
^^^^^

.. attribute:: Type

   Unknown

Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.


.. _scripts-root-mapinfo-zooms:

zoomS
^^^^^

.. attribute:: Type

   Unknown

Zoom parameter used to define the position of the camera on the world map when chosing the map to spawn in.


.. _scripts-root-mapinfo-demovideo:

demoVideo
^^^^^^^^^

.. attribute:: Type

   Unknown

`Video file <https://pzwiki.net/wiki/File_formats#Video_format>`_ used to showcase the map when selecting it.


