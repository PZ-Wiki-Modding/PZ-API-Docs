.. _item:

item
====

The item block is used to create items in the game, from weapons to food and clothing. The parameters available in this block mostly depend on the type of item you are creating, set with `ItemType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_.

To get started, create a simple item structure by setting that parameter up correctly, then add more parameters as you need. For example, for a normal item:

.. code-block:: cpp

   module yourModule
   {
     item yourID
     {
       ItemType = base:normal,
       ...
     }
   }

To add a name to display for your item, you need to add the item full type, that is its ``module.id``\ , inside the `ItemName <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#itemname>`_ translation file. Taking the example from above, your translation file would be:

.. code-block:: json

   {
     "yourModule.yourID": "Your Item Name"
   }

This block can be soft overridden in scripts.


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`

**Possible Child Blocks:**

- :ref:`component`
- :ref:`component-contextmenuconfig`
- :ref:`component-durability`
- :ref:`component-fluidcontainer`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _item-acceptitemfunction:

AcceptItemFunction
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-acceptmediatype:

AcceptMediaType
^^^^^^^^^^^^^^^

    Type: integer
    Default: -1

No description

.. _item-activateditem:

ActivatedItem
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-aimingmod:

AimingMod
^^^^^^^^^

    Type: Any

No description

.. _item-aimingperkcritmodifier:

AimingPerkCritModifier
^^^^^^^^^^^^^^^^^^^^^^

    Type: integer

See :ref:`item-criticalchance` for more details.

.. _item-aimingperkhitchancemodifier:

AimingPerkHitChanceModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: float

See :ref:`item-hitchance` for more details.

.. _item-aimingperkminanglemodifier:

AimingPerkMinAngleModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: float

See :ref:`item-minangle` for more details.

.. _item-aimingperkrangemodifier:

AimingPerkRangeModifier
^^^^^^^^^^^^^^^^^^^^^^^

    Type: float

See :ref:`item-maxrange` for more details.

.. _item-aimingtime:

Aimingtime
^^^^^^^^^^

    Type: integer

`Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtime>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtimemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. The attachments directly add or subtract their `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtimemodifier>`_ to the aiming delay.

It controls the aim-settling delay, the aiming delay counter that must tick down to 0 before the weapon is "settled". Lower values means faster target reacquisition after each shots. The primary "how snappy does this gun feel" lever for semi-automatic guns. It tick down the aiming via the following formula:

.. code-block:: java

   rate = 0.625 x gameSpeed x (1 + 0.05 x AimingLevel + (Marksman ? 0.1 : 0))

The `marksman <https://pzwiki.net/wiki/Marksman>`_ trait being no longer accessible in the recent versions of the game, the condition involving it will never be reached.

..

   Note:
   This formula might not be fully accurate as `time deltas <https://github.com/demiurgeQuantified/PZModdingGuides/blob/main/guides/GameTime.md>`_ don't appear in the formula.


While ``aimingDelay > 0``\ , both `hit chance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-hitchance>`_ and `critical chance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-criticalchance>`_ take an aim-delay penalty proportional to the remaining delay. The countdown only starts after ``recoilDelay`` has recovered, so high `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ directly delays when ``AimingTime`` begins ticking.

On each shots or equip, the aiming delay will be increased or reduced, being impacted by aiming while in a `vehicle <https://pzwiki.net/wiki/Vehicle>`_\ , being reduced by the trait `Dextrous <https://pzwiki.net/wiki/Dextrous>`_ or increased by `All Thumbs <https://pzwiki.net/wiki/All_Thumbs>`_. The following formula is used:

.. code-block:: java

   aimingDelay = AimingTime
           * (Dextrous ? 0.8 : AllThumbs ? 1.2 : 1.0)
           * (in vehicle ? 1.5 : 1.0)

.. _item-aimingtimemodifier:

AimingTimeModifier
^^^^^^^^^^^^^^^^^^

    Type: integer

See :ref:`item-aimingtime` for more details.

.. _item-aimreleasesound:

AimReleaseSound
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-alarmsound:

AlarmSound
^^^^^^^^^^

    Type: Any

No description

.. _item-alcoholic:

Alcoholic
^^^^^^^^^

    Type: Any

No description

.. _item-alcoholpower:

AlcoholPower
^^^^^^^^^^^^

    Type: Any

No description

.. _item-alwaysknockdown:

AlwaysKnockdown
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-alwayswelcomegift:

AlwaysWelcomeGift
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-ammobox:

AmmoBox
^^^^^^^

    Type: string (block: :ref:`item`, with :ref:`module`)

No description

.. _item-ammotype:

AmmoType
^^^^^^^^

    Type: string

`AmmoType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-ammotype>`_ indicates what ammo is consumed when shooting, but it also determines tracer and hit-reaction sound lookups. The value needs to reference the `registries <https://pzwiki.net/wiki/Registries>`_ entry of the ammo you want to use. The vanilla ammunition types which are available by default are:


* ``base:bullets_3030``
* ``base:bullets_308``
* ``base:bullets_357``
* ``base:bullets_38``
* ``base:bullets_44``
* ``base:bullets_45``
* ``base:bullets_556``
* ``base:bullets_9mm``
* ``base:cap_gun_cap``
* ``base:shotgun_shells``

`AmmoBox <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-ammobox>`_ is used to indicate the type of ammo box associated to the weapon. This is mostly used to spawn this type of ammo box alongside the gun.

`MagazineType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-magazinetype>`_ is used to set the magazine item the gun uses. If not provided, then the gun doesn't use a magazine item and loads rounds individually. `MaxAmmo <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxammo>`_ is used to set the capacity of either the magazine item or the gun.

`WeaponReloadType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weaponreloadtype>`_ is used to select the reload workflow of the gun. Notably affects rack-after-shot, insertion style and animations. The provided value references the `variable condition <https://pzwiki.net/wiki/Conditions>`_ ``WeaponReloadType`` in `AnimNodes <https://pzwiki.net/wiki/AnimNodes>`_. The game has the following values available by default:


* handgun
* shotgun
* boltactionnomag
* boltaction
* revolver
* doublebarrelshotgun
* doublebarrelshotgunsawn

A custom ``WeaponReloadType`` can be used if the relevant animations and condition logic are properly set up in a custom `AnimNode <https://pzwiki.net/wiki/AnimNodes>`_.

.. _item-anglefalloff:

AngleFalloff
^^^^^^^^^^^^

    Type: Any

No description

.. _item-animalfeedtype:

AnimalFeedType
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-attachmentreplacement:

AttachmentReplacement
^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-attachmentsprovided:

AttachmentsProvided
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-attachmenttype:

AttachmentType
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-badcold:

BadCold
^^^^^^^

    Type: Any

No description

.. _item-badinmicrowave:

BadInMicrowave
^^^^^^^^^^^^^^

    Type: Any

Used to set whether this item will cause a fire when put in a microwave.

.. _item-bandagepower:

BandagePower
^^^^^^^^^^^^

    Type: Any

No description

.. _item-basespeed:

BaseSpeed
^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-basevolumerange:

BaseVolumeRange
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-bitedefense:

BiteDefense
^^^^^^^^^^^

    Type: Any

No description

.. _item-bloodlocation:

BloodLocation
^^^^^^^^^^^^^

    Type: array (array of string, separator: ';')

No description

