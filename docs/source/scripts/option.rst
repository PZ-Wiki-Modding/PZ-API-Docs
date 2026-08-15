.. _scripts-option:

option
======

:Soft Override: Unknown

Defines a custom sandbox option for a mod. You can find more information about sandbox options `here <https://pzwiki.net/wiki/Sandbox_options>`_.


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

.. _scripts-option-default:

.. attribute:: default
   :noindex:

:Type: Unknown

The default value of the option. The type of the value must match the type of the option.


.. _scripts-option-max:

.. attribute:: max
   :noindex:

:Type: float

The maximum value the option can have. Only for integer and double types.


.. _scripts-option-min:

.. attribute:: min
   :noindex:

:Type: float

The minimum value the option can have. Only for integer and double types.


.. _scripts-option-page:

.. attribute:: page
   :noindex:

:Type: translation

The sandbox option to add the option to. Can be a custom page.


.. _scripts-option-translation:

.. attribute:: translation
   :noindex:

:Type: translation

The translation key for the option's name. The translation key in the `Sandbox <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#sandbox>`_ translation file should have the prefix ``Sandbox_``.

For example, with the translation parameter as such:

.. code-block:: java

   translation = MyMod_MyOption

The translation key in the Sandbox translation file should be:

.. code-block:: json

   "Sandbox_MyMod_MyOption": "My Option"


.. _scripts-option-type:

.. attribute:: type
   :noindex:

:Type: string

:Required: True

:Allowed values:    ``boolean`` | ``double`` | ``enum`` | ``integer`` | ``string``

The type of the option.


