.. _scripts-blendwhitelist:

BlendWhiteList
==============

:Soft Override: Unknown

BlendWhiteList defines a whitelist for fluids that the fluid can be blended with, while BlendBlackList defines a blacklist. By default those blocks are set whitelist, but you can add one of the available parameters to indicate whenever the block is a whitelist or a blacklist.

Fluids that are whitelisted/blacklisted can be identified either by their category via the use of a `categories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/categories.html>`_ child block, or by their name via the use of the `fluid <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#fluid>`_ parameter.


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`fluid <scripts-fluid>`

This block can have the following child blocks:

- :ref:`Categories <scripts-categories>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-blendwhitelist-whitelist:

.. attribute:: whitelist
   :noindex:

:Type: boolean

Indicates whenever blending with other fluids is allowed.


.. _scripts-blendwhitelist-blacklist:

.. attribute:: blacklist
   :noindex:

:Type: boolean

Indicates whenever blending with other fluids is disallowed.


.. _scripts-blendwhitelist-fluid:

.. attribute:: fluid
   :noindex:

:Type: array (array of string, separator: '/')

A list of fluids.


.. _scripts-blendwhitelist-category:

.. attribute:: category
   :noindex:

:Type: Unknown

Unclear what this is for since this is usually achieved with a `categories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/categories.html>`_ child block.


.. _scripts-blendwhitelist-filtertype:

.. attribute:: filterType
   :noindex:

:Type: Unknown

:Allowed values:    ``whitelist``

Just use `whitelist <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#whitelist>`_ or `blacklist <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#blacklist>`_.


