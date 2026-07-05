.. _scripts-physicsshape:

physicsShape
============

:Soft Override: Unknown

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

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


Parameters
----------

.. _scripts-physicsshape-mesh:

mesh
^^^^

:Type: string

The path to the model's mesh file, relative to the folder ``media/models_X``.


.. _scripts-physicsshape-translate:

translate
^^^^^^^^^

:Type: array (array of float, separator: ' ')

The position offset of the model, in the format ``x y z``.


.. _scripts-physicsshape-rotate:

rotate
^^^^^^

:Type: array (array of float, separator: ' ')

The rotation of the model, in the format ``x y z``.


