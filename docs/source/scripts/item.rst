.. _scripts-item:

item
====

:Soft Override: True

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


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`

This block can have the following child blocks:

- :ref:`component <scripts-component>`
- :ref:`component Durability <scripts-component-durability>`
- :ref:`component ContextMenuConfig <scripts-component-contextmenuconfig>`
- :ref:`component FluidContainer <scripts-component-fluidcontainer>`



ID
--

This block can have an ID.

:Optional: False
:Can have spaces: False


ItemType parameters
-------------------

Specific parameters are only available for certain :ref:`item-itemtype`. The following lists for each ItemType will show what parameter is only saved for that specific ItemType script class (sub classes to `Item <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/Item.html>`_), which means using them for other classes doesn't make any sense as they will simply not be loaded in by the game.

base:drainable
^^^^^^^^^^^^^^

- :ref:`cantBeConsolided <scripts-item-cantbeconsolided>`
- :ref:`ConsolidateOption <scripts-item-consolidateoption>`
- :ref:`Spice <scripts-item-spice>`
- :ref:`UseDelta <scripts-item-usedelta>`

base:food
^^^^^^^^^

- :ref:`BadInMicrowave <scripts-item-badinmicrowave>`
- :ref:`Calories <scripts-item-calories>`
- :ref:`CannedFood <scripts-item-cannedfood>`
- :ref:`Carbohydrates <scripts-item-carbohydrates>`
- :ref:`DangerousUncooked <scripts-item-dangerousuncooked>`
- :ref:`DaysFresh <scripts-item-daysfresh>`
- :ref:`DaysTotallyRotten <scripts-item-daystotallyrotten>`
- :ref:`Lipids <scripts-item-lipids>`
- :ref:`Packaged <scripts-item-packaged>`
- :ref:`Proteins <scripts-item-proteins>`
- :ref:`RemoveNegativeEffectOnCooked <scripts-item-removenegativeeffectoncooked>`
- :ref:`ReplaceOnRotten <scripts-item-replaceonrotten>`
- :ref:`Spice <scripts-item-spice>`

base:literature
^^^^^^^^^^^^^^^

- :ref:`LearnedRecipes <scripts-item-learnedrecipes>`
- :ref:`LvlSkillTrained <scripts-item-lvlskilltrained>`

base:normal
^^^^^^^^^^^

- :ref:`AmmoType <scripts-item-ammotype>`

base:radio
^^^^^^^^^^

- :ref:`UseDelta <scripts-item-usedelta>`

base:weapon
^^^^^^^^^^^

- :ref:`AimingPerkMinAngleModifier <scripts-item-aimingperkminanglemodifier>`
- :ref:`AimingPerkRangeModifier <scripts-item-aimingperkrangemodifier>`
- :ref:`Aimingtime <scripts-item-aimingtime>`
- :ref:`AmmoBox <scripts-item-ammobox>`
- :ref:`AmmoType <scripts-item-ammotype>`
- :ref:`ClickSound <scripts-item-clicksound>`
- :ref:`CriticalChance <scripts-item-criticalchance>`
- :ref:`CyclicRateMultiplier <scripts-item-cyclicratemultiplier>`
- :ref:`EnduranceMod <scripts-item-endurancemod>`
- :ref:`ExplosionDuration <scripts-item-explosionduration>`
- :ref:`ExplosionPower <scripts-item-explosionpower>`
- :ref:`ExplosionRange <scripts-item-explosionrange>`
- :ref:`FireMode <scripts-item-firemode>`
- :ref:`FireModePossibilities <scripts-item-firemodepossibilities>`
- :ref:`FireRange <scripts-item-firerange>`
- :ref:`FireStartingChance <scripts-item-firestartingchance>`
- :ref:`FireStartingEnergy <scripts-item-firestartingenergy>`
- :ref:`HitChance <scripts-item-hitchance>`
- :ref:`HitFloorSound <scripts-item-hitfloorsound>`
- :ref:`HitSound <scripts-item-hitsound>`
- :ref:`ImpactSound <scripts-item-impactsound>`
- :ref:`IsAimedFirearm <scripts-item-isaimedfirearm>`
- :ref:`IsAimedHandWeapon <scripts-item-isaimedhandweapon>`
- :ref:`JamGunChance <scripts-item-jamgunchance>`
- :ref:`MagazineType <scripts-item-magazinetype>`
- :ref:`MaxHitcount <scripts-item-maxhitcount>`
- :ref:`MaxSightRange <scripts-item-maxsightrange>`
- :ref:`MinAngle <scripts-item-minangle>`
- :ref:`MinSightRange <scripts-item-minsightrange>`
- :ref:`PhysicsObject <scripts-item-physicsobject>`
- :ref:`PiercingBullets <scripts-item-piercingbullets>`
- :ref:`Projectilecount <scripts-item-projectilecount>`
- :ref:`PushBackMod <scripts-item-pushbackmod>`
- :ref:`Ranged <scripts-item-ranged>`
- :ref:`RangeFalloff <scripts-item-rangefalloff>`
- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`ShellFallSound <scripts-item-shellfallsound>`
- :ref:`StopPower <scripts-item-stoppower>`
- :ref:`SwingSound <scripts-item-swingsound>`
- :ref:`TwoHandWeapon <scripts-item-twohandweapon>`
- :ref:`UseDelta <scripts-item-usedelta>`
- :ref:`UseEndurance <scripts-item-useendurance>`
- :ref:`WeaponReloadType <scripts-item-weaponreloadtype>`

base:weaponpart
^^^^^^^^^^^^^^^

- :ref:`AimingTimeModifier <scripts-item-aimingtimemodifier>`
- :ref:`HitChanceModifier <scripts-item-hitchancemodifier>`
- :ref:`MaxRangeModifier <scripts-item-maxrangemodifier>`
- :ref:`MaxSightRange <scripts-item-maxsightrange>`
- :ref:`MinSightRange <scripts-item-minsightrange>`
- :ref:`RecoilDelayModifier <scripts-item-recoildelaymodifier>`



Parameters
----------

.. _scripts-item-acceptitemfunction:

AcceptItemFunction
^^^^^^^^^^^^^^^^^^

:Type: string

No description provided.


.. _scripts-item-acceptmediatype:

AcceptMediaType
^^^^^^^^^^^^^^^

:Type: integer
:Default: ``-1``

No description provided.


.. _scripts-item-activateditem:

ActivatedItem
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-aimingmod:

AimingMod
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-aimingperkcritmodifier:

AimingPerkCritModifier
^^^^^^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`CriticalChance <scripts-item-criticalchance>`.


.. _scripts-item-aimingperkhitchancemodifier:

AimingPerkHitChanceModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: float

See parameter :ref:`HitChance <scripts-item-hitchance>`.


.. _scripts-item-aimingperkminanglemodifier:

AimingPerkMinAngleModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: float

See parameter :ref:`MinAngle <scripts-item-minangle>`.


.. _scripts-item-aimingperkrangemodifier:

AimingPerkRangeModifier
^^^^^^^^^^^^^^^^^^^^^^^

:Type: float

See parameter :ref:`MaxRange <scripts-item-maxrange>`.


.. _scripts-item-aimingtime:

Aimingtime
^^^^^^^^^^

:Type: integer

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


.. _scripts-item-aimingtimemodifier:

AimingTimeModifier
^^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`AimingTime <scripts-item-aimingtime>`.


.. _scripts-item-aimreleasesound:

AimReleaseSound
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-alarmsound:

AlarmSound
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-alcoholic:

Alcoholic
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-alcoholpower:

AlcoholPower
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-alwaysknockdown:

AlwaysKnockdown
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-alwayswelcomegift:

AlwaysWelcomeGift
^^^^^^^^^^^^^^^^^

:Type: boolean
:Is useless: True

No description provided.


.. _scripts-item-ammobox:

AmmoBox
^^^^^^^

:Type: string (block: :ref:`item <scripts-item>`, with :ref:`module`)

No description provided.


.. _scripts-item-ammotype:

AmmoType
^^^^^^^^

:Type: string

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


* ``handgun``
* ``shotgun``
* ``boltactionnomag``
* ``boltaction``
* ``revolver``
* ``doublebarrelshotgun``
* ``doublebarrelshotgunsawn``

A custom ``WeaponReloadType`` can be used if the relevant animations and condition logic are properly set up in a custom `AnimNode <https://pzwiki.net/wiki/AnimNodes>`_.


