.. _component-fluidcontainer:

component FluidContainer
========================

Adds a fluid container to an item


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`item`
- :ref:`entity`

**Possible Child Blocks:**

- :ref:`fluids`
- :ref:`whitelist`


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _component-fluidcontainer-capacity:

Capacity
^^^^^^^^

   Type: ``{'main': 'float'}``

The fluid capacity of the container, the minimum value is ``0.05``.

   Default: ``1.0``

.. _component-fluidcontainer-containername:

ContainerName
^^^^^^^^^^^^^

   Type: ``{'main': 'string'}``

The name of the fluid container, seems to be unused. The name cannot have whitespaces, the game will sanitize it to remove them and show an error in the console about it.

   Default: ``FluidContainer``

.. _component-fluidcontainer-customdrinksound:

CustomDrinkSound
^^^^^^^^^^^^^^^^

   Type: ``{'main': 'string'}``

Refers to a `sound block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_ to trigger when drinking.

   Default: ``DrinkingFromGeneric``

.. _component-fluidcontainer-fillswithcleanwater:

FillsWithCleanWater
^^^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

When set to true, the container will fill with clean water instead of tainted water when left outside in the rain.

   Default: ``False``

.. _component-fluidcontainer-hiddenamount:

HiddenAmount
^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

When true, will hide the fluid quantity from the UI.

   Default: ``False``

.. _component-fluidcontainer-initialpercent:

InitialPercent
^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

No description

.. _component-fluidcontainer-initialpercentmax:

InitialPercentMax
^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

The minimum amount of fluid which will appear in this container.

   Default: ``1.0``

.. _component-fluidcontainer-initialpercentmin:

InitialPercentMin
^^^^^^^^^^^^^^^^^

   Type: ``{'main': 'float'}``

The maximum amount of fluid which will appear in this container.

   Default: ``0.0``

.. _component-fluidcontainer-inputlocked:

InputLocked
^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

Unused.

   Default: ``False``

.. _component-fluidcontainer-opened:

Opened
^^^^^^

   Type: ``{'main': 'boolean'}``

Unused.

   Default: ``True``

.. _component-fluidcontainer-pickrandomfluid:

PickRandomFluid
^^^^^^^^^^^^^^^

   Type: ``{'main': 'boolean'}``

When set to true, the container will pick one of the available fluids in the `Fluids <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/fluids.html>`_ child block at random when filling. If set to false, it will make every fluids appear.

   Default: ``False``

.. _component-fluidcontainer-rainfactor:

RainFactor
^^^^^^^^^^

   Type: ``{'main': 'float'}``

Defines how much rain contributes to filling the container. A high value increases the rate of filling. A value of ``0.0`` means that rain will not fill the container, which is the default value of the parameter.

If the item is a weapon and ``RainFactor`` is set to a value above the default, when the player aims with the weapon it will empty it.

   Default: ``0.0``