Allowed values:

    - ``Apron``
    - ``ShirtNoSleeves``
    - ``JumperNoSleeves``
    - ``Shirt``
    - ``ShirtLongSleeves``
    - ``Jumper``
    - ``Jacket``
    - ``LongJacket``
    - ``ShortsShort``
    - ``Trousers``
    - ``Shoes``
    - ``FullHelmet``
    - ``Bag``
    - ``Hands``
    - ``Head``
    - ``Neck``
    - ``Groin``
    - ``UpperBody``
    - ``LowerBody``
    - ``LowerLegs``
    - ``UpperLegs``
    - ``LowerArms``
    - ``UpperArms``
    - ``Hand_L``
    - ``Hand_R``
    - ``ForeArm_L``
    - ``ForeArm_R``
    - ``UpperArm_L``
    - ``UpperArm_R``
    - ``UpperLeg_L``
    - ``UpperLeg_R``
    - ``LowerLeg_L``
    - ``LowerLeg_R``
    - ``Foot_L``
    - ``Foot_R``

.. _item-bodylocation:

BodyLocation
^^^^^^^^^^^^

    Type: Any

Used to define which location on the human character this clothing item can be worn.

.. _item-book_subject:

book_subject
^^^^^^^^^^^^

    Type: Any

No description

.. _item-boredomchange:

BoredomChange
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-brakeforce:

brakeForce
^^^^^^^^^^

    Type: Any

No description

.. _item-breaksound:

BreakSound
^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-bringtobearsound:

BringToBearSound
^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-bulletdefense:

BulletDefense
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-bullethitarmoursound:

BulletHitArmourSound
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-calories:

Calories
^^^^^^^^

    Type: Any

No description

.. _item-canattach:

CanAttach
^^^^^^^^^

    Type: Any

No description

.. _item-canbandage:

CanBandage
^^^^^^^^^^

    Type: Any

No description

.. _item-canbarricade:

CanBarricade
^^^^^^^^^^^^

    Type: Any

No description

.. _item-canbeequipped:

CanBeEquipped
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-canbeplaced:

CanBePlaced
^^^^^^^^^^^

    Type: Any

No description

.. _item-canberemote:

CanBeRemote
^^^^^^^^^^^

    Type: Any

No description

.. _item-canbereused:

CanBeReused
^^^^^^^^^^^

    Type: Any

No description

.. _item-canbewrite:

CanBeWrite
^^^^^^^^^^

    Type: Any

No description

.. _item-candetach:

CanDetach
^^^^^^^^^

    Type: Any

No description

.. _item-canhaveholes:

CanHaveHoles
^^^^^^^^^^^^

    Type: boolean
    Default: True

Used to define whenever this item can get holes in it.

.. _item-cannedfood:

CannedFood
^^^^^^^^^^

    Type: Any

No description

.. _item-canstack:

CanStack
^^^^^^^^

    Type: Any

No description

.. _item-canstorewater:

CanStoreWater
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-cantattackwithlowestendurance:

CantAttackWithLowestEndurance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-cantbeconsolided:

cantBeConsolided
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-cantbefrozen:

CantBeFrozen
^^^^^^^^^^^^

    Type: Any

No description

.. _item-canteat:

CantEat
^^^^^^^

    Type: Any

No description

.. _item-capacity:

Capacity
^^^^^^^^

    Type: integer
    Default: -1

No description

.. _item-carbohydrates:

Carbohydrates
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-categories:

Categories
^^^^^^^^^^

    Type: Any

No description

.. _item-chancetofall:

ChanceToFall
^^^^^^^^^^^^

    Type: Any

No description

.. _item-chancetospawndamaged:

ChanceToSpawnDamaged
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-clicksound:

ClickSound
^^^^^^^^^^

    Type: string (block: :ref:`sound`)
    Default: Stormy9mmClick

No description

.. _item-clipsize:

ClipSize
^^^^^^^^

    Type: Any

No description

.. _item-closekillmove:

CloseKillMove
^^^^^^^^^^^^^

    Type: Any

Used to whenever this weapon can be used to do a close kill move, like knives to assassinate in the back.

.. _item-closesound:

CloseSound
^^^^^^^^^^

    Type: Any

No description

.. _item-clothingextrasubmenu:

ClothingExtraSubmenu
^^^^^^^^^^^^^^^^^^^^

    Type: Any

See :ref:`item-clothingitem` for more details.

.. _item-clothingitem:

ClothingItem
^^^^^^^^^^^^

    Type: Any

``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.

``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.

.. _item-clothingitemextra:

ClothingItemExtra
^^^^^^^^^^^^^^^^^

    Type: Any

See :ref:`item-clothingitem` for more details.

.. _item-clothingitemextraoption:

ClothingItemExtraOption
^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

See :ref:`item-clothingitem` for more details.

.. _item-colorblue:

ColorBlue
^^^^^^^^^

    Type: integer
    Default: 255

No description

.. _item-colorgreen:

ColorGreen
^^^^^^^^^^

    Type: integer
    Default: 255

No description

.. _item-colorred:

ColorRed
^^^^^^^^

    Type: integer
    Default: 255

No description

.. _item-combatspeedmodifier:

CombatSpeedModifier
^^^^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-conditionaffectscapacity:

ConditionAffectsCapacity
^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

Set whenever condition of the item can impact the capacity value of the container.

.. _item-conditionlowerchanceonein:

ConditionLowerChanceOneIn
^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: integer
    Default: 10

`ConditionLowerChanceOneIn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-conditionlowerchanceonein>`_ impacts the durability of the item, reducing the value
used to calculate the chance by doing ``chance = 1/ConditionLowerChanceOneIn``\ ,
which means increasing this parameter value will reduce the chance to damage the
item.

`ConditionMax <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-conditionmax>`_ sets the total durability pool, starting condition and repair ceiling. Make these two parameters high for robust military rifles, and low for a cheap civilian gun.

.. _item-conditionloweroffroad:

ConditionLowerOffroad
^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-conditionlowerstandard:

ConditionLowerStandard
^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-conditionmax:

ConditionMax
^^^^^^^^^^^^

    Type: integer
    Default: 10

No description

.. _item-consolidateoption:

ConsolidateOption
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-cookingsound:

CookingSound
^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

Custom sound to play when cooking this item.

.. _item-corpsesicknessdefense:

CorpseSicknessDefense
^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-cosmetic:

Cosmetic
^^^^^^^^

    Type: Any

No description

.. _item-count:

Count
^^^^^

    Type: integer
    Default: 1

The parameter is unused in the game scripts, unclear what it is used for.

.. _item-critdmgmultiplier:

CritDmgMultiplier
^^^^^^^^^^^^^^^^^

    Type: float
    Default: 2.0

Multiplier applied to the damage of a hit if it is a critical hit, applied inside `IsoGameCharacter.Hit() <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html#Hit(zombie.inventory.types.HandWeapon,zombie.characters.IsoGameCharacter,float,boolean,float,boolean>`_\ ). Two types of crits can trigger:


* A normal crit: ``damage *= max(2.0, CritDmgMultiplier)``
* Aim-at-floor stomp (melee only): ``damage *= max(5.0, CritDmgMultiplier)``

The default value of the ``HandWeapon`` class is ``2.0``. Values of ``3.0`` to ``5.0`` visibly spike crit damage while values above ``5.0`` also start boosting stomps.