.. _scripts-item-anglefalloff:

AngleFalloff
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-animalfeedtype:

AnimalFeedType
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-attachmentreplacement:

AttachmentReplacement
^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-attachmentsprovided:

AttachmentsProvided
^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-attachmenttype:

AttachmentType
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-badcold:

BadCold
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-badinmicrowave:

BadInMicrowave
^^^^^^^^^^^^^^

:Type: boolean

No description provided.


.. _scripts-item-bandagepower:

BandagePower
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-basespeed:

BaseSpeed
^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-basevolumerange:

BaseVolumeRange
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-bitedefense:

BiteDefense
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-bloodlocation:

BloodLocation
^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')
:Allowed values: 
* ``Apron``
* ``ShirtNoSleeves``
* ``JumperNoSleeves``
* ``Shirt``
* ``ShirtLongSleeves``
* ``Jumper``
* ``Jacket``
* ``LongJacket``
* ``ShortsShort``
* ``Trousers``
* ``Shoes``
* ``FullHelmet``
* ``Bag``
* ``Hands``
* ``Head``
* ``Neck``
* ``Groin``
* ``UpperBody``
* ``LowerBody``
* ``LowerLegs``
* ``UpperLegs``
* ``LowerArms``
* ``UpperArms``
* ``Hand_L``
* ``Hand_R``
* ``ForeArm_L``
* ``ForeArm_R``
* ``UpperArm_L``
* ``UpperArm_R``
* ``UpperLeg_L``
* ``UpperLeg_R``
* ``LowerLeg_L``
* ``LowerLeg_R``
* ``Foot_L``
* ``Foot_R``

No description provided.


.. _scripts-item-bodylocation:

BodyLocation
^^^^^^^^^^^^

:Type: Unknown

Used to define which location on the human character this clothing item can be worn. Needs to be a valid `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_body_locations.html>`_ value. You can also create new ones via `registries <https://pzwiki.net/wiki/Registries>`_.


.. _scripts-item-book_subject:

book_subject
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-boredomchange:

BoredomChange
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-brakeforce:

brakeForce
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-breaksound:

BreakSound
^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-bringtobearsound:

BringToBearSound
^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-bulletdefense:

BulletDefense
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-bullethitarmoursound:

BulletHitArmourSound
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-calories:

Calories
^^^^^^^^

:Type: float

The following stats are directly linked to the player's `nutrition <https://pzwiki.net/wiki/Nutrition>`_\ , which are hidden stats that will impact the player's weight gains and more (positive values will increase the stat when eaten):


* `Calories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-calories>`_
* `Carbohydrates <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-carbohydrates>`_
* `Lipids <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-lipids>`_
* `Proteins <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-proteins>`_


.. _scripts-item-canattach:

CanAttach
^^^^^^^^^

:Type: string

`CanAttach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-canattach>`_ and `CanDetach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-candetach>`_ are used to define whenever a `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_ can be respectively attached or detached to and from a `HandWeapon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_.

`OnAttach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-onattach>`_ and `OnDetach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-ondetach>`_ are used to define a callback function which will be called when the weapon part is attached or detached from the weapon.


.. _scripts-item-canbandage:

CanBandage
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canbarricade:

CanBarricade
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canbeequipped:

CanBeEquipped
^^^^^^^^^^^^^

:Type: Unknown

Needs to reference a valid `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-bodylocation>`_ value which will serve as the equipment location.


.. _scripts-item-canbeplaced:

CanBePlaced
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canberemote:

CanBeRemote
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canbereused:

CanBeReused
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canbewrite:

CanBeWrite
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-candetach:

CanDetach
^^^^^^^^^

:Type: string

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-canhaveholes:

CanHaveHoles
^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

Used to define whenever this item can get holes in it.


.. _scripts-item-cannedfood:

CannedFood
^^^^^^^^^^

:Type: boolean

`CannedFood <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-cannedfood>`_ will mark the item as a canned food which will impact how it is spawned in the world. It will also impact the type of item where instead of being "Food" it will be "CannedFood".


.. _scripts-item-canstack:

CanStack
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canstorewater:

CanStoreWater
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-cantattackwithlowestendurance:

CantAttackWithLowestEndurance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-cantbeconsolided:

cantBeConsolided
^^^^^^^^^^^^^^^^

:Type: boolean

See parameter :ref:`ConsolidateOption <scripts-item-consolidateoption>`.


.. _scripts-item-cantbefrozen:

CantBeFrozen
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-canteat:

CantEat
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-capacity:

Capacity
^^^^^^^^

:Type: integer
:Default: ``-1``
:Maximum: ``50``

Sets the capacity of the container. This value is limited to a maximum of 50 minus its own `weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weight>`_. The weight of the bag will follow the formula ``equippedWeight = weight * EquippedOrWornEncumbranceMultiplier + contentWeight * (1.0 - weightReduction / 100)``.


.. _scripts-item-carbohydrates:

Carbohydrates
^^^^^^^^^^^^^

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-categories:

Categories
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-chancetofall:

ChanceToFall
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-chancetospawndamaged:

ChanceToSpawnDamaged
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-clicksound:

ClickSound
^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)
:Default: ``Stormy9mmClick``

No description provided.


.. _scripts-item-clipsize:

ClipSize
^^^^^^^^

:Type: integer
:Is useless: True

No description provided.


.. _scripts-item-clipsizemodifier:

ClipSizeModifier
^^^^^^^^^^^^^^^^

:Type: integer
:Is useless: True

No description provided.


.. _scripts-item-closekillmove:

CloseKillMove
^^^^^^^^^^^^^

:Type: Unknown

Used to whenever this weapon can be used to do a close kill move, like knives to assassinate in the back.


.. _scripts-item-closesound:

CloseSound
^^^^^^^^^^

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-clothingextrasubmenu:

ClothingExtraSubmenu
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-clothingitem:

ClothingItem
^^^^^^^^^^^^

:Type: Unknown

``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.

``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.


.. _scripts-item-clothingitemextra:

ClothingItemExtra
^^^^^^^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-clothingitemextraoption:

ClothingItemExtraOption
^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-colorblue:

ColorBlue
^^^^^^^^^

:Type: integer
:Default: ``255``

No description provided.


.. _scripts-item-colorgreen:

ColorGreen
^^^^^^^^^^

:Type: integer
:Default: ``255``

No description provided.


.. _scripts-item-colorred:

ColorRed
^^^^^^^^

:Type: integer
:Default: ``255``

No description provided.


.. _scripts-item-combatspeedmodifier:

CombatSpeedModifier
^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-conditionaffectscapacity:

ConditionAffectsCapacity
^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

Set whenever condition of the item can impact the capacity value of the container.


.. _scripts-item-conditionlowerchanceonein:

ConditionLowerChanceOneIn
^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``10``

`ConditionLowerChanceOneIn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-conditionlowerchanceonein>`_ impacts the durability of the item, reducing the value
used to calculate the chance by doing ``chance = 1/ConditionLowerChanceOneIn``\ ,
which means increasing this parameter value will reduce the chance to damage the
item.

`ConditionMax <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-conditionmax>`_ sets the total durability pool, starting condition and repair ceiling. Make these two parameters high for robust military rifles, and low for a cheap civilian gun.


.. _scripts-item-conditionloweroffroad:

ConditionLowerOffroad
^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-conditionlowerstandard:

ConditionLowerStandard
^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-conditionmax:

ConditionMax
^^^^^^^^^^^^

:Type: integer
:Default: ``10``

See parameter :ref:`ConditionLowerChanceOneIn <scripts-item-conditionlowerchanceonein>`.


.. _scripts-item-consolidateoption:

ConsolidateOption
^^^^^^^^^^^^^^^^^

:Type: Unknown

By setting `cantBeConsolided <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-cantbeconsolided>`_ to ``false`` and providing a `ConsolidateOption <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-consolidateoption>`_ value, the item can be marked to merge its uses with other items of the same type in the inventory. This requires the item to be `Drainable type <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_.

The ConsolidateOption value needs to be a translation key which will be passed through `getText <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/core/Translator.html#getText(java.lang.String>`_\ ) to retrieve the translation value. The vanilla drainables (duct tape, wires, matches...) use the translation key ``ContextMenu_Merge`` which outputs a text 'Add to'.


