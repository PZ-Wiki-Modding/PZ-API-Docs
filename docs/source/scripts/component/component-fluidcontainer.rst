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

    Type: float
    Default: 1.0

The fluid capacity of the container, the minimum value is ``0.05``.

.. _component-fluidcontainer-containername:

ContainerName
^^^^^^^^^^^^^

    Type: string
    Default: FluidContainer
    Useless: ✓

The name of the fluid container, seems to be unused. The name cannot have whitespaces, the game will sanitize it to remove them and show an error in the console about it.

.. _component-fluidcontainer-customdrinksound:

CustomDrinkSound
^^^^^^^^^^^^^^^^

    Type: string
    Default: DrinkingFromGeneric

Refers to a `sound block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_ to trigger when drinking.

.. _component-fluidcontainer-fillswithcleanwater:

FillsWithCleanWater
^^^^^^^^^^^^^^^^^^^

    Type: boolean
    Default: False

When set to true, the container will fill with clean water instead of tainted water when left outside in the rain.

.. _component-fluidcontainer-hiddenamount:

HiddenAmount
^^^^^^^^^^^^

    Type: boolean
    Default: False

When true, will hide the fluid quantity from the UI.

.. _component-fluidcontainer-initialpercent:

InitialPercent
^^^^^^^^^^^^^^

    Type: float
    Incompatible with: InitialPercentMin, InitialPercentMax

No description

.. _component-fluidcontainer-initialpercentmax:

InitialPercentMax
^^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0
    Incompatible with: InitialPercent

The minimum amount of fluid which will appear in this container.

.. _component-fluidcontainer-initialpercentmin:

InitialPercentMin
^^^^^^^^^^^^^^^^^

    Type: float
    Default: 0.0
    Incompatible with: InitialPercent

The maximum amount of fluid which will appear in this container.

.. _component-fluidcontainer-inputlocked:

InputLocked
^^^^^^^^^^^

    Type: boolean
    Default: False

Unused.

.. _component-fluidcontainer-opened:

Opened
^^^^^^

    Type: boolean
    Default: True

Unused.

.. _component-fluidcontainer-pickrandomfluid:

PickRandomFluid
^^^^^^^^^^^^^^^

    Type: boolean
    Default: False

When set to true, the container will pick one of the available fluids in the `Fluids <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/fluids.html>`_ child block at random when filling. If set to false, it will make every fluids appear.

.. _component-fluidcontainer-rainfactor:

RainFactor
^^^^^^^^^^

    Type: float
    Default: 0.0

Defines how much rain contributes to filling the container. A high value increases the rate of filling. A value of ``0.0`` means that rain will not fill the container, which is the default value of the parameter.

If the item is a weapon and ``RainFactor`` is set to a value above the default, when the player aims with the weapon it will empty it.

