.. _option:

option
======

Defines a custom sandbox option for a mod.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`root-sandboxoptions`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _option-default:

default
^^^^^^^

:Type: Any
:Needs: ``type``

No description

.. _option-max:

max
^^^

:Type: float
:Needs: ``type`` = integer, double

The maximum value the option can have. Only for integer and double types.

.. _option-min:

min
^^^

:Type: float
:Needs: ``type`` = integer, double

The minimum value the option can have. Only for integer and double types.

.. _option-page:

page
^^^^

:Type: string

The sandbox option to add the option to. Can be a custom page.

.. _option-translation:

translation
^^^^^^^^^^^

:Type: string

The translation key for the option's name.

.. _option-type:

type
^^^^

:Type: string **(required)**

The type of the option.

Allowed values:

    - ``boolean``
    - ``integer``
    - ``double``
    - ``string``
    - ``enum``