.. _scripts-item-cookingsound:

CookingSound
^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

Custom sound to play when cooking this item.


.. _scripts-item-corpsesicknessdefense:

CorpseSicknessDefense
^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-cosmetic:

Cosmetic
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-count:

Count
^^^^^

:Type: integer
:Default: ``1``

The parameter is unused in the game scripts, unclear what it is used for.


.. _scripts-item-critdmgmultiplier:

CritDmgMultiplier
^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``2.0``

Multiplier applied to the damage of a hit if it is a critical hit, applied inside `IsoGameCharacter.Hit() <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html#Hit(zombie.inventory.types.HandWeapon,zombie.characters.IsoGameCharacter,float,boolean,float,boolean>`_\ ). Two types of crits can trigger:


* A normal crit: ``damage *= max(2.0, CritDmgMultiplier)``
* Aim-at-floor stomp (melee only): ``damage *= max(5.0, CritDmgMultiplier)``

The default value of the ``HandWeapon`` class is ``2.0``. Values of ``3.0`` to ``5.0`` visibly spike crit damage while values above ``5.0`` also start boosting stomps.


.. _scripts-item-criticalchance:

CriticalChance
^^^^^^^^^^^^^^

:Type: float
:Default: ``20.0``

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


.. _scripts-item-customcontextmenu:

CustomContextMenu
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-customeatsound:

CustomEatSound
^^^^^^^^^^^^^^

:Type: block (block: :ref:`sound <scripts-sound>`)
:Can be empty: True

Custom sound to play when eating or drinking this item. Set to an empty string to disable any sound from playing.


.. _scripts-item-cyclicratemultiplier:

CyclicRateMultiplier
^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``
:Minimum: ``0.0``

Only in ``Auto`` `fire mode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemode>`_. Drives the full-auto animation cycle rate via the ``autoShootSpeed`` `animation variable <https://pzwiki.net/wiki/Conditions>`_.

A higher value means more shots per second. In ``Single`` mode this field is ignored and shot speed comes from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ and `Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingtime>`_ instead.

Increase for SMG feel and decrease for heavy LMG feel.


.. _scripts-item-damagecategory:

DamageCategory
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-damagemakehole:

DamageMakeHole
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-dangerousuncooked:

DangerousUncooked
^^^^^^^^^^^^^^^^^

:Type: boolean

If true, the item will cause food poisoning when eaten raw. Used for example for raw meat. The `iron gut <https://pzwiki.net/wiki/Iron_Gut>`_ trait will stop you from getting sick from eating a raw food with the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-tags>`_ ``Egg``. The severity of the food poisoning is not impacted by traits or other criteria, only by the quantity of food you eat.


.. _scripts-item-daysfresh:

DaysFresh
^^^^^^^^^

:Type: integer
:Default: ``1000000000``

`DaysFresh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daysfresh>`_ sets how many days this food item will stay fresh with default sandbox settings. `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daystotallyrotten>`_ sets how many days this food item will take to rot.

`Icon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-icon>`_ provides the ability to set a different icon for the rotten and stale version of the food.


.. _scripts-item-daystotallyrotten:

DaysTotallyRotten
^^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``1000000000``

See parameter :ref:`DaysFresh <scripts-item-daysfresh>`.


.. _scripts-item-digitalpadlock:

DigitalPadlock
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-digtype:

DigType
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-disappearonuse:

DisappearOnUse
^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

No description provided.


.. _scripts-item-discomfortmodifier:

DiscomfortModifier
^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-displaycategory:

DisplayCategory
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-damagemodifier:

DamageModifier
^^^^^^^^^^^^^^

:Type: float

See parameter :ref:`MaxDamage <scripts-item-maxdamage>`.


.. _scripts-item-doordamage:

DoorDamage
^^^^^^^^^^

:Type: integer
:Default: ``1``
:Minimum: ``1``

Damage dealt to doors, windows, barricades and some vehicle/object hits. The damage to doors cannot go lower than 1, even in the formulas it is clamped to a minimum of 1. The formula used to retrieve the damage to doors is:

.. code-block::

   damage = max(1, DoorDamage * sharpness multiplier)

More parameters will impact the door damage based on where it is used.


.. _scripts-item-doorhitsound:

DoorHitSound
^^^^^^^^^^^^

:Type: string
:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-doubleclickrecipe:

DoubleClickRecipe
^^^^^^^^^^^^^^^^^

:Type: block (block: :ref:`craftRecipe <scripts-craftrecipe>`)

No description provided.


.. _scripts-item-dropsound:

DropSound
^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-eattime:

Eattime
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-eattype:

EatType
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-ejectammosound:

EjectAmmoSound
^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-ejectammostartsound:

EjectAmmoStartSound
^^^^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-ejectammostopsound:

EjectAmmoStopSound
^^^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-endurancechange:

enduranceChange
^^^^^^^^^^^^^^^

:Type: float

No description provided.


.. _scripts-item-endurancemod:

EnduranceMod
^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

See parameter :ref:`UseEndurance <scripts-item-useendurance>`.


.. _scripts-item-engineloudness:

engineLoudness
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-equippednosprint:

EquippedNoSprint
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-equipsound:

EquipSound
^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-evolvedrecipe:

EvolvedRecipe
^^^^^^^^^^^^^

:Type: object (object: block->>string, kv: ':', pairs: ';')

`EvolvedRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-evolvedrecipe>`_ is used to list the `evolved recipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html>`_ this item can be used in as an ingredient. The syntax needs to be as follows:

.. code-block:: cpp

   EvolvedRecipe = recipeName1:quantity1;recipeName2:quantity2;recipeName3:quantity3,

A custom flag ``cooked`` can also be added for specific recipes, for example:

.. code-block:: cpp

   EvolvedRecipe = recipeName1:quantity1|cooked;recipeName2:quantity2;recipeName3:quantity3,

Here the ``recipeName1`` will require the item to be cooked first before being used in the recipe.

A simpler syntax is also technically supported where the quantity can be omitted:

.. code-block:: cpp

   EvolvedRecipe = recipeName1;recipeName2:quantity2;recipeName3,

`EvolvedRecipeName <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-evolvedrecipename>`_ can be used to set the name of the item that will be displayed in the result item. That parameter gets ignored if the game language is not english, and due to a bug it won't even use the translation of the item so it will use the fullType.


.. _scripts-item-evolvedrecipename:

EvolvedRecipeName
^^^^^^^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`EvolvedRecipe <scripts-item-evolvedrecipe>`.


.. _scripts-item-explosionduration:

ExplosionDuration
^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-explosionpower:

ExplosionPower
^^^^^^^^^^^^^^

:Type: integer

If set above 0, the explosion will burn tiles and set fire to them based on the provided `fireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_


.. _scripts-item-explosionrange:

ExplosionRange
^^^^^^^^^^^^^^

:Type: integer

`FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_ out of 100 is a chance of the explosion to set on fire tiles and burn characters in the `ExplosionRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionrange>`_. A value above 100 means the explosion will always set on fire tiles and burn characters, while a value of 0 means it will never set on fire tiles nor burn characters. Each tiles in the explosion range will run the `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_ check independently, so a value of 50 means that on average half of the tiles in the explosion range will be set on fire.

`SmokeRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-smokerange>`_ sets the range of the smoke effect. Squares in this range also can be set on fire individually based on `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingchance>`_.

`FireRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firerange>`_ will set every tiles in the provided range on fire.

`FireStartingEnergy <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firestartingenergy>`_ is an extra check added on top of all of these whenever a fire is attempted to be started. Will set the energy of the fire which impacts how strong is is. A value of 0 means no fire is started. Vegetation tiles provide a net bonus of 50 in energy to the fire being created. The created fire will have a life expectency between 300 and 600 (unclear on the units).

`ExplosionSound <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionsound>`_ can be used to set the sound played when the explosion happens, while `ExplosionDuration <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-explosionduration>`_ can be used to set the duration of the explosion effect, which is especially useful for smoke bombs.


.. _scripts-item-explosionsound:

ExplosionSound
^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-explosiontimer:

