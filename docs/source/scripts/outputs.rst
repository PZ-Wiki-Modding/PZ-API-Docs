.. _outputs:

outputs
=======

The ``outputs`` block defines the items that will be created when the recipe is finished. Outputs are listed one after the other and follow the format below:

.. code-block:: cpp

   outputs
   {

       /* simple item output */
       item quantity item,

       /* using mappers */
       item quantity mapper:mapperID,

       ...
   }

For example:

.. code-block:: cpp

   outputs
   {
       item 1 Base.Tissue,
       item 1 Base.ScratchTicket,
   }


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`craftrecipe`


ID Properties
-------------

This block should not have an ID.