.. _item-criticalchance:

CriticalChance
^^^^^^^^^^^^^^

    Type: float
    Default: 20.0

`CriticalChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-criticalchance>`_ sets the base critical hit chance of the weapon. The final ``CriticalChance`` value after all applied bonuses and penalties have been applied is compared on a 0-100 roll.

Below is a table listing the different elements which can influence the critical hit chance of a weapon:

.. list-table::
   :header-rows: 1

   * - Element
     - Type
     - Description
     - Formula
   * - `AimingPerkCritModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingperkcritmodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's critical hit chance by adding the following to the ``CriticalChance`` value.
     - ``CriticalChance += AimingPerkCritModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result. The aim delay penalty depends on `Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtime>`_
     - ``CriticalChance += max(sightlessBonus - sightlessAimDelayPenalty, sightWindowBonus - sightWindowAimDelayPenalty)``
   * - Moodles penalty
     - Player condition
     - Being panicked, stressed, tired, drunk or lacking endurance will all negatively impact the ``CriticalChance``.
     - ``CriticalChance -= moodlesPenalty``
   * - Weather penalty
     - Environment
     - Wind, rain, fog, low-light will all negatively impact the ``CriticalChance``.
     - ``CriticalChance -= weatherPenalty``
   * - Movement penalty
     - Player condition
     - The shooter speed and the distance will negatively impact the ``CriticalChance``.
     - ``CriticalChance -= movementPenalty``
   * - `Marksman trait <https://pzwiki.net/wiki/Marksman>`_
     - Player condition
     - This condition can never be reached as the Marksman trait no longer exists.
     - ``CriticalChance += 10``


For PvP targets, the entire formula is bypassed and `StopPower <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-stoppower>`_ is used instead. ``StopPower`` is never used against non-player targets.

.. code-block::

   CriticalChance = StopPower * ( 1 + Aiming level / 15)

``CriticalChance`` sets the floor for unskilled players while ``AimingPerkCritModifier`` rewards more or less the character ability to aim. High modified and low base chance means the weapon is a skill-gated crit machine, making the weapon a sort of "experts" weapon.

.. _item-customcontextmenu:

CustomContextMenu
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-customeatsound:

CustomEatSound
^^^^^^^^^^^^^^

    Type: Any
    Can be empty: ✓

Custom sound to play when eating or drinking this item, refers to the ID of a sound script. Set to an empty string to disable any sound from playing.

.. _item-cyclicratemultiplier:

CyclicRateMultiplier
^^^^^^^^^^^^^^^^^^^^

    Type: float
    Range: Min: 0.0
    Default: 1.0

Only in ``Auto`` `fire mode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemode>`_. Drives the full-auto animation cycle rate via the ``autoShootSpeed`` `animation variable <https://pzwiki.net/wiki/Conditions>`_.

A higher value means more shots per second. In ``Single`` mode this field is ignored and shot speed comes from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ and `Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtime>`_ instead.

Increase for SMG feel and decrease for heavy LMG feel.

.. _item-damagecategory:

DamageCategory
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-damagemakehole:

DamageMakeHole
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-dangerousuncooked:

DangerousUncooked
^^^^^^^^^^^^^^^^^

    Type: boolean

If true, the item will cause food poisoning when eaten raw. Used for example for raw meat. The `iron gut <https://pzwiki.net/wiki/Iron_Gut>`_ trait will stop you from getting sick from eating a raw food with the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-tags>`_ ``Egg``. The severity of the food poisoning is not impacted by traits or other criteria, only by the quantity of food you eat.

.. _item-daysfresh:

DaysFresh
^^^^^^^^^

    Type: integer
    Default: 1000000000

`DaysFresh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daysfresh>`_ sets how many days this food item will stay fresh with default sandbox settings. `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daystotallyrotten>`_ sets how many days this food item will take to rot.

`Icon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-icon>`_ provides the ability to set a different icon for the rotten and stale version of the food.

.. _item-daystotallyrotten:

DaysTotallyRotten
^^^^^^^^^^^^^^^^^

    Type: integer
    Default: 1000000000

See :ref:`item-daysfresh` for more details.

.. _item-digitalpadlock:

DigitalPadlock
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-digtype:

DigType
^^^^^^^

    Type: Any

No description

.. _item-disappearonuse:

DisappearOnUse
^^^^^^^^^^^^^^

    Type: boolean
    Default: True

No description

.. _item-discomfortmodifier:

DiscomfortModifier
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-displaycategory:

DisplayCategory
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-displayname:

DisplayName
^^^^^^^^^^^

    Type: Any

Sets the name of the item which will be displayed in-game. It's recommended to use a translation entry for this parameter to allow localization of the item name.

.. warning::

   **Deprecated** (since version 42.13.0)

   Naming an item should be done with a translation entry. See the `wiki <https://pzwiki.net/wiki/DisplayName>`_ page for more information.

.. _item-doordamage:

DoorDamage
^^^^^^^^^^

    Type: integer
    Range: Min: 1
    Default: 1

Damage dealt to doors, windows, barricades and some vehicle/object hits. The damage to doors cannot go lower than 1, even in the formulas it is clamped to a minimum of 1. The formula used to retrieve the damage to doors is:

.. code-block::

   damage = max(1, DoorDamage * sharpness multiplier)

More parameters will impact the door damage based on where it is used.

.. _item-doorhitsound:

DoorHitSound
^^^^^^^^^^^^

    Type: string
    Default: BaseballBatHit

No description

.. _item-doubleclickrecipe:

DoubleClickRecipe
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-dropsound:

DropSound
^^^^^^^^^

    Type: string

No description

.. _item-eattime:

Eattime
^^^^^^^

    Type: Any

No description

.. _item-eattype:

EatType
^^^^^^^

    Type: Any

No description

.. _item-ejectammosound:

EjectAmmoSound
^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-ejectammostartsound:

EjectAmmoStartSound
^^^^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-ejectammostopsound:

EjectAmmoStopSound
^^^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-endurancechange:

enduranceChange
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-endurancemod:

EnduranceMod
^^^^^^^^^^^^

    Type: float
    Default: 1.0

See :ref:`item-useendurance` for more details.

.. _item-engineloudness:

engineLoudness
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-equippednosprint:

EquippedNoSprint
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-equipsound:

EquipSound
^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-evolvedrecipe:

EvolvedRecipe
^^^^^^^^^^^^^

    Type: Any

List of evolved recipes this item can be used in.

.. _item-evolvedrecipename:

EvolvedRecipeName
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-explosionduration:

ExplosionDuration
^^^^^^^^^^^^^^^^^

    Type: integer

See :ref:`item-explosionrange` for more details.

.. _item-explosionpower:

ExplosionPower
^^^^^^^^^^^^^^

    Type: integer

If set above 0, the explosion will burn tiles and set fire to them based on the provided `fireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_

.. _item-explosionrange:

ExplosionRange
^^^^^^^^^^^^^^

    Type: integer

`FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_ out of 100 is a chance of the explosion to set on fire tiles and burn characters in the `ExplosionRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionrange>`_. A value above 100 means the explosion will always set on fire tiles and burn characters, while a value of 0 means it will never set on fire tiles nor burn characters. Each tiles in the explosion range will run the `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_ check independently, so a value of 50 means that on average half of the tiles in the explosion range will be set on fire.

`SmokeRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-smokerange>`_ sets the range of the smoke effect. Squares in this range also can be set on fire individually based on `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_.

`FireRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firerange>`_ will set every tiles in the provided range on fire.

`FireStartingEnergy <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingenergy>`_ is an extra check added on top of all of these whenever a fire is attempted to be started. Will set the energy of the fire which impacts how strong is is. A value of 0 means no fire is started. Vegetation tiles provide a net bonus of 50 in energy to the fire being created. The created fire will have a life expectency between 300 and 600 (unclear on the units).

`ExplosionSound <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionsound>`_ can be used to set the sound played when the explosion happens, while `ExplosionDuration <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionduration>`_ can be used to set the duration of the explosion effect, which is especially useful for smoke bombs.

.. _item-explosionsound:

ExplosionSound
^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

See :ref:`item-explosionrange` for more details.

.. _item-explosiontimer:

ExplosionTimer
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-fabrictype:

FabricType
^^^^^^^^^^

    Type: Any

No description

.. _item-fatiguechange:

fatigueChange
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-fillfromdispensersound:

FillFromDispenserSound
^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-fillfromlakesound:

FillFromLakeSound
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-fillfromtapsound:

FillFromTapSound
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-fillfromtoiletsound:

FillFromToiletSound
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-firefuelratio:

FireFuelRatio
^^^^^^^^^^^^^

    Type: Any
    Useless: ✓

No description

.. _item-firemode:

FireMode
^^^^^^^^

    Type: string

`FireModePossibilities <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemodepossibilities>`_ lists the available fire modes of the weapon, and the player can automatically switch between them with the relevant keybind. `FireMode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemode>`_ sets the default fire mode of the weapon, which is the one it will spawn with.

The vanilla fire modes are:


* ``Single``
* ``Auto``

Other values are not supported by the game and will be considered as ``Single``.

.. _item-firemodepossibilities:

FireModePossibilities
^^^^^^^^^^^^^^^^^^^^^

    Type: array (array of string, separator: '/')

See :ref:`item-firemode` for more details.

.. _item-firerange:

FireRange
^^^^^^^^^

    Type: Any

See :ref:`item-explosionrange` for more details.

.. _item-firestartingchance:

FireStartingChance
^^^^^^^^^^^^^^^^^^

    Type: integer

See :ref:`item-explosionrange` for more details.

.. _item-firestartingenergy:

FireStartingEnergy
^^^^^^^^^^^^^^^^^^

    Type: integer

No description

.. _item-fishinglure:

FishingLure
^^^^^^^^^^^

    Type: Any

No description

.. _item-flureduction:

fluReduction
^^^^^^^^^^^^

    Type: Any

No description

.. _item-foodsicknesschange:

FoodSicknessChange
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-foodtype:

FoodType
^^^^^^^^

    Type: Any

No description

.. _item-goodhot:

GoodHot
^^^^^^^

    Type: Any

No description

.. _item-guntype:

GunType
^^^^^^^

    Type: Any

No description

.. _item-havechamber:

HaveChamber
^^^^^^^^^^^

    Type: boolean
    Default: True

Whether the weapon has a chamber that can hold a round in addition to its magazine.

.. _item-headcondition:

HeadCondition
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-headconditionlowerchancemultiplier:

HeadConditionLowerChanceMultiplier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-headconditionmax:

HeadConditionMax
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-hearingmodifier:

HearingModifier
^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-herbalisttype:

HerbalistType
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-hidden:

Hidden
^^^^^^

    Type: Any

No description

.. _item-hitanglemod:

HitAngleMod
^^^^^^^^^^^

    Type: Any

No description

.. _item-hitchance:

HitChance
^^^^^^^^^

    Type: integer

`HitChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-hitchance>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `HitChanceModified <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-hitchancemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

The initial hitchance is determined by the following configuration:

.. code-block::

   HitChance = min(HitChance, CombatConfigKey.MAXIMUM_START_TO_HIT_CHANCE)

`MAXIMUM_START_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MAXIMUM_START_TO_HIT_CHANCE>`_ is a configuration of the combat system of Project Zomboid. In this case, the default value is ``95.0``\ , which means the initial HitChance cannot be above ``95.0``.

Below is a table listing the different elements which can influence the hit chance of a weapon:

.. list-table::
   :header-rows: 1

   * - Element
     - Type
     - Description
     - Formula
   * - `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingperkhitchancemodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's hit chance.
     - ``HitChance += AimingPerkHitChanceModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result.
     - ``HitChance += max(sightlessBonus - sightlessAimDelayPenalty, sightWindowBonus - sightWindowAimDelayPenalty)``
   * - Moodles penalty
     - Player condition
     - Being panicked, stressed, tired, drunk or lacking endurance will all negatively impact the ``HitChance``.
     - ``HitChance -= moodlesPenalty``
   * - Weather penalty
     - Environment
     - Wind, rain, fog, low-light will all negatively impact the ``HitChance``.
     - ``HitChance -= weatherPenalty``
   * - Movement penalty
     - Player condition
     - The shooter speed and the distance will negatively impact the ``HitChance``.
     - ``HitChance -= movementPenalty``
   * - Arm pain penalty
     - Player condition
     - The character's level of `pain <https://pzwiki.net/wiki/Pain>`_ will impact its aiming.
     - ``HitChance -= armPainPenalty``
   * - Headgear vision penalty
     - Player condition
     - Headgear will impact aiming, if the relevant sandbox option is enabled.
     - ``HitChance -= headgearVisionPenalty``


The final obtained value of ``HitChance`` is clamped against the `MINIMUM_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MINIMUM_TO_HIT_CHANCE>`_ and `MAXIMUM_TO_HIT_CHANCE <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/combat/CombatConfigKey.html#MAXIMUM_TO_HIT_CHANCE>`_\ , both respectively equal to ``5.0`` and ``100.0`` by default.

At point-blank range, all combined penalties are scaled toward zero, so close shots are always more forgiving. The `HitChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-hitchance>`_ parameter will set the floor for all players while `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingperkhitchancemodifier>`_ will increase accuracy with the level of aiming of the player. Low base and high modifier makes the gun terrible while unskilled but excellent with investment in aiming.

.. _item-hitchancemodifier:

HitChanceModifier
^^^^^^^^^^^^^^^^^

    Type: integer

See :ref:`item-hitchance` for more details.

.. _item-hitfloorsound:

HitFloorSound
^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)
    Default: BatOnFloor

No description

.. _item-hitsound:

HitSound
^^^^^^^^

    Type: string (block: :ref:`sound`)
    Default: BaseballBatHit

No description

.. _item-hungerchange:

HungerChange
^^^^^^^^^^^^

    Type: Any

No description

.. _item-icon:

Icon
^^^^

    Type: string
    Default: None

Used to specify the icon of the item, usually used in the inventory and crafting menus to easily recognize the item. The icon file needs to be located inside the ``media/textures/`` folder and the file name must start with ``Item_``\ , and be of the extension ``.png``.

.. code-block::

   📁 media
     📁 textures
       📄 Item_iconName.png

When referencing the icon in the item script, you should not include the ``Item_`` prefix and the ``.png`` extension. For example, to reference the icon file above in the item script:

.. code-block::

   Icon = iconName,