ExplosionTimer
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fabrictype:

FabricType
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fatiguechange:

fatigueChange
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fillfromdispensersound:

FillFromDispenserSound
^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fillfromlakesound:

FillFromLakeSound
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fillfromtapsound:

FillFromTapSound
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-fillfromtoiletsound:

FillFromToiletSound
^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-firefuelratio:

FireFuelRatio
^^^^^^^^^^^^^

:Type: Unknown
:Is useless: True

No description provided.


.. _scripts-item-firemode:

FireMode
^^^^^^^^

:Type: string

`FireModePossibilities <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemodepossibilities>`_ lists the available fire modes of the weapon, and the player can automatically switch between them with the relevant keybind. `FireMode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-firemode>`_ sets the default fire mode of the weapon, which is the one it will spawn with.

The vanilla fire modes are:


* ``Single``
* ``Auto``

Other values are not supported by the game and will be considered as ``Single``.


.. _scripts-item-firemodepossibilities:

FireModePossibilities
^^^^^^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: '/')

See parameter :ref:`FireMode <scripts-item-firemode>`.


.. _scripts-item-firerange:

FireRange
^^^^^^^^^

:Type: Unknown

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-firestartingchance:

FireStartingChance
^^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-firestartingenergy:

FireStartingEnergy
^^^^^^^^^^^^^^^^^^

:Type: integer

No description provided.


.. _scripts-item-fishinglure:

FishingLure
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-flureduction:

fluReduction
^^^^^^^^^^^^

:Type: integer

When eating this food item, the player cold or pain will be reduced by the percentage of the food being eaten times respectively the values of `fluReduction <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-flureduction>`_ and `painReduction <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-painreduction>`_.


.. _scripts-item-foodsicknesschange:

FoodSicknessChange
^^^^^^^^^^^^^^^^^^

:Type: integer

Set the base food sickness change.

The amount of food sickness you get varies based on this parameter and other factors:


* burnt food will divide by 3 the amount of food sickness you get
* stale food will divide by 1.3
* rotten food will divide by 2.2
* cooked food will multiply by 1.3
* raw food provides this base value


.. _scripts-item-foodtype:

FoodType
^^^^^^^^

:Type: string

Sets the food type of the item. A translation entry needs to be made for custom types which has the key ``ContextMenu_FoodType_<type>``.

To be a valid food item to feed to animals, the item needs to be of type ``Fruits`` or ``Vegetables``.


.. _scripts-item-goodhot:

GoodHot
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-guntype:

GunType
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-havechamber:

HaveChamber
^^^^^^^^^^^

:Type: boolean
:Default: ``True``

Whether the weapon has a chamber that can hold a round in addition to its magazine.


.. _scripts-item-headcondition:

HeadCondition
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-headconditionlowerchancemultiplier:

HeadConditionLowerChanceMultiplier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-headconditionmax:

HeadConditionMax
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-hearingmodifier:

HearingModifier
^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-herbalisttype:

HerbalistType
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-hidden:

Hidden
^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-hitanglemod:

HitAngleMod
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-hitchance:

HitChance
^^^^^^^^^

:Type: integer

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


.. _scripts-item-hitchancemodifier:

HitChanceModifier
^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`HitChance <scripts-item-hitchance>`.


.. _scripts-item-hitfloorsound:

HitFloorSound
^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)
:Default: ``BatOnFloor``

No description provided.


.. _scripts-item-hitsound:

HitSound
^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)
:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-hungerchange:

HungerChange
^^^^^^^^^^^^

:Type: float

Different stats are available for food items which will impact the player's hunger, thirst, boredom etc.


* `HungerChange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-hungerchange>`_ when negative will reduce the hunger of the player, with ``100`` the maximum amount of hunger of a player
* `ThirstChange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-thirstchange>`_ when negative will reduce the thirst of the player, with ``100`` the maximum amount of thirst of a player
* `UnhappyChange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-unhappychange>`_ when positive will decrease the player's unhappiness, with ``100`` the maximum amount of unhappiness of a player
* `StressChange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-stresschange>`_ when negative will reduce the stress of the player, with ``100`` the maximum amount of stress of a player


.. _scripts-item-icon:

Icon
^^^^

:Type: string
:Default: ``None``

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

`IconsForTexture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-iconsfortexture>`_ can be used alongside `WorldStaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-worldstaticmodelsbyindex>`_ and `StaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-staticmodelsbyindex>`_ to have variant icons for different models, and all for the same item definition. See those parameters definitions for more information.


.. _scripts-item-iconcolormask:

IconColorMask
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-iconfluidmask:

IconFluidMask
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-iconsfortexture:

IconsForTexture
^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

See parameter :ref:`Icon <scripts-item-icon>`.


.. _scripts-item-idleanim:

IdleAnim
^^^^^^^^

:Type: string
:Default: ``Idle``

No description provided.


.. _scripts-item-impactsound:

ImpactSound
^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)
:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-insertallbulletsreload:

InsertAllBulletsReload
^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-insertammosound:

InsertAmmoSound
^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insertammostartsound:

InsertAmmoStartSound
^^^^^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insertammostopsound:

InsertAmmoStopSound
^^^^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insulation:

Insulation
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-inversecoughprobability:

InverseCoughProbability
^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-inversecoughprobabilitysmoker:

InverseCoughProbabilitySmoker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-isaimedfirearm:

IsAimedFirearm
^^^^^^^^^^^^^^

:Type: boolean

`IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-isaimedfirearm>`_ enables the entire aimed-firearm subsystem: ballistics controller, reticle, muzzle flash, firearm-specific condition handling and ballistics-base target detection. Without it the weapon falls back to melee sweep logic.

Set to ``true`` for any normal gun. Distinct from `Ranged <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-ranged>`_ which marks the item as a ranged weapon for the animations `conditions <https://pzwiki.net/wiki/Conditions>`_.


.. _scripts-item-isaimedhandweapon:

IsAimedHandWeapon
^^^^^^^^^^^^^^^^^

:Type: boolean

No description provided.


.. _scripts-item-iscookable:

IsCookable
^^^^^^^^^^

:Type: boolean

`IsCookable <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-iscookable>`_ marks as the item as cookable.

`MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestocook>`_ controls how many in-game minutes it takes for the food to be fully cooked. 

`MinutesToBurn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestoburn>`_ controls how many in-game minutes it takes for the food to burn. This value must be higher than `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minutestocook>`_ or your item will be instantly burnt before being fully cooked.

`RemoveNegativeEffectOnCooked <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-removenegativeeffectoncooked>`_ will remove any negative changes in thirst, unhappiness and boredom when the food is cooked.

`BadInMicrowave <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-badinmicrowave>`_ will set the unhappiness and boredom changes to ``5.0`` when cooked in a microwave.


.. _scripts-item-isdung:

IsDung
^^^^^^

:Type: boolean

No description provided.


.. _scripts-item-ishightier:

IsHighTier
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-isportable:

IsPortable
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-istelevision:

IsTelevision
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-iswatersource:

IsWaterSource
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-itemaftercleaning:

ItemAfterCleaning
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-itemtype:

ItemType
^^^^^^^^

:Type: string
:Required: True
:Allowed values: 
* ``base:alarmclock``
* ``base:alarmclockclothing``
* ``base:animal``
* ``base:clothing``
* ``base:container``
* ``base:drainable``
* ``base:food``
* ``base:key``
* ``base:literature``
* ``base:map``
* ``base:moveable``
* ``base:normal``
* ``base:radio``
* ``base:weapon``
* ``base:weaponpart``

Defines the class of the item which will impact which parameters the item can take and its properties as well as how it is used by the player. Clothing for instance will handle differently their texture and model in comparison to the other type of items, containers can hold items and weapons can be used by the player to attack and deal damage. You cannot use a custom class of item and only the ones accepted by the game.


.. _scripts-item-type:

Type
^^^^

:Type: Unknown
:Deprecated: {'replacedBy': 'ItemType', 'version': '42.13.0'}

Used to set the class of the item, which will influence parameters available.


.. _scripts-item-displayname:

DisplayName
^^^^^^^^^^^

:Type: Unknown
:Deprecated: {'description': 'Naming an item should be done with a translation entry. See the [wiki](https://pzwiki.net/wiki/DisplayName) page for more information.', 'version': '42.13.0'}

