.. _scripts-option:

option
======

:Soft Override: Unknown

Defines a custom sandbox option for a mod.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`ROOT-SandboxOptions <scripts-root-sandboxoptions>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


Parameters
----------

.. _scripts-option-type:

type
^^^^

:Type: string
:Required: True
:Allowed values: 
* ``boolean``
* ``integer``
* ``double``
* ``string``
* ``enum``

The type of the option.


.. _scripts-option-min:

min
^^^

:Type: float

The minimum value the option can have. Only for integer and double types.


.. _scripts-option-max:

max
^^^

:Type: float

The maximum value the option can have. Only for integer and double types.


.. _scripts-option-default:

default
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-option-page:

page
^^^^

:Type: string

The sandbox option to add the option to. Can be a custom page.


.. _scripts-option-translation:

translation
^^^^^^^^^^^

:Type: string

The translation key for the option's name.