Subfolders
""""""""""

Subfolders are not directly supported, but you can use some tricks to have them working. Here's a simple example:

.. code-block::

   Icon = subFolder/iconName,

Means your folder structure should be:

.. code-block::

   📁 media
     📁 textures
       📁 Item_subFolder
         📄 iconName.png

Notice how the ``Item_`` prefix is not on the file but on the folder in this case.

Food icons
""""""""""

Icons can be specified for rotten, cooked and burned food (\ ``ItemType = base:food,``\ ) by adding the following suffix to the icon files:


* ``Rotten`` or ``Spoiled`` for food that has rotten, meaning has passed the `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daystotallyrotten>`_ value.
* ``Cooked`` for food that has been cooked, meaning has passed the `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestocook>`_ value.
* ``Overdone`` or ``Burnt`` for food that has been cooked to the point of burning, meaning has passed the `MinutesToBurn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestoburn>`_ value.

For example, take a food item with the icon file defined as such:

.. code-block::

   Icon = iconName,

To add variants based on food condition, you would have the following file structure:

.. code-block::

   📁 media
     📁 textures
       📄 Item_iconName.png
       📄 Item_iconNameCooked.png
       📄 Item_iconNameRotten.png
       📄 Item_iconNameBurnt.png

.. _item-iconcolormask:

IconColorMask
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-iconfluidmask:

IconFluidMask
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-iconsfortexture:

IconsForTexture
^^^^^^^^^^^^^^^

    Type: array (array of string, separator: ';')

No description

.. _item-idleanim:

IdleAnim
^^^^^^^^

    Type: string
    Default: Idle

No description

.. _item-impactsound:

ImpactSound
^^^^^^^^^^^

    Type: string (block: :ref:`sound`)
    Default: BaseballBatHit

No description

.. _item-insertallbulletsreload:

InsertAllBulletsReload
^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-insertammosound:

InsertAmmoSound
^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-insertammostartsound:

InsertAmmoStartSound
^^^^^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-insertammostopsound:

InsertAmmoStopSound
^^^^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-insulation:

Insulation
^^^^^^^^^^

    Type: Any

No description

.. _item-inversecoughprobability:

InverseCoughProbability
^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-inversecoughprobabilitysmoker:

InverseCoughProbabilitySmoker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-isaimedfirearm:

IsAimedFirearm
^^^^^^^^^^^^^^

    Type: boolean

`IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-isaimedfirearm>`_ enables the entire aimed-firearm subsystem: ballistics controller, reticle, muzzle flash, firearm-specific condition handling and ballistics-base target detection. Without it the weapon falls back to melee sweep logic.

Set to ``true`` for any normal gun. Distinct from `Ranged <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-ranged>`_ which marks the item as a ranged weapon for the animations `conditions <https://pzwiki.net/wiki/Conditions>`_.

.. _item-isaimedhandweapon:

IsAimedHandWeapon
^^^^^^^^^^^^^^^^^

    Type: boolean

No description

.. _item-iscookable:

IsCookable
^^^^^^^^^^

    Type: boolean

No description

.. _item-isdung:

IsDung
^^^^^^

    Type: boolean

No description

.. _item-ishightier:

IsHighTier
^^^^^^^^^^

    Type: Any

No description

.. _item-isportable:

IsPortable
^^^^^^^^^^

    Type: Any

No description

.. _item-istelevision:

IsTelevision
^^^^^^^^^^^^

    Type: Any

No description

.. _item-iswatersource:

IsWaterSource
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-itemaftercleaning:

ItemAfterCleaning
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-itemtype:

ItemType
^^^^^^^^

    Type: string (required)

Defines the class of the item which will impact which parameters the item can take and its properties as well as how it is used by the player. Clothing for instance will handle differently their texture and model in comparison to the other type of items, containers can hold items and weapons can be used by the player to attack and deal damage. You cannot use a custom class of item and only the ones accepted by the game.

Allowed values:

    - ``base:alarmclock``
    - ``base:alarmclockclothing``
    - ``base:animal``
    - ``base:clothing``
    - ``base:container``
    - ``base:drainable``
    - ``base:food``
    - ``base:key``
    - ``base:literature``
    - ``base:map``
    - ``base:moveable``
    - ``base:normal``
    - ``base:radio``
    - ``base:weapon``
    - ``base:weaponpart``

.. _item-itemwhendry:

ItemWhenDry
^^^^^^^^^^^

    Type: Any

No description

.. _item-jamgunchance:

JamGunChance
^^^^^^^^^^^^

    Type: float
    Default: 1.0

Base probability of a jam on each trigger pull. Final jam roml also scales with the sandbox jam multiplier, current gun condition (lower condition = higher jam chance), and low Aiming/Strength.

``JamGunChance = 1`` is already low. Setting it to ``0`` basically disables jams from this weapon. Higher values makes the gun unreliable and punishes neglecting the gun or unskilled use.

.. _item-keepondeplete:

KeepOnDeplete
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-knockbackonnodeath:

KnockBackOnNoDeath
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-knockdownmod:

KnockdownMod
^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-learnedrecipes:

LearnedRecipes
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-lightdistance:

LightDistance
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-lightstrength:

LightStrength
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-lipids:

Lipids
^^^^^^

    Type: Any

No description

.. _item-lowlightbonus:

LowLightBonus
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-lvlskilltrained:

LvlSkillTrained
^^^^^^^^^^^^^^^

    Type: integer
    Default: -1

No description

.. _item-magazine_subject:

magazine_subject
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-magazinetype:

MagazineType
^^^^^^^^^^^^

    Type: string (block: :ref:`item`, with :ref:`module`)

See :ref:`item-ammotype` for more details.

.. _item-makeuptype:

MakeUpType
^^^^^^^^^^

    Type: Any

No description

.. _item-manuallyremovespentrounds:

ManuallyRemoveSpentRounds
^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-map:

Map
^^^

    Type: Any

No description

.. _item-maxammo:

MaxAmmo
^^^^^^^

    Type: integer

No description

.. _item-maxcapacity:

MaxCapacity
^^^^^^^^^^^

    Type: integer
    Default: -1

No description

.. _item-maxchannel:

MaxChannel
^^^^^^^^^^

    Type: integer
    Default: 108000

No description

.. _item-maxdamage:

MaxDamage
^^^^^^^^^

    Type: float
    Default: 1.5

Rolls the hit damage of the weapon between ``MinDamage`` and ``MaxDamage``.

.. _item-maxhitcount:

MaxHitcount
^^^^^^^^^^^

    Type: integer
    Default: 1000

`MaxHitcount <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxhitcount>`_ sets the maximum number of targets the weapon can hit with one attack. For ranged weapons, it will determine how many targets a single shot can hit. For melee weapons, a single swing can hit multiple targets if the relevant sandbox option allows it (Weapon Multi-Hit).

When `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-piercingbullets>`_ is ``true``\ , a shot continues past the first target and registers on collinear targets behind it. Each subsequent pierced target receives reduced damage (\ ``damage / PIERCING_BULLET_DAMAGE_REDUCTION``\ ). Targets must be within approximatively 1 degree of each other in angle to qualify.

Keep ``MaxHitcount`` to 1 for a standard rifle, and set it to 2 with `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-piercingbullets>`_ to have AP rounds behavior (M16A2 for example).

.. _item-maxitemsize:

MaxItemSize
^^^^^^^^^^^

    Type: Any