Sets the name of the item which will be displayed in-game. It's recommended to use a translation entry for this parameter to allow localization of the item name.


.. _scripts-item-itemwhendry:

ItemWhenDry
^^^^^^^^^^^

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`module`)

See parameter :ref:`Wet <scripts-item-wet>`.


.. _scripts-item-jamgunchance:

JamGunChance
^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

Base probability of a jam on each trigger pull. Final jam roml also scales with the sandbox jam multiplier, current gun condition (lower condition = higher jam chance), and low Aiming/Strength.

``JamGunChance = 1`` is already low. Setting it to ``0`` basically disables jams from this weapon. Higher values makes the gun unreliable and punishes neglecting the gun or unskilled use.


.. _scripts-item-keepondeplete:

KeepOnDeplete
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-knockbackonnodeath:

KnockBackOnNoDeath
^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-knockdownmod:

KnockdownMod
^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-learnedrecipes:

LearnedRecipes
^^^^^^^^^^^^^^

:Type: array (array of block, separator: ';')

List of `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ this item will teach the player when read.


.. _scripts-item-lightdistance:

LightDistance
^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`LightStrength <scripts-item-lightstrength>`.


.. _scripts-item-lightstrength:

LightStrength
^^^^^^^^^^^^^

:Type: float

`LightDistance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-lightdistance>`_ is used to determine the radius of the light emitted by the item. It is compared to the `Manhattan distance <https://en.wikipedia.org/wiki/Taxicab_geometry>`_ of the item to the square. The higher the value, the higher is the radius of the light.

`LightStrength <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-lightstrength>`_ will boost the light emitted.

.. code-block::

   new_light_level = current_light_level + 3 * LightStrength * (1 - clamp(dist / LightDistance, 0.0, 1.0))

The ``new_light_level`` is limited to a maximum of ``2.5``.


.. _scripts-item-lipids:

Lipids
^^^^^^

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-lowlightbonus:

LowLightBonus
^^^^^^^^^^^^^

:Type: float
:Is useless: True

No description provided.


.. _scripts-item-lvlskilltrained:

LvlSkillTrained
^^^^^^^^^^^^^^^

:Type: integer
:Default: ``-1``

No description provided.


.. _scripts-item-magazine_subject:

magazine_subject
^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

You can find a list of subjects in the `MagazineSubject <https://pz-wiki-modding.github.io/PZ-API-Docs/java/magazine_subject.html>`_.


.. _scripts-item-magazinetype:

MagazineType
^^^^^^^^^^^^

:Type: string (block: :ref:`item <scripts-item>`, with :ref:`module`)

See parameter :ref:`AmmoType <scripts-item-ammotype>`.


.. _scripts-item-makeuptype:

MakeUpType
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-manuallyremovespentrounds:

ManuallyRemoveSpentRounds
^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-map:

Map
^^^

:Type: Unknown

No description provided.


.. _scripts-item-maxammo:

MaxAmmo
^^^^^^^

:Type: integer

No description provided.


.. _scripts-item-maxcapacity:

MaxCapacity
^^^^^^^^^^^

:Type: integer
:Default: ``-1``

No description provided.


.. _scripts-item-maxchannel:

MaxChannel
^^^^^^^^^^

:Type: integer
:Default: ``108000``

No description provided.


.. _scripts-item-maxdamage:

MaxDamage
^^^^^^^^^

:Type: float
:Default: ``1.5``

Rolls the hit damage of the weapon between ``MinDamage`` and ``MaxDamage``.

`WeaponParts <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_ can modify the damage of the weapon with the `DamageModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-damagemodifier>`_ parameter. When equipped, a `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_ will increase the minimum and maximum damage of the weapon by the provided value. You are not limited to positive values, you can also add damage debuffs to the weapon by providing negative values.


.. _scripts-item-maxhitcount:

MaxHitcount
^^^^^^^^^^^

:Type: integer
:Default: ``1000``

`MaxHitcount <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxhitcount>`_ sets the maximum number of targets the weapon can hit with one attack. For ranged weapons, it will determine how many targets a single shot can hit. For melee weapons, a single swing can hit multiple targets if the relevant sandbox option allows it (Weapon Multi-Hit).

When `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-piercingbullets>`_ is ``true``\ , a shot continues past the first target and registers on collinear targets behind it. Each subsequent pierced target receives reduced damage (\ ``damage / PIERCING_BULLET_DAMAGE_REDUCTION``\ ). Targets must be within approximatively 1 degree of each other in angle to qualify.

Keep ``MaxHitcount`` to 1 for a standard rifle, and set it to 2 with `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-piercingbullets>`_ to have AP rounds behavior (M16A2 for example).


.. _scripts-item-maxitemsize:

MaxItemSize
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-maxrange:

MaxRange
^^^^^^^^

:Type: float
:Default: ``1.0``

`MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrange>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `MaxRangeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrangemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

The `MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxrange>`_ of a weapon is used to determine the maximum distance the weapon can shoot. Targets beyond ``effectiveMaxRange`` calculated with the formula below simply can't be reached, the parameter is a hard cutoff, not a penalty in damage or anything like that.

.. code-block::

   effectiveMaxRange = MaxRange + AimingPerkRangeModifier x (AimingLevel / 2.0)

All rifles from the base game have a ``AimingPerkRangeModifier`` of 0, so `aiming level <https://pzwiki.net/wiki/Aiming>`_ has no effect on the range of guns. Set it above 0 to give skilled players extra reach.


.. _scripts-item-maxrangemodifier:

MaxRangeModifier
^^^^^^^^^^^^^^^^

:Type: float

See parameter :ref:`MaxRange <scripts-item-maxrange>`.


.. _scripts-item-maxsightrange:

MaxSightRange
^^^^^^^^^^^^^

:Type: float

`MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_ define the optimal sight window, to be more specific, the distance band where hits and critical hits bonuses peak.

The `aiming skill <https://pzwiki.net/wiki/Aiming>`_ and `eagle eyed <https://pzwiki.net/wiki/Eagle_Eyed>`_ will impact these values:

.. code-block::

   effectiveMin = MinSightRange x (1 - AimingLevel / 30)
   effectiveMax = MaxSightRange x (1 + AimingLevel / 30) x (EagleEyed ? 1.2 : 1.0)

At aiming 10, the minimum shrinks by 33% and the max grows by 33%, which widens the window significantly. When the trait `Short Sighted <https://pzwiki.net/wiki/Short_Sighted>`_ is present and the character doesn't wear glasses, the ``effectiveMax`` equals ``effectiveMin``\ , making the entire bonus window disappear.

Inside the the ``effectiveMin`` and ``effectiveMax`` window, the bonus follows a `Gaussian <https://en.wikipedia.org/wiki/Bell-shaped_function>`_ with the bonus peaking at the midpoint. Aim-delay penalty is also reduced inside the window.

Below ``effectiveMin``\ , a small linear penalty is applied as the gun is not suited for point-blank. Above ``effectiveMax``\ , a growing quadratic penalty is applied, the bonus degrades rapidly past the edge.

A CQC gun should have a low `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-maxsightrange>`_ while a marksman riffle should have a high `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_ with a wide window.


.. _scripts-item-mechanicsitem:

MechanicsItem
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-mediacategory:

MediaCategory
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-medical:

Medical
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-metalvalue:

MetalValue
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-micrange:

MicRange
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-minangle:

MinAngle
^^^^^^^^

:Type: float
:Default: ``1.0``

For `IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-isaimedfirearm>`_ set to ``true``\ , the ballistics controller handles target detection and does not use `MinAngle <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minangle>`_ in the ranged hit-chance formula. These serve one narrow purpose: the ``isMeleeTargetTooCloseToShoot()`` check, detecting if a target is so close it should trigger a melee strike instead of a shot.

``MinAngle`` is a dot-product threshold (-1 to 1). Values near 1.0 mean the target must be almost directly in front to trigger the melee-swap check, while lower values widen the angle.

`AimingPerkMinAngleModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-aimingperkminanglemodifier>`_ is parsed and stored and impacts the minimum angle with the following formula:

.. code-block:: java

   effectiveMinAngle = MinAngle - AimingPerkMinAngleModifier * Aiming level


.. _scripts-item-minchannel:

MinChannel
^^^^^^^^^^

:Type: integer
:Default: ``88000``

No description provided.


.. _scripts-item-mindamage:

MinDamage
^^^^^^^^^

:Type: float

See parameter :ref:`MaxDamage <scripts-item-maxdamage>`.


.. _scripts-item-minimumswingtime:

MinimumSwingtime
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-minrange:

MinRange
^^^^^^^^

:Type: float

Hard minimum attack distance. If the target is closer than ``MinRange``\ , the ballistics controller does not register the shot and the game may force a melee swap. This is a binary threshold, not a penalty band. Separate from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-minsightrange>`_.

