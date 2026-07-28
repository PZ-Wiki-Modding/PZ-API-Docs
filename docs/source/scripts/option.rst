.. _scripts-option:

option
======

.. attribute:: Soft Override

   Unknown

Defines a custom sandbox option for a mod. You can find more information about sandbox options `here <https://pzwiki.net/wiki/Sandbox_options>`_.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`ROOT-SandboxOptions <scripts-root-sandboxoptions>`



ID
--

This block can have an ID.

.. attribute:: Optional

   False

.. attribute:: Can have spaces

   False


Parameters
----------

.. _scripts-option-type:

type
^^^^

.. attribute:: Type

   string

.. attribute:: Required

   True

.. attribute:: Allowed values

   
   * boolean
   * integer
   * double
   * string
   * enum

The type of the option.


.. _scripts-option-min:

min
^^^

.. attribute:: Type

   float

The minimum value the option can have. Only for integer and double types.


.. _scripts-option-max:

max
^^^

.. attribute:: Type

   float

The maximum value the option can have. Only for integer and double types.


.. _scripts-option-default:

default
^^^^^^^

.. attribute:: Type

   Unknown

The default value of the option. The type of the value must match the type of the option.


.. _scripts-option-page:

page
^^^^

.. attribute:: Type

   string

The sandbox option to add the option to. Can be a custom page.


.. _scripts-option-translation:

translation
^^^^^^^^^^^

.. attribute:: Type

   string

The translation key for the option's name. The translation key in the `Sandbox <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#sandbox>`_ translation file should have the prefix ``Sandbox_``.

For example, with the translation parameter as such:

.. code-block:: java

   translation = MyMod_MyOption

The translation key in the Sandbox translation file should be:

.. code-block:: json

   "Sandbox_MyMod_MyOption": "My Option"


