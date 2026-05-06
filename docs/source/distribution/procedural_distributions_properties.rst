Procedural distributions properties
===================================

Reference for all available properties that can be set on procedural distributions.

.. _procedural-distributions-property-noAutoAge:

noAutoAge
---------

No description available.

.. _procedural-distributions-property-fillRand:

fillRand
--------

No description available.

.. _procedural-distributions-property-maxMap:

maxMap
------

Integer value, limits the same item to a max amount (UNSURE).

.. _procedural-distributions-property-stashchance:

stashchance
-----------

Chance for the container to be a stash.

.. _procedural-distributions-property-dontSpawnAmmo:

dontSpawnAmmo
-------------

No description available.

.. _procedural-distributions-property-gunStorage:

gunStorage
----------

No description available.

.. _procedural-distributions-property-ignoreZombieDensity:

ignoreZombieDensity
-------------------

Ignores the zombie density impact on item spawn chance.

.. _procedural-distributions-property-cookFood:

cookFood
--------

No description available.

.. _procedural-distributions-property-canBurn:

canBurn
-------

Food cna be burnt (25% chance) or cooked.

.. _procedural-distributions-property-isTrash:

isTrash
-------

items spawn with lower condition, delta etc:


* HandWeapon get reduced item condition
* Items with head condition get reduced head condition
* Items with sharpness condition get reduced head condition
* DrainiableComboItem get reduced item uses (i.e. batteries)
* Impact on non-canned and edible (non can't eat) food:

  * Non-vermin, cookable and non-replacable on cooked will be either cooked or burnt (50% chance)
  * Non-rotten item will be rotten (75% chance) or have increased age (less fresh)
  * Have reduced food values

``isWorn`` containers will have clothing items with reduced condition, can be dirty (25% chance), bloody (1% chance) and/or have holes (25% chance).

``isTrash`` containers will have clothing items with reduced condition, can be wet (25% chance), dirty (95% chance), bloody (10% chance) and /or have holes (75% chance).

.. _procedural-distributions-property-isWorn:

isWorn
------

No description available.

.. _procedural-distributions-property-isRotten:

isRotten
--------

Non-rotten items will be rotten (75% chance) or have increased age (less fresh).

.. _procedural-distributions-property-onlyOne:

onlyOne
-------

Deprecated, a tag which can be found in distributions looks deprecated from the Java.

.. _procedural-distributions-property-isShop:

isShop
------

When not set to true:


* Can be a stash (related to ``stashChance``\ )
* DrainableComboItem get random amount of uses
* HandWeapon can have lower condition (40% chance)
* Items with head conditio nget reduced head condition (40% chance)
* Items with sharpness condition get reduced sharpness condition (40% chance)
* Bags get items inside them

.. _procedural-distributions-property-bags:

bags
----

Unclear what this does.

.. _procedural-distributions-property-junk:

junk
----

No description available.

.. _procedural-distributions-property-items:

items
-----

Holds the various items that will spawn in this procedural distribution list. The format should be as follow:

.. code-block:: lua

   items = {
     "item1", roll_chance1,
     "item2", roll_chance2,
     "item3", roll_chance3,
     ...
   }

.. _procedural-distributions-property-rolls:

rolls
-----

Number of rolls to perform on the procedural distribution list. This roll amount is applied for each item entries of this procedural distribution list. So if there are 5 items and 2 rolls, the game will roll 2 times for each of the 5 items individually, so 10 rolls in total.