Long rifles should be hard to use in tight spaces. ``0.2`` to ``0.35`` is a small gap but ``0.61`` is noticeably limiting indoors.


.. _scripts-item-minsightrange:

MinSightRange
^^^^^^^^^^^^^

:Type: float

See parameter :ref:`MaxSightRange <scripts-item-maxsightrange>`.


.. _scripts-item-minutestoburn:

MinutesToBurn
^^^^^^^^^^^^^

:Type: float
:Default: ``120.0``

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-minutestocook:

MinutesToCook
^^^^^^^^^^^^^

:Type: float
:Default: ``60.0``

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-modelweaponpart:

ModelWeaponPart
^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ' ')

No description provided.


.. _scripts-item-mounton:

MountOn
^^^^^^^

:Type: array (array of string, separator: ';')

No description provided.


.. _scripts-item-multiplehitconditionaffected:

MultipleHitConditionAffected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

No description provided.


.. _scripts-item-muzzleflashmodelkey:

MuzzleFlashModelKey
^^^^^^^^^^^^^^^^^^^

:Type: string (block: :ref:`model <scripts-model>`)

No description provided.


.. _scripts-item-neckprotectionmodifier:

NeckProtectionModifier
^^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-needtobeclosedoncereload:

needtobeclosedoncereload
^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-noiseduration:

NoiseDuration
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-noiserange:

NoiseRange
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-notransmit:

NoTransmit
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-npcsoundboost:

NPCSoundBoost
^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-numberofpages:

NumberOfPages
^^^^^^^^^^^^^

:Type: integer
:Default: ``-1``

No description provided.


.. _scripts-item-numlevelstrained:

NumLevelsTrained
^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``1``

No description provided.


.. _scripts-item-onattach:

OnAttach
^^^^^^^^

:Type: callback

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-onbreak:

OnBreak
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-oncooked:

OnCooked
^^^^^^^^

:Type: callback

No description provided.


.. _scripts-item-oncreate:

OnCreate
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-ondetach:

OnDetach
^^^^^^^^

:Type: callback

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-oneat:

OnEat
^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-onlyacceptcategory:

OnlyAcceptCategory
^^^^^^^^^^^^^^^^^^

:Type: string

Makes sure only items with the specified `ItemCategory <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/itemcategory.html>`_ corresponding to the provided value of this parameter can be inserted into the container.


.. _scripts-item-openingrecipe:

OpeningRecipe
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-opensound:

OpenSound
^^^^^^^^^

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-originx:

OriginX
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-originy:

OriginY
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-originz:

originZ
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-otherhandrequire:

OtherHandRequire
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-otherhanduse:

OtherHandUse
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-packaged:

Packaged
^^^^^^^^

:Type: boolean

Setting this to ``true`` will add readable content on the food item, which will display the `nutrional information <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-calories>`_ of the food item.


.. _scripts-item-padlock:

Padlock
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-pagetowrite:

PageToWrite
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-painreduction:

painReduction
^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`fluReduction <scripts-item-flureduction>`.


.. _scripts-item-parttype:

PartType
^^^^^^^^

:Type: string

Marks the `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_ as a specific type of part. For proper tooltip of your weapon part, you need to either use one of the existing parts or use a custom part type but provide a translation entry inside `Tooltip.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#tooltip>`_ as ``Tooltip_weapon_`` followed by that part type value. For example, if you set ``PartType = customPart``\ , you need to provide a translation entry as ``Tooltip_weapon_customPart`` with the name of your part.

Here are the available part types in the base game:


* RecoilPad
* Clip
* Canon
* Scope
* Sling
* Stock

There are also some indirect part types. If the item has the `TorchCone <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-torchcone>`_ parameter, that part will be valid as a torch attachment. If it has the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtag>`_ ``base:optics``\ , it will be valid as an optics attachment.

Technically, there are other ``Tooltip_weapon_`` combination than the ones listed above, but they are not used as part types, but due to them sharing the same translation entry format, they can technically be used as a part type. It means these should not be used as part types, as you'd have to overwrite their translation entries which could brake the translation of the base game:


* Condition
* HandleCondition
* HeadCondition
* Sharpness
* Repaired
* Damage
* Unusable_at_max_exertion
* Ammo
* AmmoCount
* Range
* Type
* CanBeMountOn
* Jammed
* NoRoundChambered
* SpentRoundChambered
* SpentRounds
* ContainsClip
* NoClip
* NoMaintenanceXp


.. _scripts-item-physicsobject:

PhysicsObject
^^^^^^^^^^^^^

:Type: string (block: :ref:`item <scripts-item>`, with :ref:`module`)

Provides another item (or itself) as a throwable object. When used, the item will be thrown instead of used as an actual in hands weapon.


.. _scripts-item-piercingbullets:

PiercingBullets
^^^^^^^^^^^^^^^

:Type: boolean

See parameter :ref:`MaxHitcount <scripts-item-maxhitcount>`.


.. _scripts-item-placedsprite:

PlacedSprite
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-placemultiplesound:

PlaceMultipleSound
^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-placeonesound:

PlaceOneSound
^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-poison:

Poison
^^^^^^

:Type: boolean
:Is useless: True
:Default: ``False``

See parameter :ref:`PoisonPower <scripts-item-poisonpower>`.


.. _scripts-item-poisondetectionlevel:

PoisonDetectionLevel
^^^^^^^^^^^^^^^^^^^^

:Type: integer

See parameter :ref:`PoisonPower <scripts-item-poisonpower>`.


.. _scripts-item-poisonpower:

PoisonPower
^^^^^^^^^^^

:Type: integer

`PoisonPower <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-poisonpower>`_ defines the strength of the poison, where a positive value will make the food poisonous.

`PoisonDetectionLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-poisondetectionlevel>`_ doesn't seem to be useful, where a positive value will make it pass all the checks anyway, so increasing that value doesn't do anything.]

You can also mark an item to be shown as poisonous to the player by adding the `ItemTag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtag>`_ ``base:showpoison``.

The parameters `Poison <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-poison>`_ and `UseForPoison <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-useforpoison>`_ look unused.


.. _scripts-item-pourtype:

PourType
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-primaryanimmask:

primaryAnimMask
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-projectilecount:

Projectilecount
^^^^^^^^^^^^^^^

:Type: integer
:Default: ``1``

Only active when the weapon is ranged and has `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-rangefalloff>`_ set to ``true``. In that mode, the ballistics controller generates multiple spread projectiles. The field is never read when `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-rangefalloff>`_ is ``false``.

Inert for standard rifles. Required only for shotgun-style spread.


.. _scripts-item-projectilespread:

ProjectileSpread
^^^^^^^^^^^^^^^^

:Type: float

Projectile spread seems to be mostly a visual effect and doesn't affect the actual hit chance of the weapon. The spread will be calculated following a formula close to the following:

.. code-block::

   spread = ProjectileSpread * 10 degrees +/- 2 degrees

With the ``spread`` value being the total cone angle of the projectiles.


.. _scripts-item-projectilespreadmodifier:

ProjectileSpreadModifier
^^^^^^^^^^^^^^^^^^^^^^^^

:Type: float

No description provided.


.. _scripts-item-projectileweightcenter:

ProjectileWeightCenter
^^^^^^^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-protectfromrainwhenequipped:

ProtectFromRainWhenEquipped
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-proteins:

Proteins
^^^^^^^^

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-pushbackmod:

PushBackMod
^^^^^^^^^^^

:Type: float
:Default: ``1.0``

Scales the magnitude of the hit-reaction push applied to the target character. A higher value will increase the time the target is staggered. It will also impact the spread of blood.

Higher gives a more weighty, impactful feel.


.. _scripts-item-putinsound:

PutInSound
^^^^^^^^^^

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-rackaftershoot:

RackAfterShoot
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-racksound:

RackSound
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-rainfactor:

RainFactor
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-ranged:

Ranged
^^^^^^

:Type: boolean

See parameter :ref:`IsAimedFirearm <scripts-item-isaimedfirearm>`.


.. _scripts-item-rangefalloff:

RangeFalloff
^^^^^^^^^^^^

:Type: boolean

No description provided.


.. _scripts-item-readtype:

ReadType
^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-recoildelay:

RecoilDelay
^^^^^^^^^^^

:Type: Unknown

`RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelaymodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. Weapon attachments will add or subtract from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ directly.

