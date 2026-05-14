.. _physicsshape:

physicsShape
============

Defines a 3D object's physical shape to be used as a world object.

For example:

.. code-block:: cpp

   module YourModule {
     physicsShape ramp20segment5w {
         mesh = physics/ramp20|Segment5,
         translate = 4.0 0.0 0.0,
         rotate = 0.0 270.0 0.0,
     }
   }


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _physicsshape-mesh:

mesh
^^^^

:Type: string

The path to the model's mesh file, relative to the folder ``media/models_X``.

.. _physicsshape-rotate:

rotate
^^^^^^

:Type: array

The rotation of the model, in the format ``x y z``.

.. _physicsshape-translate:

translate
^^^^^^^^^

:Type: array

The position offset of the model, in the format ``x y z``.

