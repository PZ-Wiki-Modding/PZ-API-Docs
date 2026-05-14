.. _blendblacklist:

BlendBlackList
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