Controls how long post-shot recovery takes before aim settling can begin. High values means the gun has a huge kick and forces a pause. Lower values is a flat, fast and snappy gun. `Strength <https://pzwiki.net/wiki/Strength>`_ and `aiming <https://pzwiki.net/wiki/Aiming>`_ will both reduce the recoil delay. Holding the gun one-handed will negatively impact the recoil handling. The following formula is used:

.. code-block:: java

   effectiveDelay = RecoilDelay
                 * (1 - AimingLevel / 40)
                 * (1 - (StrengthLevel * 2 - 10) / 40)
                 * (one-handed penalty: * 1.3 if primary hand only, secondary empty)

Aim countdown starts when the recoil delay counter is less than ``effectiveDelay * AimingLevel / 30``. Higher aiming also lets aim recovery start earlier in the recoil window.


.. _scripts-item-recoildelaymodifier:

RecoilDelayModifier
^^^^^^^^^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`RecoilDelay <scripts-item-recoildelay>`.


.. _scripts-item-reduceinfectionpower:

ReduceInfectionPower
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-reloadtime:

Reloadtime
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-reloadtimemodifier:

ReloadTimeModifier
^^^^^^^^^^^^^^^^^^

:Type: integer

No description provided.


.. _scripts-item-remotecontroller:

RemoteController
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-remoterange:

RemoteRange
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-removenegativeeffectoncooked:

RemoveNegativeEffectOnCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: boolean

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-removeonbroken:

RemoveOnBroken
^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

No description provided.


.. _scripts-item-removeunhappinesswhencooked:

RemoveUnhappinessWhenCooked
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-replaceinprimaryhand:

ReplaceInPrimaryHand
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-replaceinsecondhand:

ReplaceInSecondHand
^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-replaceoncooked:

ReplaceOnCooked
^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

A list of `items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ that will replace the cooked item by adding them to the player's inventory.


.. _scripts-item-replaceondeplete:

ReplaceOnDeplete
^^^^^^^^^^^^^^^^

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`module`)

When providing a `ReplaceOnDeplete <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-replaceondeplete>`_\ , the moment the item is depleted (e.g. a drainable item has no uses left anymore), it will be replaced by the item defined in this parameter. If this is empty, the item will be deleted without any replacement. This can notably be used to replace towels with a `wet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-wet>`_ towel.

`ReplaceOnExtinguish <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-replaceonextinguish>`_ on the other hand is used for `light sources items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-lightstrength>`_ to swap between the lit and unlit version of the item when it is fully drained.

`ReplaceOnRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-replaceonrotten>`_ is used for food items to swap to a different rotten version of items when they are fully rotten. This is actually not used to make an item rotten, which is natively handled by the game when providing `DaysFresh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daysfresh>`_ and `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-daystotallyrotten>`_ but instead when the item isn't necessary bad to eat after the days rotten duration, like ice cream becoming melted for example.

`ReplaceOnUse <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-replaceonuse>`_ is used whenever an item is used, to replace it with another item. Used for containers containing food items to provide the container back after the food is eaten, or for dirty items getting cleaned.


.. _scripts-item-replaceonextinguish:

ReplaceOnExtinguish
^^^^^^^^^^^^^^^^^^^

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`module`)

No description provided.


.. _scripts-item-replaceonrotten:

ReplaceOnRotten
^^^^^^^^^^^^^^^

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`module`)

No description provided.


.. _scripts-item-replaceonuse:

ReplaceOnUse
^^^^^^^^^^^^

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`module`)

No description provided.


.. _scripts-item-requireinhandorinventory:

RequireInHandOrInventory
^^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-requiresequippedbothhands:

RequiresEquippedBothHands
^^^^^^^^^^^^^^^^^^^^^^^^^

:Type: boolean

No description provided.


.. _scripts-item-researchablerecipes:

Researchablerecipes
^^^^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

No description provided.


.. _scripts-item-runanim:

RunAnim
^^^^^^^

:Type: string
:Default: ``Run``

No description provided.


.. _scripts-item-runspeedmodifier:

RunSpeedModifier
^^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-scaleworldicon:

ScaleWorldIcon
^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-scratchdefense:

ScratchDefense
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-secondaryanimmask:

secondaryAnimMask
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-sensorrange:

SensorRange
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-sharpness:

Sharpness
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-shellfallsound:

ShellFallSound
^^^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-shoutmultiplier:

ShoutMultiplier
^^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-shouttype:

ShoutType
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-skilltrained:

SkillTrained
^^^^^^^^^^^^

:Type: string
:Default: ````

No description provided.


.. _scripts-item-smokerange:

SmokeRange
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-soundgain:

SoundGain
^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-soundmap:

SoundMap
^^^^^^^^

:Type: object (object: string->>block, kv: ' ', pairs: ';')

No description provided.


.. _scripts-item-soundparameter:

SoundParameter
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-soundradius:

SoundRadius
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-soundvolume:

SoundVolume
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-spawnwith:

SpawnWith
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-spice:

Spice
^^^^^

:Type: boolean

Marks this item as a spice, which can be used in the `evolved recipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html>`_ system.


.. _scripts-item-splatbloodonnodeath:

SplatBloodOnNoDeath
^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-splatnumber:

SplatNumber
^^^^^^^^^^^

:Type: integer
:Default: ``2``

No description provided.


.. _scripts-item-splatsize:

SplatSize
^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-staticmodel:

StaticModel
^^^^^^^^^^^

:Type: block (block: :ref:`model <scripts-model>`, with :ref:`module`)

`StaticModel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-staticmodel>`_ is used to define the model of the item being held in hands. On the other hand, `WorldStaticModel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-worldstaticmodel>`_ is used to define the model of the item being placed in the world. The two models can be different, for example an item can have a handle that is up when held in hands, but down when placed in the world.

Alternatively, `StaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-staticmodelsbyindex>`_ and `WorldStaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-worldstaticmodelsbyindex>`_ can be used to define multiple models for the same item definition, which is useful for variants of the same item (e.g. a weapon with different skins). You can use `IconsForTexture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-iconsfortexture>`_ alongside those to define different `icons <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-icon>`_ for each variant. Here's an example usage with three variants of the same item:

.. code-block:: cpp

   StaticModelsByIndex = AK47;AK47_Desert;AK47_Woodland,
   WorldStaticModelsByIndex = AK47;AK47_Desert;AK47_Woodland,
   IconsForTexture = AK47;AK47_Desert;AK47_Woodland,


.. _scripts-item-staticmodelsbyindex:

StaticModelsByIndex
^^^^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

See parameter :ref:`StaticModel <scripts-item-staticmodel>`.


.. _scripts-item-stomppower:

StompPower
^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-stoppower:

StopPower
^^^^^^^^^

:Type: float
:Default: ``5.0``

See parameter :ref:`CriticalChance <scripts-item-criticalchance>`.


.. _scripts-item-stresschange:

StressChange
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-subcategory:

SubCategory
^^^^^^^^^^^

:Type: string
:Default: ````

No description provided.


.. _scripts-item-survivalgear:

SurvivalGear
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-suspensioncompression:

suspensionCompression
^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-suspensiondamping:

suspensionDamping
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-swingamountbeforeimpact:

SwingAmountBeforeImpact
^^^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-swinganim:

SwingAnim
^^^^^^^^^

:Type: string
:Default: ``Rifle``

No description provided.


.. _scripts-item-swingsound:

SwingSound
^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)
:Default: ``BaseballBatSwing``

No description provided.


.. _scripts-item-swingtime:

Swingtime
^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-tags:

Tags
^^^^

:Type: array (array of string, separator: ';')

A list of tags to assign to the item. Tags are used by the game to easily identify properties of the items from the Lua or Java. This can notably be used in `craftRecipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_.