No description

.. _item-maxrange:

MaxRange
^^^^^^^^

    Type: float
    Default: 1.0

`MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrange>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `MaxRangeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrangemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

The `MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrange>`_ of a weapon is used to determine the maximum distance the weapon can shoot. Targets beyond ``effectiveMaxRange`` calculated with the formula below simply can't be reached, the parameter is a hard cutoff, not a penalty in damage or anything like that.

.. code-block::

   effectiveMaxRange = MaxRange + AimingPerkRangeModifier x (AimingLevel / 2.0)

All rifles from the base game have a ``AimingPerkRangeModifier`` of 0, so `aiming level <https://pzwiki.net/wiki/Aiming>`_ has no effect on the range of guns. Set it above 0 to give skilled players extra reach.

.. _item-maxrangemodifier:

MaxRangeModifier
^^^^^^^^^^^^^^^^

    Type: float

See :ref:`item-maxrange` for more details.

.. _item-maxsightrange:

MaxSightRange
^^^^^^^^^^^^^

    Type: float

`MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_ define the optimal sight window, to be more specific, the distance band where hits and critical hits bonuses peak.

The `aiming skill <https://pzwiki.net/wiki/Aiming>`_ and `eagle eyed <https://pzwiki.net/wiki/Eagle_Eyed>`_ will impact these values:

.. code-block::

   effectiveMin = MinSightRange x (1 - AimingLevel / 30)
   effectiveMax = MaxSightRange x (1 + AimingLevel / 30) x (EagleEyed ? 1.2 : 1.0)

At aiming 10, the minimum shrinks by 33% and the max grows by 33%, which widens the window significantly. When the trait `Short Sighted <https://pzwiki.net/wiki/Short_Sighted>`_ is present and the character doesn't wear glasses, the ``effectiveMax`` equals ``effectiveMin``\ , making the entire bonus window disappear.

Inside the the ``effectiveMin`` and ``effectiveMax`` window, the bonus follows a `Gaussian <https://en.wikipedia.org/wiki/Bell-shaped_function>`_ with the bonus peaking at the midpoint. Aim-delay penalty is also reduced inside the window.

Below ``effectiveMin``\ , a small linear penalty is applied as the gun is not suited for point-blank. Above ``effectiveMax``\ , a growing quadratic penalty is applied, the bonus degrades rapidly past the edge.

A CQC gun should have a low `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_ while a marksman riffle should have a high `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ with a wide window.

.. _item-mechanicsitem:

MechanicsItem
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-mediacategory:

MediaCategory
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-medical:

Medical
^^^^^^^

    Type: Any

No description

.. _item-metalvalue:

MetalValue
^^^^^^^^^^

    Type: Any

No description

.. _item-micrange:

MicRange
^^^^^^^^

    Type: Any

No description

.. _item-minangle:

MinAngle
^^^^^^^^

    Type: float
    Default: 1.0

For `IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-isaimedfirearm>`_ set to ``true``\ , the ballistics controller handles target detection and does not use `MinAngle <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minangle>`_ in the ranged hit-chance formula. These serve one narrow purpose: the ``isMeleeTargetTooCloseToShoot()`` check, detecting if a target is so close it should trigger a melee strike instead of a shot.

``MinAngle`` is a dot-product threshold (-1 to 1). Values near 1.0 mean the target must be almost directly in front to trigger the melee-swap check, while lower values widen the angle.

`AimingPerkMinAngleModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingperkminanglemodifier>`_ is parsed and stored and impacts the minimum angle with the following formula:

.. code-block:: java

   effectiveMinAngle = MinAngle - AimingPerkMinAngleModifier * Aiming level

.. _item-minchannel:

MinChannel
^^^^^^^^^^

    Type: integer
    Default: 88000

No description

.. _item-mindamage:

MinDamage
^^^^^^^^^

    Type: float

See :ref:`item-maxdamage` for more details.

.. _item-minimumswingtime:

MinimumSwingtime
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-minrange:

MinRange
^^^^^^^^

    Type: float

Hard minimum attack distance. If the target is closer than ``MinRange``\ , the ballistics controller does not register the shot and the game may force a melee swap. This is a binary threshold, not a penalty band. Separate from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_.

Long rifles should be hard to use in tight spaces. ``0.2`` to ``0.35`` is a small gap but ``0.61`` is noticeably limiting indoors.

.. _item-minsightrange:

MinSightRange
^^^^^^^^^^^^^

    Type: float

See :ref:`item-maxsightrange` for more details.

.. _item-minutestoburn:

MinutesToBurn
^^^^^^^^^^^^^

    Type: float
    Default: 120.0

How many in-game minutes it takes to burn the food. This value must
be higher than `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestocook>`_.

