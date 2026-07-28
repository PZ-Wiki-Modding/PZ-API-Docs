.. _scripts-sandboxoptions:

ROOT-SandboxOptions
===================

.. attribute:: Soft Override

   Unknown

.. attribute:: Is Root

   True

.. attribute:: Root patterns

   
   * ``media\/sandbox-options\.txt$``

The root of a sandbox options file. The file should be stored in the following path:

.. code-block::

   📁 media
     📄 sandbox-options.txt

You can find more information about sandbox options `here <https://pzwiki.net/wiki/Sandbox_options>`_.


Hierarchy
---------

This block can have the following child blocks:

- :ref:`option <scripts-option>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-root-sandboxoptions-version:

VERSION
^^^^^^^

.. attribute:: Type

   Unknown

.. attribute:: Required

   True

.. attribute:: Allowed values

   
   * 1

The version of the handler of the sandbox options. Keep this equal to 1.