For example:

.. code-block:: cpp

   Tags = base:egg;base:hasmetal,

You can find a list of all tags on the `PZ API Doc <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_. The pzwiki also provides a list of every items (per full type) associated to tags `here <https://pzwiki.net/wiki/Item_tag>`_.

To create a custom tag, you have to first create its definition in your mod's `registries <https://pzwiki.net/wiki/Registries>`_. In the ``registries.lua`` file, define the following by renaming the various elements to fit your mod name, id etc:

.. code-block:: lua

   YourModRegistry = {}
   YourModRegistry.YOUR_TAG_NAME = ItemTag.register("yourmodid:yourtagname")

You can then use that tag ``yourmodid:yourtagname`` in your item definition. And you can use the stored ItemTag reference ``YourModRegistry.YOUR_TAG_NAME`` in your Lua code.


.. _scripts-item-thirstchange:

ThirstChange
^^^^^^^^^^^^

:Type: float

No description provided.


.. _scripts-item-ticksperequipuse:

ticksPerEquipUse
^^^^^^^^^^^^^^^^

:Type: integer
:Default: ``30``

No description provided.


.. _scripts-item-tohitmodifier:

ToHitModifier
^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-tooltip:

Tooltip
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-torchcone:

TorchCone
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-torchdot:

TorchDot
^^^^^^^^

:Type: float
:Default: ``0.96``

No description provided.


.. _scripts-item-transmitrange:

TransmitRange
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-trap:

Trap
^^^^

:Type: boolean
:Default: ``False``

No description provided.


.. _scripts-item-treedamage:

TreeDamage
^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-triggerexplosiontimer:

triggerExplosionTimer
^^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-twohandweapon:

TwoHandWeapon
^^^^^^^^^^^^^

:Type: boolean

`TwoHandWeapon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-twohandweapon>`_ marks the weapon as a two-handed weapon. `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-recoildelay>`_ gets a x1.3 penalty when the weapon is held one-handed instead of two handed. `RequiresEquippedBothHands <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-requiresequippedbothhands>`_ enforces the equip restriction in the context menu.


.. _scripts-item-twoway:

TwoWay
^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-unequipsound:

UnequipSound
^^^^^^^^^^^^

:Type: string (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-unhappychange:

UnhappyChange
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-usedelta:

UseDelta
^^^^^^^^

:Type: float
:Default: ``0.03125``

Used to set the number of `uses <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/InventoryItem.html#getCurrentUses(>`_\ ) for the item where its durability has a value of ``1`` when full and ``0`` when empty. For example, a `base:drainable <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_ item with a ``UseDelta`` of ``0.03125`` (the default value) will have 32 uses ($1/0.03125$) before it is depleted.

When used for `Clothing items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemtype>`_\ , the ``UseDelta`` is used to indicate the amount of durability lost for `oxygen tanks <https://pzwiki.net/wiki/Oxygen_Tank>`_ for items with the `ItemTags <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ ``base:scba`` or `gas mask filters <https://pzwiki.net/wiki/Gas_Mask_Filter>`_ for items with the ItemTags ``base:gasmask``\ , ``base:respirator`` or ``base:improvisedgasmask``.

Some food items seem to be using that parameter but it doesn't seem to be used for those anywhere. There's uses for it in the Java for Drainable, Weapon and Radio items, but it doesn't seem to be limited to those.


.. _scripts-item-useendurance:

UseEndurance
^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

If ``true``\ , the weapon will consume stamina on use based on the weapon `weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weight>`_\ , `EnduranceMod <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-endurancemod>`_\ , fatigue modifiers and traits.

For guns, it is preferable to keep this as ``False``.


.. _scripts-item-useforpoison:

UseForPoison
^^^^^^^^^^^^

:Type: integer
:Default: ``0``

No description provided.


.. _scripts-item-usesbattery:

UsesBattery
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-useself:

UseSelf
^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-usewhileequipped:

UseWhileEquipped
^^^^^^^^^^^^^^^^

:Type: boolean
:Default: ``True``

No description provided.


.. _scripts-item-usewhileunequipped:

UseWhileUnequipped
^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-useworlditem:

UseWorldItem
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-vehiclepartmodel:

VehiclePartModel
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-vehicletype:

VehicleType
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-visionmodifier:

VisionModifier
^^^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-visualaid:

VisualAid
^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-waterresistance:

WaterResistance
^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-weaponhitarmoursound:

WeaponHitArmourSound
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-weaponlength:

WeaponLength
^^^^^^^^^^^^

:Type: float
:Default: ``0.4``

No description provided.


.. _scripts-item-weaponreloadtype:

WeaponReloadType
^^^^^^^^^^^^^^^^

:Type: string
:Default: ``handgun``

See parameter :ref:`AmmoType <scripts-item-ammotype>`.


.. _scripts-item-weaponsprite:

WeaponSprite
^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-weaponspritesbyindex:

WeaponSpritesByIndex
^^^^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-weaponweight:

WeaponWeight
^^^^^^^^^^^^

:Type: float
:Default: ``1.0``

No description provided.


.. _scripts-item-weight:

Weight
^^^^^^

:Type: float
:Default: ``1.0``
:Minimum: ``0.0``

`Weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weight>`_ sets the weight of the item, or more commonly refered to as a `encumbrance <https://pzwiki.net/wiki/Heavy_load>`_. `Weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_ will impact the weight of the weapon when attached. Will also impact stamina drain when `UseEndurance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-useendurance>`_ is ``true``.

`WeightEmpty <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weightempty>`_ is used to set the weight of a drainable when it is empty.

`WeightWet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-weightwet>`_ is used to set the weight of a clothing item when it is wet. The weight of the clothing item will be interpolated between ``Weight`` and ``WeightWet`` based on the `wetness <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/InventoryItem.html#getWetness(>`_\ ) of the clothing item.


.. _scripts-item-weightempty:

WeightEmpty
^^^^^^^^^^^

:Type: Unknown

See parameter :ref:`Weight <scripts-item-weight>`.


.. _scripts-item-weightwet:

WeightWet
^^^^^^^^^

:Type: Unknown

See parameter :ref:`Weight <scripts-item-weight>`.


.. _scripts-item-weightmodifier:

WeightModifier
^^^^^^^^^^^^^^

:Type: float

No description provided.


.. _scripts-item-weightreduction:

WeightReduction
^^^^^^^^^^^^^^^

:Type: integer
:Minimum: ``0``
:Maximum: ``100``

Percentage of the total contained weight in the bag that will be reduced. If the bag's content weights 10 and the reduction is 65, the bag content will only weight


.. _scripts-item-wet:

Wet
^^^

:Type: boolean

`Wet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-wet>`_ marks the item as being wet. This is notably used for towels alongside the `WetCooldown <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-wetcooldown>`_ which indicates how long the item will stay wet before drying out.

When the item is dry, it is another item marked with the parameter `ItemWhenDry <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#item-itemwhendry>`_.


.. _scripts-item-wetcooldown:

WetCooldown
^^^^^^^^^^^

:Type: float
:Default: ``-1.0``

See parameter :ref:`Wet <scripts-item-wet>`.


.. _scripts-item-wheelfriction:

wheelFriction
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-windresistance:

WindResistance
^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-withdrainable:

WithDrainable
^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-withoutdrainable:

WithoutDrainable
^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-worldobjectsprite:

WorldObjectSprite
^^^^^^^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-worldrender:

WorldRender
^^^^^^^^^^^

:Type: Unknown

No description provided.


.. _scripts-item-worldstaticmodel:

WorldStaticModel
^^^^^^^^^^^^^^^^

:Type: block (block: :ref:`model <scripts-model>`, with :ref:`module`)

See parameter :ref:`StaticModel <scripts-item-staticmodel>`.


.. _scripts-item-worldstaticmodelsbyindex:

WorldStaticModelsByIndex
^^^^^^^^^^^^^^^^^^^^^^^^

:Type: array (array of string, separator: ';')

See parameter :ref:`StaticModel <scripts-item-staticmodel>`.