In comparison with `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestocook>`_\ , this parameter is not available for ``base:drainable`` `ItemTypes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_.

.. _item-minutestocook:

MinutesToCook
^^^^^^^^^^^^^

    Type: float
    Default: 60.0

How many in-game minutes it takes to cook the food. This value must be smaller than `MinutesToBurn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestoburn>`_.

.. _item-modelweaponpart:

ModelWeaponPart
^^^^^^^^^^^^^^^

    Type: Any
    Can be duplicated: ✓

No description

.. _item-mounton:

MountOn
^^^^^^^

    Type: Any

No description

.. _item-multiplehitconditionaffected:

MultipleHitConditionAffected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: boolean
    Default: True

No description

.. _item-muzzleflashmodelkey:

MuzzleFlashModelKey
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-neckprotectionmodifier:

NeckProtectionModifier
^^^^^^^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-needtobeclosedoncereload:

needtobeclosedoncereload
^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-noiseduration:

NoiseDuration
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-noiserange:

NoiseRange
^^^^^^^^^^

    Type: Any

No description

.. _item-notransmit:

NoTransmit
^^^^^^^^^^

    Type: Any

No description

.. _item-npcsoundboost:

NPCSoundBoost
^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-numberofpages:

NumberOfPages
^^^^^^^^^^^^^

    Type: integer
    Default: -1

No description

.. _item-numlevelstrained:

NumLevelsTrained
^^^^^^^^^^^^^^^^

    Type: integer
    Default: 1

No description

.. _item-onbreak:

OnBreak
^^^^^^^

    Type: Any

No description

.. _item-oncooked:

OnCooked
^^^^^^^^

    Type: Any

No description

.. _item-oncreate:

OnCreate
^^^^^^^^

    Type: Any

No description

.. _item-oneat:

OnEat
^^^^^

    Type: Any

No description

.. _item-openingrecipe:

OpeningRecipe
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-opensound:

OpenSound
^^^^^^^^^

    Type: Any

No description

.. _item-originx:

OriginX
^^^^^^^

    Type: Any

No description

.. _item-originy:

OriginY
^^^^^^^

    Type: Any

No description

.. _item-originz:

originZ
^^^^^^^

    Type: Any

No description

.. _item-otherhandrequire:

OtherHandRequire
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-otherhanduse:

OtherHandUse
^^^^^^^^^^^^

    Type: Any

No description

.. _item-packaged:

Packaged
^^^^^^^^

    Type: Any

No description

.. _item-padlock:

Padlock
^^^^^^^

    Type: Any

No description

.. _item-pagetowrite:

PageToWrite
^^^^^^^^^^^

    Type: Any

No description

.. _item-painreduction:

painReduction
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-parttype:

PartType
^^^^^^^^

    Type: Any

No description

.. _item-physicsobject:

PhysicsObject
^^^^^^^^^^^^^

    Type: string (block: :ref:`item`, with :ref:`module`)

Provides another item (or itself) as a throwable object. When used, the item will be thrown instead of used as an actual in hands weapon.

.. _item-piercingbullets:

PiercingBullets
^^^^^^^^^^^^^^^

    Type: boolean

See :ref:`item-maxhitcount` for more details.

.. _item-placedsprite:

PlacedSprite
^^^^^^^^^^^^

    Type: Any

No description

.. _item-placemultiplesound:

PlaceMultipleSound
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-placeonesound:

PlaceOneSound
^^^^^^^^^^^^^

    Type: string

No description

.. _item-poisonpower:

PoisonPower
^^^^^^^^^^^

    Type: Any

No description

.. _item-pourtype:

PourType
^^^^^^^^

    Type: Any

No description

.. _item-primaryanimmask:

primaryAnimMask
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-projectilecount:

Projectilecount
^^^^^^^^^^^^^^^

    Type: integer
    Default: 1

Only active when the weapon is ranged and has `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-rangefalloff>`_ set to ``true``. In that mode, the ballistics controller generates multiple spread projectiles. The field is never read when `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-rangefalloff>`_ is ``false``.

Inert for standard rifles. Required only for shotgun-style spread.

.. _item-projectilespread:

ProjectileSpread
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-projectilespreadmodifier:

ProjectileSpreadModifier
^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-projectileweightcenter:

ProjectileWeightCenter
^^^^^^^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-protectfromrainwhenequipped:

ProtectFromRainWhenEquipped
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-proteins:

Proteins
^^^^^^^^

    Type: Any

No description

.. _item-pushbackmod:

PushBackMod
^^^^^^^^^^^

    Type: float
    Default: 1.0

Scales the magnitude of the hit-reaction push applied to the target character. A higher value will increase the time the target is staggered. It will also impact the spread of blood.

Higher gives a more weighty, impactful feel.

.. _item-putinsound:

PutInSound
^^^^^^^^^^

    Type: Any

No description

.. _item-rackaftershoot:

RackAfterShoot
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-racksound:

RackSound
^^^^^^^^^

    Type: Any

No description

.. _item-rainfactor:

RainFactor
^^^^^^^^^^

    Type: Any

No description

.. _item-ranged:

Ranged
^^^^^^

    Type: boolean

See :ref:`item-isaimedfirearm` for more details.

.. _item-rangefalloff:

RangeFalloff
^^^^^^^^^^^^

    Type: boolean

No description

.. _item-readtype:

ReadType
^^^^^^^^

    Type: Any

No description

.. _item-recoildelay:

RecoilDelay
^^^^^^^^^^^

    Type: Any

`RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelaymodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. Weapon attachments will add or subtract from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ directly.

Controls how long post-shot recovery takes before aim settling can begin. High values means the gun has a huge kick and forces a pause. Lower values is a flat, fast and snappy gun. `Strength <https://pzwiki.net/wiki/Strength>`_ and `aiming <https://pzwiki.net/wiki/Aiming>`_ will both reduce the recoil delay. Holding the gun one-handed will negatively impact the recoil handling. The following formula is used:

.. code-block:: java

   effectiveDelay = RecoilDelay
                 * (1 - AimingLevel / 40)
                 * (1 - (StrengthLevel * 2 - 10) / 40)
                 * (one-handed penalty: * 1.3 if primary hand only, secondary empty)

Aim countdown starts when the recoil delay counter is less than ``effectiveDelay * AimingLevel / 30``. Higher aiming also lets aim recovery start earlier in the recoil window.

.. _item-recoildelaymodifier:

RecoilDelayModifier
^^^^^^^^^^^^^^^^^^^

    Type: Any

See :ref:`item-recoildelay` for more details.

.. _item-reduceinfectionpower:

ReduceInfectionPower
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-reloadtime:

Reloadtime
^^^^^^^^^^

    Type: Any

No description

.. _item-reloadtimemodifier:

ReloadTimeModifier
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-remotecontroller:

RemoteController
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-remoterange:

RemoteRange
^^^^^^^^^^^

    Type: Any

No description

.. _item-removenegativeeffectoncooked:

RemoveNegativeEffectOnCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-removeonbroken:

RemoveOnBroken
^^^^^^^^^^^^^^

    Type: boolean
    Default: True

No description

.. _item-removeunhappinesswhencooked:

RemoveUnhappinessWhenCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceinprimaryhand:

ReplaceInPrimaryHand
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceinsecondhand:

ReplaceInSecondHand
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceoncooked:

ReplaceOnCooked
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceondeplete:

ReplaceOnDeplete
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceonextinguish:

ReplaceOnExtinguish
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceonrotten:

ReplaceOnRotten
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-replaceonuse:

ReplaceOnUse
^^^^^^^^^^^^

    Type: Any

No description

.. _item-requireinhandorinventory:

RequireInHandOrInventory
^^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-requiresequippedbothhands:

RequiresEquippedBothHands
^^^^^^^^^^^^^^^^^^^^^^^^^

    Type: boolean

No description

.. _item-researchablerecipes:

Researchablerecipes
^^^^^^^^^^^^^^^^^^^

    Type: array (array of string, separator: ';')

No description

.. _item-runanim:

RunAnim
^^^^^^^

    Type: string
    Default: Run

No description

.. _item-runspeedmodifier:

RunSpeedModifier
^^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-scaleworldicon:

ScaleWorldIcon
^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-scratchdefense:

ScratchDefense
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-secondaryanimmask:

secondaryAnimMask
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-sensorrange:

SensorRange
^^^^^^^^^^^

    Type: Any

No description

.. _item-sharpness:

Sharpness
^^^^^^^^^

    Type: Any

No description

.. _item-shellfallsound:

ShellFallSound
^^^^^^^^^^^^^^

    Type: string (block: :ref:`sound`)

No description

.. _item-shoutmultiplier:

ShoutMultiplier
^^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-shouttype:

ShoutType
^^^^^^^^^

    Type: Any

No description

.. _item-skilltrained:

SkillTrained
^^^^^^^^^^^^

    Type: string

No description

.. _item-smokerange:

SmokeRange
^^^^^^^^^^

    Type: Any

No description

.. _item-soundgain:

SoundGain
^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-soundmap:

SoundMap
^^^^^^^^

    Type: Any
    Can be duplicated: ✓

No description

.. _item-soundparameter:

SoundParameter
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-soundradius:

SoundRadius
^^^^^^^^^^^

    Type: Any

No description

.. _item-soundvolume:

SoundVolume
^^^^^^^^^^^

    Type: Any

No description

.. _item-spawnwith:

SpawnWith
^^^^^^^^^

    Type: Any

No description

.. _item-spice:

Spice
^^^^^

    Type: Any

No description

.. _item-splatbloodonnodeath:

SplatBloodOnNoDeath
^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-splatnumber:

SplatNumber
^^^^^^^^^^^

    Type: integer
    Default: 2

No description

.. _item-splatsize:

SplatSize
^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-staticmodel:

StaticModel
^^^^^^^^^^^

    Type: string (block: :ref:`model`, with :ref:`module`)

No description

.. _item-staticmodelsbyindex:

