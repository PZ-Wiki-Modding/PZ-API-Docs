.. _scripts-component-fluidcontainer:

component FluidContainer
========================

:Soft Override: Unknown

:Is Variant of: :ref:`component <scripts-component>`

Adds a fluid container to an item


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`entity <scripts-entity>`
- :ref:`item <scripts-item>`

This block can have the following child blocks:

- :ref:`Fluids <scripts-fluids>`
- :ref:`whitelist <scripts-whitelist>`



ID
--

This block should have no ID.


Parameters
----------

.. _scripts-component-fluidcontainer-capacity:

.. attribute:: Capacity
   :noindex:

:Type: float

:Default: ``1.0``

The fluid capacity of the container, the minimum value is ``0.05``.


.. _scripts-component-fluidcontainer-containername:

.. attribute:: ContainerName
   :noindex:

:Type: string

:Is useless: True

:Default: ``FluidContainer``

The name of the fluid container, seems to be unused. The name cannot have whitespaces, the game will sanitize it to remove them and show an error in the console about it.


.. _scripts-component-fluidcontainer-customdrinksound:

.. attribute:: CustomDrinkSound
   :noindex:

:Type: string

:Default: ``DrinkingFromGeneric``

Refers to a `sound block <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html>`_ to trigger when drinking.


.. _scripts-component-fluidcontainer-fillswithcleanwater:

.. attribute:: FillsWithCleanWater
   :noindex:

:Type: boolean

:Default: ``False``

When set to true, the container will fill with clean water instead of tainted water when left outside in the rain.


.. _scripts-component-fluidcontainer-hiddenamount:

.. attribute:: HiddenAmount
   :noindex:

:Type: boolean

:Default: ``False``

When true, will hide the fluid quantity from the UI.


.. _scripts-component-fluidcontainer-initialpercent:

.. attribute:: InitialPercent
   :noindex:

:Type: float

:Incompatible with:    :ref:`InitialPercentMax <scripts-component-fluidcontainer-initialpercentmax>` | :ref:`InitialPercentMin <scripts-component-fluidcontainer-initialpercentmin>`

No description provided.


.. _scripts-component-fluidcontainer-initialpercentmax:

.. attribute:: InitialPercentMax
   :noindex:

:Type: float

:Default: ``1.0``

:Incompatible with:    :ref:`InitialPercent <scripts-component-fluidcontainer-initialpercent>`

The minimum amount of fluid which will appear in this container.


.. _scripts-component-fluidcontainer-initialpercentmin:

.. attribute:: InitialPercentMin
   :noindex:

:Type: float

:Default: ``0.0``

:Incompatible with:    :ref:`InitialPercent <scripts-component-fluidcontainer-initialpercent>`

The maximum amount of fluid which will appear in this container.


.. _scripts-component-fluidcontainer-inputlocked:

.. attribute:: InputLocked
   :noindex:

:Type: boolean

:Default: ``False``

Unused.


.. _scripts-component-fluidcontainer-opened:

.. attribute:: Opened
   :noindex:

:Type: boolean

:Default: ``True``

Unused.


.. _scripts-component-fluidcontainer-pickrandomfluid:

.. attribute:: PickRandomFluid
   :noindex:

:Type: boolean

:Default: ``False``

When set to true, the container will pick one of the available fluids in the `Fluids <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/fluids.html>`_ child block at random when filling. If set to false, it will make every fluids appear.


.. _scripts-component-fluidcontainer-rainfactor:

.. attribute:: RainFactor
   :noindex:

:Type: float

:Default: ``0.0``

Defines how much rain contributes to filling the container. A high value increases the rate of filling. A value of ``0.0`` means that rain will not fill the container, which is the default value of the parameter.

If the item is a weapon and ``RainFactor`` is set to a value above the default, when the player aims with the weapon it will empty it.


