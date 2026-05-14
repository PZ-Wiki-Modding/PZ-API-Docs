.. _blendwhitelist:

BlendWhiteList
==============

BlendWhiteList defines a whitelist for fluids that the fluid can be blended with, while BlendBlackList defines a blacklist. By default those blocks are set whitelist, but you can add one of the available parameters to indicate whenever the block is a whitelist or a blacklist.

Fluids that are whitelisted/blacklisted can be identified either by their category via the use of a `categories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/categories.html>`_ child block, or by their name via the use of the `fluid <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#fluid>`_ parameter.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`fluid`

**Possible Child Blocks:**

- :ref:`categories`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _blendwhitelist-blacklist:

blacklist
^^^^^^^^^

    Type: boolean

Indicates whenever blending with other fluids is disallowed.

.. _blendwhitelist-category:

category
^^^^^^^^

    Type: Any

Unclear what this is for since this is usually achieved with a `categories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/categories.html>`_ child block.

.. _blendwhitelist-filtertype:

filterType
^^^^^^^^^^

    Type: Any

Just use `whitelist <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#whitelist>`_ or `blacklist <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/blendwhitelist.html#blacklist>`_.

Allowed values:

    - ``whitelist``

.. _blendwhitelist-fluid:

fluid
^^^^^

    Type: array (array of string, separator: '/')

A list of fluids.

.. _blendwhitelist-whitelist:

whitelist
^^^^^^^^^

    Type: boolean

Indicates whenever blending with other fluids is allowed.