StaticModelsByIndex
^^^^^^^^^^^^^^^^^^^

    Type: array (array of string, separator: ';')

No description

.. _item-stomppower:

StompPower
^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-stoppower:

StopPower
^^^^^^^^^

    Type: float
    Default: 5.0

See :ref:`item-criticalchance` for more details.

.. _item-stresschange:

StressChange
^^^^^^^^^^^^

    Type: Any

No description

.. _item-subcategory:

SubCategory
^^^^^^^^^^^

    Type: string

No description

.. _item-survivalgear:

SurvivalGear
^^^^^^^^^^^^

    Type: Any

No description

.. _item-suspensioncompression:

suspensionCompression
^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-suspensiondamping:

suspensionDamping
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-swingamountbeforeimpact:

SwingAmountBeforeImpact
^^^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-swinganim:

SwingAnim
^^^^^^^^^

    Type: string
    Default: Rifle

No description

.. _item-swingsound:

SwingSound
^^^^^^^^^^

    Type: string (block: :ref:`sound`)
    Default: BaseballBatSwing

No description

.. _item-swingtime:

Swingtime
^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-tags:

Tags
^^^^

    Type: array (array of string, separator: ';')

A list of tags to assign to the item. Tags are used by the game to easily identify properties of the items from the Lua or Java. This can notably be used in `craftRecipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_.

For example:

.. code-block:: cpp

   Tags = base:egg;base:hasmetal,

You can find a list of all tags on the `wiki <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_. The wiki also provides a list of every items (per full type) associated to tags `here <https://pzwiki.net/wiki/Item_tag>`_.

To create a custom tag, you have to first create its definition in your mod's `registries <https://pzwiki.net/wiki/Registries>`_. In the ``registries.lua`` file, define the following by renaming the various elements to fit your mod name, id etc:

.. code-block:: lua

   YourModRegistry = {}
   YourModRegistry.YOUR_TAG_NAME = ItemTag.register("yourmodid:yourtagname")

You can then use that tag ``yourmodid:yourtagname`` in your item definition. And you can use the stored ItemTag reference ``YourModRegistry.YOUR_TAG_NAME`` in your Lua code.

.. _item-thirstchange:

ThirstChange
^^^^^^^^^^^^

    Type: Any

No description

.. _item-ticksperequipuse:

ticksPerEquipUse
^^^^^^^^^^^^^^^^

    Type: integer
    Default: 30

No description

.. _item-tohitmodifier:

ToHitModifier
^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-tooltip:

Tooltip
^^^^^^^

    Type: Any

No description

.. _item-torchcone:

TorchCone
^^^^^^^^^

    Type: Any

No description

.. _item-torchdot:

TorchDot
^^^^^^^^

    Type: float
    Default: 0.96

No description

.. _item-transmitrange:

TransmitRange
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-trap:

Trap
^^^^

    Type: boolean
    Default: False

No description

.. _item-treedamage:

TreeDamage
^^^^^^^^^^

    Type: Any

No description

.. _item-triggerexplosiontimer:

triggerExplosionTimer
^^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-twohandweapon:

TwoHandWeapon
^^^^^^^^^^^^^

    Type: boolean

`TwoHandWeapon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-twohandweapon>`_ marks the weapon as a two-handed weapon. `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ gets a x1.3 penalty when the weapon is held one-handed instead of two handed. `RequiresEquippedBothHands <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-requiresequippedbothhands>`_ enforces the equip restriction in the context menu.

.. _item-twoway:

TwoWay
^^^^^^

    Type: Any

No description

.. _item-type:

Type
^^^^

    Type: Any

Used to set the class of the item, which will influence parameters available.

.. warning::

   **Deprecated** (since version 42.13.0)

   Use :ref:`item-itemtype` instead.

.. _item-unequipsound:

UnequipSound
^^^^^^^^^^^^

    Type: string

No description

.. _item-unhappychange:

UnhappyChange
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-usedelta:

UseDelta
^^^^^^^^

    Type: float
    Default: 0.03125

No description

.. _item-useendurance:

UseEndurance
^^^^^^^^^^^^

    Type: boolean
    Default: True

If ``true``\ , the weapon will consume stamina on use based on the weapon `weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weight>`_\ , `EnduranceMod <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-endurancemod>`_\ , fatigue modifiers and traits.

For guns, it is preferable to keep this as ``False``.

.. _item-usesbattery:

UsesBattery
^^^^^^^^^^^

    Type: Any

No description

.. _item-useself:

UseSelf
^^^^^^^

    Type: Any

No description

.. _item-usewhileequipped:

UseWhileEquipped
^^^^^^^^^^^^^^^^

    Type: boolean
    Default: True

No description

.. _item-usewhileunequipped:

UseWhileUnequipped
^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-useworlditem:

UseWorldItem
^^^^^^^^^^^^

    Type: Any

No description

.. _item-vehiclepartmodel:

VehiclePartModel
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-vehicletype:

VehicleType
^^^^^^^^^^^

    Type: Any

No description

.. _item-visionmodifier:

VisionModifier
^^^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-visualaid:

VisualAid
^^^^^^^^^

    Type: Any

No description

.. _item-waterresistance:

WaterResistance
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-weaponhitarmoursound:

WeaponHitArmourSound
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-weaponlength:

WeaponLength
^^^^^^^^^^^^

    Type: float
    Default: 0.4

No description

.. _item-weaponreloadtype:

WeaponReloadType
^^^^^^^^^^^^^^^^

    Type: string
    Default: handgun

See :ref:`item-ammotype` for more details.

.. _item-weaponsprite:

WeaponSprite
^^^^^^^^^^^^

    Type: Any

No description

.. _item-weaponspritesbyindex:

WeaponSpritesByIndex
^^^^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-weaponweight:

WeaponWeight
^^^^^^^^^^^^

    Type: float
    Default: 1.0

No description

.. _item-weight:

Weight
^^^^^^

    Type: float
    Default: 1.0

Sets the weight of the item, or more commonly refered to as a encumbrance. `Weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_ will impact the weight of the weapon when attached. Will also impact stamina drain when `UseEndurance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-useendurance>`_ is ``true``.

.. _item-weightempty:

WeightEmpty
^^^^^^^^^^^

    Type: Any

No description

.. _item-weightmodifier:

WeightModifier
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-weightreduction:

WeightReduction
^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-wet:

Wet
^^^

    Type: Any

No description

.. _item-wetcooldown:

WetCooldown
^^^^^^^^^^^

    Type: Any

No description

.. _item-wheelfriction:

wheelFriction
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-windresistance:

WindResistance
^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-withdrainable:

WithDrainable
^^^^^^^^^^^^^

    Type: Any

No description

.. _item-withoutdrainable:

WithoutDrainable
^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-worldobjectsprite:

WorldObjectSprite
^^^^^^^^^^^^^^^^^

    Type: Any

No description

.. _item-worldrender:

WorldRender
^^^^^^^^^^^

    Type: Any

No description

.. _item-worldstaticmodel:

WorldStaticModel
^^^^^^^^^^^^^^^^

    Type: string (block: :ref:`model`, with :ref:`module`)

No description

.. _item-worldstaticmodelsbyindex:

WorldStaticModelsByIndex
^^^^^^^^^^^^^^^^^^^^^^^^

    Type: array (array of string, separator: ';')

No description

