.. _scripts-item:

item
====

:Soft Override: True

The item block is used to create items in the game, from weapons to food and clothing. The parameters available in this block mostly depend on the type of item you are creating, set with `ItemType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_.

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

- :ref:`component FluidContainer <scripts-component-fluidcontainer>`
- :ref:`component Durability <scripts-component-durability>`
- :ref:`component <scripts-component>`
- :ref:`component ContextMenuConfig <scripts-component-contextmenuconfig>`



ID
--

This block can have an ID.

:Optional: False

:Can have spaces: False


ItemType parameters
-------------------

Specific parameters are only available for certain `ItemType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#ItemType>`_. The following lists for each ItemType will show what parameter is only saved for that specific ItemType script class (sub classes to `Item <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/Item.html>`_), which means using them for other classes doesn't make any sense as they will simply not be loaded in by the game.

base:container
^^^^^^^^^^^^^^

- :ref:`CanBeEquipped <scripts-item-canbeequipped>`
- :ref:`Capacity <scripts-item-capacity>`
- :ref:`WeightReduction <scripts-item-weightreduction>`

base:drainable
^^^^^^^^^^^^^^

- :ref:`cantBeConsolided <scripts-item-cantbeconsolided>`
- :ref:`ConsolidateOption <scripts-item-consolidateoption>`
- :ref:`OnCooked <scripts-item-oncooked>`
- :ref:`ReplaceOnCooked <scripts-item-replaceoncooked>`
- :ref:`Spice <scripts-item-spice>`

base:food
^^^^^^^^^

- :ref:`BadCold <scripts-item-badcold>`
- :ref:`BadInMicrowave <scripts-item-badinmicrowave>`
- :ref:`Calories <scripts-item-calories>`
- :ref:`CannedFood <scripts-item-cannedfood>`
- :ref:`Carbohydrates <scripts-item-carbohydrates>`
- :ref:`DangerousUncooked <scripts-item-dangerousuncooked>`
- :ref:`DaysFresh <scripts-item-daysfresh>`
- :ref:`DaysTotallyRotten <scripts-item-daystotallyrotten>`
- :ref:`fluReduction <scripts-item-flureduction>`
- :ref:`Lipids <scripts-item-lipids>`
- :ref:`OnCooked <scripts-item-oncooked>`
- :ref:`Packaged <scripts-item-packaged>`
- :ref:`painReduction <scripts-item-painreduction>`
- :ref:`Poison <scripts-item-poison>`
- :ref:`Proteins <scripts-item-proteins>`
- :ref:`RemoveNegativeEffectOnCooked <scripts-item-removenegativeeffectoncooked>`
- :ref:`ReplaceOnCooked <scripts-item-replaceoncooked>`
- :ref:`ReplaceOnRotten <scripts-item-replaceonrotten>`
- :ref:`Spice <scripts-item-spice>`
- :ref:`UseForPoison <scripts-item-useforpoison>`

base:literature
^^^^^^^^^^^^^^^

- :ref:`LearnedRecipes <scripts-item-learnedrecipes>`
- :ref:`LvlSkillTrained <scripts-item-lvlskilltrained>`

base:radio
^^^^^^^^^^

- :ref:`CanBeEquipped <scripts-item-canbeequipped>`

base:weapon
^^^^^^^^^^^

- :ref:`AimingPerkMinAngleModifier <scripts-item-aimingperkminanglemodifier>`
- :ref:`AimingPerkRangeModifier <scripts-item-aimingperkrangemodifier>`
- :ref:`Aimingtime <scripts-item-aimingtime>`
- :ref:`AmmoBox <scripts-item-ammobox>`
- :ref:`ClickSound <scripts-item-clicksound>`
- :ref:`ClipSize <scripts-item-clipsize>`
- :ref:`CriticalChance <scripts-item-criticalchance>`
- :ref:`CyclicRateMultiplier <scripts-item-cyclicratemultiplier>`
- :ref:`EnduranceMod <scripts-item-endurancemod>`
- :ref:`ExplosionDuration <scripts-item-explosionduration>`
- :ref:`ExplosionPower <scripts-item-explosionpower>`
- :ref:`ExplosionRange <scripts-item-explosionrange>`
- :ref:`extraDamage <scripts-item-extradamage>`
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
- :ref:`ProjectileSpread <scripts-item-projectilespread>`
- :ref:`PushBackMod <scripts-item-pushbackmod>`
- :ref:`Ranged <scripts-item-ranged>`
- :ref:`RangeFalloff <scripts-item-rangefalloff>`
- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`ShellFallSound <scripts-item-shellfallsound>`
- :ref:`StopPower <scripts-item-stoppower>`
- :ref:`SwingSound <scripts-item-swingsound>`
- :ref:`TwoHandWeapon <scripts-item-twohandweapon>`
- :ref:`UseEndurance <scripts-item-useendurance>`
- :ref:`WeaponReloadType <scripts-item-weaponreloadtype>`

base:weaponpart
^^^^^^^^^^^^^^^

- :ref:`AimingTimeModifier <scripts-item-aimingtimemodifier>`
- :ref:`CanAttach <scripts-item-canattach>`
- :ref:`CanDetach <scripts-item-candetach>`
- :ref:`ClipSizeModifier <scripts-item-clipsizemodifier>`
- :ref:`DamageModifier <scripts-item-damagemodifier>`
- :ref:`HitChanceModifier <scripts-item-hitchancemodifier>`
- :ref:`MaxRangeModifier <scripts-item-maxrangemodifier>`
- :ref:`MaxSightRange <scripts-item-maxsightrange>`
- :ref:`MinSightRange <scripts-item-minsightrange>`
- :ref:`MountOn <scripts-item-mounton>`
- :ref:`OnAttach <scripts-item-onattach>`
- :ref:`OnDetach <scripts-item-ondetach>`
- :ref:`PartType <scripts-item-parttype>`
- :ref:`ProjectileSpreadModifier <scripts-item-projectilespreadmodifier>`
- :ref:`RecoilDelayModifier <scripts-item-recoildelaymodifier>`
- :ref:`ReloadTimeModifier <scripts-item-reloadtimemodifier>`
- :ref:`WeightModifier <scripts-item-weightmodifier>`



Parameters
----------

.. _scripts-item-acceptitemfunction:

.. attribute:: AcceptItemFunction
   :noindex:

:Type: callback

No description provided.


.. _scripts-item-acceptmediatype:

.. attribute:: AcceptMediaType
   :noindex:

:Type: integer

:Default: ``-1``

No description provided.


.. _scripts-item-activateditem:

.. attribute:: ActivatedItem
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-aimingmod:

.. attribute:: AimingMod
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-aimingperkcritmodifier:

.. attribute:: AimingPerkCritModifier
   :noindex:

:Type: integer

See parameter :ref:`CriticalChance <scripts-item-criticalchance>`.


.. _scripts-item-aimingperkhitchancemodifier:

.. attribute:: AimingPerkHitChanceModifier
   :noindex:

:Type: float

See parameter :ref:`HitChance <scripts-item-hitchance>`.


.. _scripts-item-aimingperkminanglemodifier:

.. attribute:: AimingPerkMinAngleModifier
   :noindex:

:Type: float

See parameter :ref:`MinAngle <scripts-item-minangle>`.


.. _scripts-item-aimingperkrangemodifier:

.. attribute:: AimingPerkRangeModifier
   :noindex:

:Type: float

See parameter :ref:`MaxRange <scripts-item-maxrange>`.


.. _scripts-item-aimingtime:

.. attribute:: Aimingtime
   :noindex:

:Type: integer

`Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingtime>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingtimemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. The attachments directly add their `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingtimemodifier>`_ to the aiming delay.

It controls the aim-settling delay, the aiming delay counter that must tick down to 0 before the weapon is "settled". Lower values means faster target reacquisition after each shots. The primary "how snappy does this gun feel" lever for semi-automatic guns. It tick down the aiming via the following formula:

.. code-block:: java

   rate = 0.625 x gameSpeed x (1 + 0.05 x AimingLevel + (Marksman ? 0.1 : 0))

The `marksman <https://pzwiki.net/wiki/Marksman>`_ trait being no longer accessible in the recent versions of the game, the condition involving it will never be reached.

..

   Note:
   This formula might not be fully accurate as `time deltas <https://github.com/demiurgeQuantified/PZModdingGuides/blob/main/guides/GameTime.md>`_ don't appear in the formula.


While ``aimingDelay > 0``\ , both `hit chance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-hitchance>`_ and `critical chance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-criticalchance>`_ take an aim-delay penalty proportional to the remaining delay. The countdown only starts after ``recoilDelay`` has recovered, so high `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelay>`_ directly delays when ``AimingTime`` begins ticking.

On each shots or equip, the aiming delay will be increased or reduced, being impacted by aiming while in a `vehicle <https://pzwiki.net/wiki/Vehicle>`_\ , being reduced by the trait `Dextrous <https://pzwiki.net/wiki/Dextrous>`_ or increased by `All Thumbs <https://pzwiki.net/wiki/All_Thumbs>`_. The following formula is used:

.. code-block:: java

   aimingDelay = AimingTime
           * (Dextrous ? 0.8 : AllThumbs ? 1.2 : 1.0)
           * (in vehicle ? 1.5 : 1.0)

See also:

- :ref:`AimingTimeModifier <scripts-item-aimingtimemodifier>`
- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`HitChance <scripts-item-hitchance>`
- :ref:`CriticalChance <scripts-item-criticalchance>`


.. _scripts-item-aimingtimemodifier:

.. attribute:: AimingTimeModifier
   :noindex:

:Type: integer

See parameter :ref:`AimingTime <scripts-item-aimingtime>`.

See also:

- :ref:`AimingTime <scripts-item-aimingtime>`
- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`HitChance <scripts-item-hitchance>`
- :ref:`CriticalChance <scripts-item-criticalchance>`


.. _scripts-item-aimreleasesound:

.. attribute:: AimReleaseSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-alarmsound:

.. attribute:: AlarmSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-alcoholic:

.. attribute:: Alcoholic
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-alcoholpower:

.. attribute:: AlcoholPower
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-alwaysknockdown:

.. attribute:: AlwaysKnockdown
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-alwayswelcomegift:

.. attribute:: AlwaysWelcomeGift
   :noindex:

:Type: boolean

:Is useless: True

No description provided.


.. _scripts-item-ammobox:

.. attribute:: AmmoBox
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

Used to indicate the type of ammo box associated to the weapon. This is mostly used to spawn this type of ammo box alongside the gun.

See also:

- :ref:`AmmoType <scripts-item-ammotype>`
- :ref:`MaxAmmo <scripts-item-maxammo>`


.. _scripts-item-ammotype:

.. attribute:: AmmoType
   :noindex:

:Type: string

`AmmoType <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-ammotype>`_ indicates what ammo is consumed when shooting, but it also determines tracer and hit-reaction sound lookups. The value needs to reference the `registries <https://pzwiki.net/wiki/Registries>`_ entry of the ammo you want to use.

Here is a list of some of the ammo types available in the vanilla game:


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

See also:

- :ref:`MagazineType <scripts-item-magazinetype>`
- :ref:`MaxAmmo <scripts-item-maxammo>`
- :ref:`WeaponReloadType <scripts-item-weaponreloadtype>`
- :ref:`AmmoBox <scripts-item-ammobox>`


.. _scripts-item-anglefalloff:

.. attribute:: AngleFalloff
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-animalfeedtype:

.. attribute:: AnimalFeedType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-attachmentreplacement:

.. attribute:: AttachmentReplacement
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-attachmentsprovided:

.. attribute:: AttachmentsProvided
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-attachmenttype:

.. attribute:: AttachmentType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-badcold:

.. attribute:: BadCold
   :noindex:

:Type: boolean




.. _scripts-item-badinmicrowave:

.. attribute:: BadInMicrowave
   :noindex:

:Type: boolean

No description provided.


.. _scripts-item-bandagepower:

.. attribute:: BandagePower
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-basespeed:

.. attribute:: BaseSpeed
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-basevolumerange:

.. attribute:: BaseVolumeRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-bitedefense:

.. attribute:: BiteDefense
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-bloodlocation:

.. attribute:: BloodLocation
   :noindex:

:Type: array (array of string, separator: ';')

:Allowed values:    ``Apron`` | ``Bag`` | ``Foot_L`` | ``Foot_R`` | ``ForeArm_L`` | ``ForeArm_R`` | ``FullHelmet`` | ``Groin`` | ``Hand_L`` | ``Hand_R`` | ``Hands`` | ``Head`` | ``Jacket`` | ``JumperNoSleeves`` | ``Jumper`` | ``LongJacket`` | ``LowerArms`` | ``LowerBody`` | ``LowerLeg_L`` | ``LowerLeg_R`` | ``LowerLegs`` | ``Neck`` | ``ShirtLongSleeves`` | ``ShirtNoSleeves`` | ``Shirt`` | ``Shoes`` | ``ShortsShort`` | ``Trousers`` | ``UpperArm_L`` | ``UpperArm_R`` | ``UpperArms`` | ``UpperBody`` | ``UpperLeg_L`` | ``UpperLeg_R`` | ``UpperLegs``

No description provided.


.. _scripts-item-bodylocation:

.. attribute:: BodyLocation
   :noindex:

:Type: Unknown

Used to define which location on the human character this clothing item can be worn. Needs to be a valid `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_body_locations.html>`_ value. You can also create new ones via `registries <https://pzwiki.net/wiki/Registries>`_.


.. _scripts-item-book_subject:

.. attribute:: book_subject
   :noindex:

:Type: array (array of string, separator: ';')

Add a subject to the litterature item. The value needs to be an array of `BookSubject <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/BookSubject.html>`_ values.

`book_subject <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-book-subject>`_ is for books while `magazine_subject <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-magazine-subject>`_ is for magazines.

This is notably used to pick a random book or magazine when spawning a book.


.. _scripts-item-boredomchange:

.. attribute:: BoredomChange
   :noindex:

:Type: integer

When negative, the item being consumed will reduce the `player's boredom <https://pzwiki.net/wiki/Bored>`_\ , with ``100`` the maximum amount of boredom of a player.

See also:

- :ref:`HungerChange <scripts-item-hungerchange>`
- :ref:`ThirstChange <scripts-item-thirstchange>`
- :ref:`UnhappyChange <scripts-item-unhappychange>`
- :ref:`StressChange <scripts-item-stresschange>`


.. _scripts-item-brakeforce:

.. attribute:: brakeForce
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-breaksound:

.. attribute:: BreakSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-bringtobearsound:

.. attribute:: BringToBearSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-bulletdefense:

.. attribute:: BulletDefense
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-bullethitarmoursound:

.. attribute:: BulletHitArmourSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-calories:

.. attribute:: Calories
   :noindex:

:Type: float

The following stats are directly linked to the player's `nutrition <https://pzwiki.net/wiki/Nutrition>`_\ , which are hidden stats that will impact the player's weight gains and more (positive values will increase the stat when eaten):


* `Calories <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-calories>`_
* `Carbohydrates <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-carbohydrates>`_
* `Lipids <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-lipids>`_
* `Proteins <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-proteins>`_


.. _scripts-item-canattach:

.. attribute:: CanAttach
   :noindex:

:Type: callback

`CanAttach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-canattach>`_ and `CanDetach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-candetach>`_ are used to define whenever a `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_ can be respectively attached or detached to and from a `HandWeapon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_.

`OnAttach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-onattach>`_ and `OnDetach <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-ondetach>`_ are used to define a callback function which will be called when the weapon part is attached or detached from the weapon.


.. _scripts-item-canbandage:

.. attribute:: CanBandage
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canbarricade:

.. attribute:: CanBarricade
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canbeequipped:

.. attribute:: CanBeEquipped
   :noindex:

:Type: Unknown

Needs to reference a valid `BodyLocation <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-bodylocation>`_ value which will serve as the equipment location.


.. _scripts-item-canbeplaced:

.. attribute:: CanBePlaced
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canberemote:

.. attribute:: CanBeRemote
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canbereused:

.. attribute:: CanBeReused
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canbewrite:

.. attribute:: CanBeWrite
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-candetach:

.. attribute:: CanDetach
   :noindex:

:Type: callback

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-canhaveholes:

.. attribute:: CanHaveHoles
   :noindex:

:Type: boolean

:Default: ``True``

Used to define whenever this item can get holes in it.


.. _scripts-item-cannedfood:

.. attribute:: CannedFood
   :noindex:

:Type: boolean

`CannedFood <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-cannedfood>`_ will mark the item as a canned food which will impact how it is spawned in the world. It will also impact the type of item where instead of being "Food" it will be "CannedFood".


.. _scripts-item-canstack:

.. attribute:: CanStack
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canstorewater:

.. attribute:: CanStoreWater
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-cantattackwithlowestendurance:

.. attribute:: CantAttackWithLowestEndurance
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-cantbeconsolided:

.. attribute:: cantBeConsolided
   :noindex:

:Type: boolean

See parameter :ref:`ConsolidateOption <scripts-item-consolidateoption>`.


.. _scripts-item-cantbefrozen:

.. attribute:: CantBeFrozen
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-canteat:

.. attribute:: CantEat
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-capacity:

.. attribute:: Capacity
   :noindex:

:Type: integer

:Default: ``-1``

:Maximum: ``50``

Sets the capacity of the container. This value is limited to a maximum of 50 minus its own `weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-weight>`_. The weight of the bag will follow the formula ``equippedWeight = weight * EquippedOrWornEncumbranceMultiplier + contentWeight * (1.0 - weightReduction / 100)``.


.. _scripts-item-carbohydrates:

.. attribute:: Carbohydrates
   :noindex:

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-categories:

.. attribute:: Categories
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-chancetofall:

.. attribute:: ChanceToFall
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-chancetospawndamaged:

.. attribute:: ChanceToSpawnDamaged
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-clicksound:

.. attribute:: ClickSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Default: ``Stormy9mmClick``

No description provided.


.. _scripts-item-clipsize:

.. attribute:: ClipSize
   :noindex:

:Type: integer

:Is useless: True

No description provided.


.. _scripts-item-clipsizemodifier:

.. attribute:: ClipSizeModifier
   :noindex:

:Type: integer

:Is useless: True

No description provided.


.. _scripts-item-closekillmove:

.. attribute:: CloseKillMove
   :noindex:

:Type: Unknown

Used to whenever this weapon can be used to do a close kill move, like knives to assassinate in the back.


.. _scripts-item-closesound:

.. attribute:: CloseSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-clothingextrasubmenu:

.. attribute:: ClothingExtraSubmenu
   :noindex:

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-clothingitem:

.. attribute:: ClothingItem
   :noindex:

:Type: Unknown

``ClothingItem`` references the clothing defined inside the `clothing.xml <https://pzwiki.net/wiki/Clothing.xml>`_ file. ``ClothingExtraSubmenu`` will define the name of the context menu option to equip the clothing item.

``ClothingItemExtra`` and ``ClothingItemExtraOption`` are used to define additional clothing equip options, they reference another item script block.


.. _scripts-item-clothingitemextra:

.. attribute:: ClothingItemExtra
   :noindex:

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-clothingitemextraoption:

.. attribute:: ClothingItemExtraOption
   :noindex:

:Type: Unknown

See parameter :ref:`ClothingItem <scripts-item-clothingitem>`.


.. _scripts-item-colorblue:

.. attribute:: ColorBlue
   :noindex:

:Type: integer

:Default: ``255``

No description provided.


.. _scripts-item-colorgreen:

.. attribute:: ColorGreen
   :noindex:

:Type: integer

:Default: ``255``

No description provided.


.. _scripts-item-colorred:

.. attribute:: ColorRed
   :noindex:

:Type: integer

:Default: ``255``

No description provided.


.. _scripts-item-combatspeedmodifier:

.. attribute:: CombatSpeedModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-conditionaffectscapacity:

.. attribute:: ConditionAffectsCapacity
   :noindex:

:Type: Unknown

Set whenever condition of the item can impact the capacity value of the container.


.. _scripts-item-conditionlowerchanceonein:

.. attribute:: ConditionLowerChanceOneIn
   :noindex:

:Type: integer

:Default: ``10``

`ConditionLowerChanceOneIn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-conditionlowerchanceonein>`_ impacts the durability of the item, reducing the value
used to calculate the chance by doing ``chance = 1/ConditionLowerChanceOneIn``\ ,
which means increasing this parameter value will reduce the chance to damage the
item.

`ConditionMax <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-conditionmax>`_ sets the total durability pool, starting condition and repair ceiling. Make these two parameters high for robust military rifles, and low for a cheap civilian gun.


.. _scripts-item-conditionloweroffroad:

.. attribute:: ConditionLowerOffroad
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-conditionlowerstandard:

.. attribute:: ConditionLowerStandard
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-conditionmax:

.. attribute:: ConditionMax
   :noindex:

:Type: integer

:Default: ``10``

See parameter :ref:`ConditionLowerChanceOneIn <scripts-item-conditionlowerchanceonein>`.


.. _scripts-item-consolidateoption:

.. attribute:: ConsolidateOption
   :noindex:

:Type: Unknown

By setting `cantBeConsolided <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-cantbeconsolided>`_ to ``false`` and providing a `ConsolidateOption <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-consolidateoption>`_ value, the item can be marked to merge its uses with other items of the same type in the inventory. This requires the item to be `Drainable type <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_.

The ConsolidateOption value needs to be a translation key which will be passed through `getText <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/core/Translator.html#getText(java.lang.String>`_\ ) to retrieve the translation value. The vanilla drainables (duct tape, wires, matches...) use the translation key ``ContextMenu_Merge`` which outputs a text 'Add to'.


.. _scripts-item-cookingsound:

.. attribute:: CookingSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

Custom sound to play when cooking this item.


.. _scripts-item-corpsesicknessdefense:

.. attribute:: CorpseSicknessDefense
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-cosmetic:

.. attribute:: Cosmetic
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-count:

.. attribute:: Count
   :noindex:

:Type: integer

:Default: ``1``

The parameter is unused in the game scripts, unclear what it is used for.


.. _scripts-item-critdmgmultiplier:

.. attribute:: CritDmgMultiplier
   :noindex:

:Type: float

:Default: ``2.0``

Multiplier applied to the damage of a hit if it is a critical hit, applied inside `IsoGameCharacter.Hit() <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/IsoGameCharacter.html#Hit(zombie.inventory.types.HandWeapon,zombie.characters.IsoGameCharacter,float,boolean,float,boolean>`_\ ). Two types of crits can trigger:


* A normal crit: ``damage *= max(2.0, CritDmgMultiplier)``
* Aim-at-floor stomp (melee only): ``damage *= max(5.0, CritDmgMultiplier)``

The default value of the ``HandWeapon`` class is ``2.0``. Values of ``3.0`` to ``5.0`` visibly spike crit damage while values above ``5.0`` also start boosting stomps.


.. _scripts-item-criticalchance:

.. attribute:: CriticalChance
   :noindex:

:Type: float

:Default: ``20.0``

`CriticalChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-criticalchance>`_ sets the base critical hit chance of the weapon. The final ``CriticalChance`` value after all applied bonuses and penalties have been applied is compared on a 0-100 roll.

Below is a table listing the different elements which can influence the critical hit chance of a weapon:

.. list-table::
   :header-rows: 1

   * - Element
     - Type
     - Description
     - Formula
   * - `AimingPerkCritModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingperkcritmodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's critical hit chance by adding the following to the ``CriticalChance`` value.
     - ``CriticalChance += AimingPerkCritModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result. The aim delay penalty depends on `Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingtime>`_
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


For PvP targets, the entire formula is bypassed and `StopPower <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-stoppower>`_ is used instead. ``StopPower`` is never used against non-player targets.

.. code-block::

   CriticalChance = StopPower * ( 1 + Aiming level / 15)

``CriticalChance`` sets the floor for unskilled players while ``AimingPerkCritModifier`` rewards more or less the character ability to aim. High modified and low base chance means the weapon is a skill-gated crit machine, making the weapon a sort of "experts" weapon.

See also:

- :ref:`AimingTime <scripts-item-aimingtime>`
- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`HitChance <scripts-item-hitchance>`
- :ref:`MinSightRange <scripts-item-minsightrange>`
- :ref:`MaxSightRange <scripts-item-maxsightrange>`
- :ref:`StopPower <scripts-item-stoppower>`


.. _scripts-item-customcontextmenu:

.. attribute:: CustomContextMenu
   :noindex:

:Type: translation

No description provided.


.. _scripts-item-customeatsound:

.. attribute:: CustomEatSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Can be empty: True

Custom sound to play when eating or drinking this item. Set to an empty string to disable any sound from playing.


.. _scripts-item-cyclicratemultiplier:

.. attribute:: CyclicRateMultiplier
   :noindex:

:Type: float

:Default: ``1.0``

:Minimum: ``0.0``

Only in ``Auto`` `fire mode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firemode>`_. Drives the full-auto animation cycle rate via the ``autoShootSpeed`` `animation variable <https://pzwiki.net/wiki/Conditions>`_.

A higher value means more shots per second. In ``Single`` mode this field is ignored and shot speed comes from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelay>`_ and `Aimingtime <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingtime>`_ instead.

Increase for SMG feel and decrease for heavy LMG feel.


.. _scripts-item-damagecategory:

.. attribute:: DamageCategory
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-damagemakehole:

.. attribute:: DamageMakeHole
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-damagemodifier:

.. attribute:: DamageModifier
   :noindex:

:Type: float

See parameter :ref:`MaxDamage <scripts-item-maxdamage>`.


.. _scripts-item-dangerousuncooked:

.. attribute:: DangerousUncooked
   :noindex:

:Type: boolean

If true, the item will cause food poisoning when eaten raw. Used for example for raw meat. The `iron gut <https://pzwiki.net/wiki/Iron_Gut>`_ trait will stop you from getting sick from eating a raw food with the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-tags>`_ ``Egg``. The severity of the food poisoning is not impacted by traits or other criteria, only by the quantity of food you eat.


.. _scripts-item-daysfresh:

.. attribute:: DaysFresh
   :noindex:

:Type: integer

:Default: ``1000000000``

`DaysFresh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-daysfresh>`_ sets how many days this food item will stay fresh with default sandbox settings. `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-daystotallyrotten>`_ sets how many days this food item will take to rot.

`Icon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-icon>`_ provides the ability to set a different icon for the rotten and stale version of the food.


.. _scripts-item-daystotallyrotten:

.. attribute:: DaysTotallyRotten
   :noindex:

:Type: integer

:Default: ``1000000000``

See parameter :ref:`DaysFresh <scripts-item-daysfresh>`.


.. _scripts-item-digitalpadlock:

.. attribute:: DigitalPadlock
   :noindex:

:Type: boolean

Looks unused by the game.


.. _scripts-item-digtype:

.. attribute:: DigType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-disappearonuse:

.. attribute:: DisappearOnUse
   :noindex:

:Type: boolean

:Default: ``True``

No description provided.


.. _scripts-item-discomfortmodifier:

.. attribute:: DiscomfortModifier
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-displaycategory:

.. attribute:: DisplayCategory
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-displayname:

.. attribute:: DisplayName
   :noindex:

:Type: Unknown

:Deprecated: {'description': 'Naming an item should be done with a translation entry. See the [wiki](https://pzwiki.net/wiki/DisplayName) page for more information.', 'version': '42.13.0'}

Sets the name of the item which will be displayed in-game. It's recommended to use a translation entry for this parameter to allow localization of the item name.


.. _scripts-item-doordamage:

.. attribute:: DoorDamage
   :noindex:

:Type: integer

:Default: ``1``

:Minimum: ``1``

Damage dealt to doors, windows, barricades and some vehicle/object hits. The damage to doors cannot go lower than 1, even in the formulas it is clamped to a minimum of 1. The formula used to retrieve the damage to doors is:

.. code-block::

   damage = max(1, DoorDamage * sharpness multiplier)

More parameters will impact the door damage based on where it is used.


.. _scripts-item-doorhitsound:

.. attribute:: DoorHitSound
   :noindex:

:Type: string

:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-doubleclickrecipe:

.. attribute:: DoubleClickRecipe
   :noindex:

:Type: block (block: :ref:`craftRecipe <scripts-craftrecipe>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-item-dropsound:

.. attribute:: DropSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-eattime:

.. attribute:: Eattime
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-eattype:

.. attribute:: EatType
   :noindex:

:Type: string

Used mostly on the Lua side and in `AnimNodes <https://pzwiki.net/wiki/AnimNode>`_ as a `condition <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/animNode.html#m-conditions>`_ to mark what animation to use when eating this item. Based on the type of item, this is directly applied to the ``FoodType`` animation condition.

Here's a small summary of some special conditions:


* ``Pot`` and ``PotForged`` are applied directly, and will force the item to be held in the right hand and removing other items from the left hand, meant for a pot held with two hands.
* ``popcan`` forces drinking `timed action <https://pzwiki.net/wiki/Timed_Action_(Lua>`_\ ) ``maxTime`` to a flat ``160``.
* ``Candrink`` will make the player uses an item with the  spoon or `fork <https://pzwiki.net/wiki/Fork#Eating>`_ tag in their inventory. A "scraping" sound will also be played when using an utensil and 70% of the eating action is passed.
* ``Plate`` can also use a fork or spoon.
* ``2handbowl`` will use only spoons in the player inventory.

There also exists more generic ones:


* ``2hand``
* ``plate`` (different than ``Plate``\ )
* ``EatSmall``
* ``EatBox``

You can use any custom value which will be passed to the ``FoodType`` condition.


.. _scripts-item-ejectammosound:

.. attribute:: EjectAmmoSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-ejectammostartsound:

.. attribute:: EjectAmmoStartSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-ejectammostopsound:

.. attribute:: EjectAmmoStopSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-endurancechange:

.. attribute:: enduranceChange
   :noindex:

:Type: float

No description provided.


.. _scripts-item-endurancemod:

.. attribute:: EnduranceMod
   :noindex:

:Type: float

:Default: ``1.0``

See parameter :ref:`UseEndurance <scripts-item-useendurance>`.


.. _scripts-item-engineloudness:

.. attribute:: engineLoudness
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-equippednosprint:

.. attribute:: EquippedNoSprint
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-equipsound:

.. attribute:: EquipSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-evolvedrecipe:

.. attribute:: EvolvedRecipe
   :noindex:

:Type: object (object: block->>string, kv: ':', pairs: ';')

`EvolvedRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-evolvedrecipe>`_ is used to list the `evolved recipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html>`_ this item can be used in as an ingredient. The syntax needs to be as follows:

.. code-block:: cpp

   EvolvedRecipe = recipeName1:quantity1;recipeName2:quantity2;recipeName3:quantity3,

A custom flag ``cooked`` can also be added for specific recipes, for example:

.. code-block:: cpp

   EvolvedRecipe = recipeName1:quantity1|cooked;recipeName2:quantity2;recipeName3:quantity3,

Here the ``recipeName1`` will require the item to be cooked first before being used in the recipe.

A simpler syntax is also technically supported where the quantity can be omitted:

.. code-block:: cpp

   EvolvedRecipe = recipeName1;recipeName2:quantity2;recipeName3,

`EvolvedRecipeName <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-evolvedrecipename>`_ can be used to set the name of the item that will be displayed in the result item. That parameter gets ignored if the game language is not english, and due to a bug it won't even use the translation of the item so it will use the fullType.


.. _scripts-item-evolvedrecipename:

.. attribute:: EvolvedRecipeName
   :noindex:

:Type: Unknown

See parameter :ref:`EvolvedRecipe <scripts-item-evolvedrecipe>`.


.. _scripts-item-explosionduration:

.. attribute:: ExplosionDuration
   :noindex:

:Type: integer

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-explosionpower:

.. attribute:: ExplosionPower
   :noindex:

:Type: integer

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-explosionrange:

.. attribute:: ExplosionRange
   :noindex:

:Type: integer

`FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firestartingchance>`_ out of 100 is a chance of the explosion to set on fire tiles and burn characters in the `ExplosionRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-explosionrange>`_. A value above 100 means the explosion will always set on fire tiles and burn characters, while a value of 0 means it will never set on fire tiles nor burn characters. Each tiles in the explosion range will run the `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firestartingchance>`_ check independently, so a value of 50 means that on average half of the tiles in the explosion range will be set on fire.

If `ExplosionPower <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-explosionpower>`_ is set above 0, the explosion will burn tiles and set fire to them based on the provided `fireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firestartingchance>`_.

`extraDamage <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-extradamage>`_ is used to add a net bonus damage dealt by the trap.

The damage the trap deals is calculated as follows:

.. code-block::

   damage = random(explosionPower/20, explosionPower/20 * 2) + extraDamage

`SmokeRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-smokerange>`_ sets the range of the smoke effect. Squares in this range also can be set on fire individually based on `FireStartingChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firestartingchance>`_.

`FireRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firerange>`_ will set every tiles in the provided range on fire.

`FireStartingEnergy <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firestartingenergy>`_ is an extra check added on top of all of these whenever a fire is attempted to be started. Will set the energy of the fire which impacts how strong is is. A value of 0 means no fire is started. Vegetation tiles provide a net bonus of 50 in energy to the fire being created. The created fire will have a life expectency between 300 and 600 (unclear on the units).

`ExplosionSound <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-explosionsound>`_ can be used to set the sound played when the explosion happens, while `ExplosionDuration <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-explosionduration>`_ can be used to set the duration of the explosion effect, which is especially useful for smoke bombs.


.. _scripts-item-explosionsound:

.. attribute:: ExplosionSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-explosiontimer:

.. attribute:: ExplosionTimer
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-extradamage:

.. attribute:: extraDamage
   :noindex:

:Type: float

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-fabrictype:

.. attribute:: FabricType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-fatiguechange:

.. attribute:: fatigueChange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-fillfromdispensersound:

.. attribute:: FillFromDispenserSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-fillfromlakesound:

.. attribute:: FillFromLakeSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-fillfromtapsound:

.. attribute:: FillFromTapSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-fillfromtoiletsound:

.. attribute:: FillFromToiletSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-firefuelratio:

.. attribute:: FireFuelRatio
   :noindex:

:Type: Unknown

:Is useless: True

No description provided.


.. _scripts-item-firemode:

.. attribute:: FireMode
   :noindex:

:Type: string

`FireModePossibilities <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firemodepossibilities>`_ lists the available fire modes of the weapon, and the player can automatically switch between them with the relevant keybind. `FireMode <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-firemode>`_ sets the default fire mode of the weapon, which is the one it will spawn with.

The vanilla fire modes are:


* ``Single``
* ``Auto``

Other values are not supported by the game and will be considered as ``Single``.


.. _scripts-item-firemodepossibilities:

.. attribute:: FireModePossibilities
   :noindex:

:Type: array (array of string, separator: '/')

See parameter :ref:`FireMode <scripts-item-firemode>`.


.. _scripts-item-firerange:

.. attribute:: FireRange
   :noindex:

:Type: Unknown

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-firestartingchance:

.. attribute:: FireStartingChance
   :noindex:

:Type: integer

See parameter :ref:`ExplosionRange <scripts-item-explosionrange>`.


.. _scripts-item-firestartingenergy:

.. attribute:: FireStartingEnergy
   :noindex:

:Type: integer

No description provided.


.. _scripts-item-fishinglure:

.. attribute:: FishingLure
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-flureduction:

.. attribute:: fluReduction
   :noindex:

:Type: integer

When eating this food item, the player cold or pain will be reduced by the percentage of the food being eaten times respectively the values of `fluReduction <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-flureduction>`_ and `painReduction <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-painreduction>`_.


.. _scripts-item-foodsicknesschange:

.. attribute:: FoodSicknessChange
   :noindex:

:Type: integer

Set the base food sickness change.

The amount of food sickness you get varies based on this parameter and other factors:


* burnt food will divide by 3 the amount of food sickness you get
* stale food will divide by 1.3
* rotten food will divide by 2.2
* cooked food will multiply by 1.3
* raw food provides this base value


.. _scripts-item-foodtype:

.. attribute:: FoodType
   :noindex:

:Type: string

Sets the food type of the item. A translation entry needs to be made for custom types which has the key ``ContextMenu_FoodType_<type>``.

To be a valid food item to feed to animals, the item needs to be of type ``Fruits`` or ``Vegetables``.


.. _scripts-item-goodhot:

.. attribute:: GoodHot
   :noindex:

:Type: Unknown

`GoodHot <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-goodhot>`_ reduces by a flat 2 the happiness change when eating this food hot. On the other hand, `BadCold <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-badcold>`_ increases by a flat 2 the unhappiness change when eating this food cold.


.. _scripts-item-guntype:

.. attribute:: GunType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-havechamber:

.. attribute:: HaveChamber
   :noindex:

:Type: boolean

:Default: ``True``

Whether the weapon has a chamber that can hold a round in addition to its magazine.


.. _scripts-item-headcondition:

.. attribute:: HeadCondition
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-headconditionlowerchancemultiplier:

.. attribute:: HeadConditionLowerChanceMultiplier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-headconditionmax:

.. attribute:: HeadConditionMax
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-hearingmodifier:

.. attribute:: HearingModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-herbalisttype:

.. attribute:: HerbalistType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-hidden:

.. attribute:: Hidden
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-hitanglemod:

.. attribute:: HitAngleMod
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-hitchance:

.. attribute:: HitChance
   :noindex:

:Type: integer

`HitChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-hitchance>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `HitChanceModified <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-hitchancemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

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
   * - `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingperkhitchancemodifier>`_ and `aiming skill <https://pzwiki.net/wiki/Aiming>`_ of the character
     - Weapon parameter
     - The aiming level of the character impacts the player's hit chance.
     - ``HitChance += AimingPerkHitChanceModifier * Aiming level``
   * - Sight bonus / penalty
     - Weapon parameter
     - In the formula, ``sightWindowBonus`` refers to the bonus from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxsightrange>`_. ``sightlessBonus`` on the other hand is a simpler parameter which uses a distance falloff when there is not active sight. The best path is used for the better result.
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

At point-blank range, all combined penalties are scaled toward zero, so close shots are always more forgiving. The `HitChance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-hitchance>`_ parameter will set the floor for all players while `AimingPerkHitChanceModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingperkhitchancemodifier>`_ will increase accuracy with the level of aiming of the player. Low base and high modifier makes the gun terrible while unskilled but excellent with investment in aiming.


.. _scripts-item-hitchancemodifier:

.. attribute:: HitChanceModifier
   :noindex:

:Type: integer

See parameter :ref:`HitChance <scripts-item-hitchance>`.


.. _scripts-item-hitfloorsound:

.. attribute:: HitFloorSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Default: ``BatOnFloor``

No description provided.


.. _scripts-item-hitsound:

.. attribute:: HitSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-hungerchange:

.. attribute:: HungerChange
   :noindex:

:Type: float

When negative, the item being consumed will reduce the `player's hunger <https://pzwiki.net/wiki/Hungry>`_\ , with ``100`` the maximum amount of hunger of a player.

See also:

- :ref:`UnhappyChange <scripts-item-unhappychange>`
- :ref:`ThirstChange <scripts-item-thirstchange>`
- :ref:`StressChange <scripts-item-stresschange>`
- :ref:`BoredomChange <scripts-item-boredomchange>`


.. _scripts-item-icon:

.. attribute:: Icon
   :noindex:

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


* ``Rotten`` or ``Spoiled`` for food that has rotten, meaning has passed the `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-daystotallyrotten>`_ value.
* ``Cooked`` for food that has been cooked, meaning has passed the `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minutestocook>`_ value.
* ``Overdone`` or ``Burnt`` for food that has been cooked to the point of burning, meaning has passed the `MinutesToBurn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minutestoburn>`_ value.

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

`IconsForTexture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-iconsfortexture>`_ can be used alongside `WorldStaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-worldstaticmodelsbyindex>`_ and `StaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-staticmodelsbyindex>`_ to have variant icons for different models, and all for the same item definition. See those parameters definitions for more information.


.. _scripts-item-iconcolormask:

.. attribute:: IconColorMask
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-iconfluidmask:

.. attribute:: IconFluidMask
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-iconsfortexture:

.. attribute:: IconsForTexture
   :noindex:

:Type: array (array of string, separator: ';')

See parameter :ref:`Icon <scripts-item-icon>`.

See also:

- :ref:`StaticModelsByIndex <scripts-item-staticmodelsbyindex>`
- :ref:`WorldStaticModelsByIndex <scripts-item-worldstaticmodelsbyindex>`


.. _scripts-item-idleanim:

.. attribute:: IdleAnim
   :noindex:

:Type: string

:Default: ``Idle``

No description provided.


.. _scripts-item-impactsound:

.. attribute:: ImpactSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Default: ``BaseballBatHit``

No description provided.


.. _scripts-item-insertallbulletsreload:

.. attribute:: InsertAllBulletsReload
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-insertammosound:

.. attribute:: InsertAmmoSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insertammostartsound:

.. attribute:: InsertAmmoStartSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insertammostopsound:

.. attribute:: InsertAmmoStopSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-insulation:

.. attribute:: Insulation
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-inversecoughprobability:

.. attribute:: InverseCoughProbability
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-inversecoughprobabilitysmoker:

.. attribute:: InverseCoughProbabilitySmoker
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-isaimedfirearm:

.. attribute:: IsAimedFirearm
   :noindex:

:Type: boolean

`IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-isaimedfirearm>`_ enables the entire aimed-firearm subsystem: ballistics controller, reticle, muzzle flash, firearm-specific condition handling and ballistics-base target detection. Without it the weapon falls back to melee sweep logic.

Set to ``true`` for any normal gun. Distinct from `Ranged <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-ranged>`_ which marks the item as a ranged weapon for the animations `conditions <https://pzwiki.net/wiki/Conditions>`_.


.. _scripts-item-isaimedhandweapon:

.. attribute:: IsAimedHandWeapon
   :noindex:

:Type: boolean

No description provided.


.. _scripts-item-iscookable:

.. attribute:: IsCookable
   :noindex:

:Type: boolean

`IsCookable <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-iscookable>`_ marks as the item as cookable.

`MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minutestocook>`_ controls how many in-game minutes it takes for the food to be fully cooked. 

`MinutesToBurn <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minutestoburn>`_ controls how many in-game minutes it takes for the food to burn. This value must be higher than `MinutesToCook <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minutestocook>`_ or your item will be instantly burnt before being fully cooked.

`RemoveNegativeEffectOnCooked <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-removenegativeeffectoncooked>`_ will remove any negative changes in thirst, unhappiness and boredom when the food is cooked.

`BadInMicrowave <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-badinmicrowave>`_ will set the unhappiness and boredom changes to ``5.0`` when cooked in a microwave.


.. _scripts-item-isdung:

.. attribute:: IsDung
   :noindex:

:Type: boolean

No description provided.


.. _scripts-item-ishightier:

.. attribute:: IsHighTier
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-isportable:

.. attribute:: IsPortable
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-istelevision:

.. attribute:: IsTelevision
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-iswatersource:

.. attribute:: IsWaterSource
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-itemaftercleaning:

.. attribute:: ItemAfterCleaning
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-itemtype:

.. attribute:: ItemType
   :noindex:

:Type: string

:Required: True

:Allowed values:    ``base:alarmclock`` | ``base:alarmclockclothing`` | ``base:animal`` | ``base:clothing`` | ``base:container`` | ``base:drainable`` | ``base:food`` | ``base:key`` | ``base:literature`` | ``base:map`` | ``base:moveable`` | ``base:normal`` | ``base:radio`` | ``base:weapon`` | ``base:weaponpart``

Defines the class of the item which will impact which parameters the item can take and its properties as well as how it is used by the player. Clothing for instance will handle differently their texture and model in comparison to the other type of items, containers can hold items and weapons can be used by the player to attack and deal damage. You cannot use a custom class of item and only the ones accepted by the game.


.. _scripts-item-itemwhendry:

.. attribute:: ItemWhenDry
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

See parameter :ref:`Wet <scripts-item-wet>`.


.. _scripts-item-jamgunchance:

.. attribute:: JamGunChance
   :noindex:

:Type: float

:Default: ``1.0``

Base probability of a jam on each trigger pull. Final jam roml also scales with the sandbox jam multiplier, current gun condition (lower condition = higher jam chance), and low Aiming/Strength.

``JamGunChance = 1`` is already low. Setting it to ``0`` basically disables jams from this weapon. Higher values makes the gun unreliable and punishes neglecting the gun or unskilled use.


.. _scripts-item-keepondeplete:

.. attribute:: KeepOnDeplete
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-knockbackonnodeath:

.. attribute:: KnockBackOnNoDeath
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-knockdownmod:

.. attribute:: KnockdownMod
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-learnedrecipes:

.. attribute:: LearnedRecipes
   :noindex:

:Type: array (array of block, separator: ';')

List of `craftRecipe <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html>`_ this item will teach the player when read.


.. _scripts-item-lightdistance:

.. attribute:: LightDistance
   :noindex:

:Type: integer

See parameter :ref:`LightStrength <scripts-item-lightstrength>`.


.. _scripts-item-lightstrength:

.. attribute:: LightStrength
   :noindex:

:Type: float

`LightDistance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-lightdistance>`_ is used to determine the radius of the light emitted by the item. It is compared to the `Manhattan distance <https://en.wikipedia.org/wiki/Taxicab_geometry>`_ of the item to the square. The higher the value, the higher is the radius of the light.

`LightStrength <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-lightstrength>`_ will boost the light emitted.

.. code-block::

   new_light_level = current_light_level + 3 * LightStrength * (1 - clamp(dist / LightDistance, 0.0, 1.0))

The ``new_light_level`` is limited to a maximum of ``2.5``.


.. _scripts-item-lipids:

.. attribute:: Lipids
   :noindex:

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-lowlightbonus:

.. attribute:: LowLightBonus
   :noindex:

:Type: float

:Is useless: True

No description provided.


.. _scripts-item-lvlskilltrained:

.. attribute:: LvlSkillTrained
   :noindex:

:Type: integer

:Default: ``-1``

See parameter :ref:`SkillTrained <scripts-item-skilltrained>`.


.. _scripts-item-magazine_subject:

.. attribute:: magazine_subject
   :noindex:

:Type: array (array of string, separator: ';')

You can find a list of subjects in the `MagazineSubject <https://pz-wiki-modding.github.io/PZ-API-Docs/java/magazine_subject.html>`_.


.. _scripts-item-magazinetype:

.. attribute:: MagazineType
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

Used to set the magazine item the gun uses. If not provided, then the gun doesn't use a magazine item and loads rounds individually. `MaxAmmo <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxammo>`_ is used to set the capacity of either the magazine item or the gun.

See also:

- :ref:`AmmoType <scripts-item-ammotype>`
- :ref:`MaxAmmo <scripts-item-maxammo>`
- :ref:`AmmoBox <scripts-item-ammobox>`
- :ref:`WeaponReloadType <scripts-item-weaponreloadtype>`


.. _scripts-item-makeuptype:

.. attribute:: MakeUpType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-manuallyremovespentrounds:

.. attribute:: ManuallyRemoveSpentRounds
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-map:

.. attribute:: Map
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-maxammo:

.. attribute:: MaxAmmo
   :noindex:

:Type: integer

See parameter :ref:`MagazineType <scripts-item-magazinetype>`.

See also:

- :ref:`MagazineType <scripts-item-magazinetype>`
- :ref:`AmmoType <scripts-item-ammotype>`
- :ref:`AmmoBox <scripts-item-ammobox>`


.. _scripts-item-maxcapacity:

.. attribute:: MaxCapacity
   :noindex:

:Type: integer

:Default: ``-1``

No description provided.


.. _scripts-item-maxchannel:

.. attribute:: MaxChannel
   :noindex:

:Type: integer

:Default: ``108000``

No description provided.


.. _scripts-item-maxdamage:

.. attribute:: MaxDamage
   :noindex:

:Type: float

:Default: ``1.5``

Rolls the hit damage of the weapon between ``MinDamage`` and ``MaxDamage``.

`WeaponParts <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_ can modify the damage of the weapon with the `DamageModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-damagemodifier>`_ parameter. When equipped, a `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_ will increase the minimum and maximum damage of the weapon by the provided value. You are not limited to positive values, you can also add damage debuffs to the weapon by providing negative values.


.. _scripts-item-maxhitcount:

.. attribute:: MaxHitcount
   :noindex:

:Type: integer

:Default: ``1000``

`MaxHitcount <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxhitcount>`_ sets the maximum number of targets the weapon can hit with one attack. For ranged weapons, it will determine how many targets a single shot can hit. For melee weapons, a single swing can hit multiple targets if the relevant sandbox option allows it (Weapon Multi-Hit).

When `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-piercingbullets>`_ is ``true``\ , a shot continues past the first target and registers on collinear targets behind it. Each subsequent pierced target receives reduced damage (\ ``damage / PIERCING_BULLET_DAMAGE_REDUCTION``\ ). Targets must be within approximatively 1 degree of each other in angle to qualify.

Keep ``MaxHitcount`` to 1 for a standard rifle, and set it to 2 with `PiercingBullets <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-piercingbullets>`_ to have AP rounds behavior (M16A2 for example).


.. _scripts-item-maxitemsize:

.. attribute:: MaxItemSize
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-maxrange:

.. attribute:: MaxRange
   :noindex:

:Type: float

:Default: ``1.0``

`MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxrange>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `MaxRangeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxrangemodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_.

The `MaxRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxrange>`_ of a weapon is used to determine the maximum distance the weapon can shoot. Targets beyond ``effectiveMaxRange`` calculated with the formula below simply can't be reached, the parameter is a hard cutoff, not a penalty in damage or anything like that.

.. code-block::

   effectiveMaxRange = MaxRange + AimingPerkRangeModifier x (AimingLevel / 2.0)

All rifles from the base game have a ``AimingPerkRangeModifier`` of 0, so `aiming level <https://pzwiki.net/wiki/Aiming>`_ has no effect on the range of guns. Set it above 0 to give skilled players extra reach.


.. _scripts-item-maxrangemodifier:

.. attribute:: MaxRangeModifier
   :noindex:

:Type: float

See parameter :ref:`MaxRange <scripts-item-maxrange>`.


.. _scripts-item-maxsightrange:

.. attribute:: MaxSightRange
   :noindex:

:Type: float

`MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minsightrange>`_ and `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxsightrange>`_ define the optimal sight window, to be more specific, the distance band where hits and critical hits bonuses peak.

The `aiming skill <https://pzwiki.net/wiki/Aiming>`_ and `eagle eyed <https://pzwiki.net/wiki/Eagle_Eyed>`_ will impact these values:

.. code-block::

   effectiveMin = MinSightRange x (1 - AimingLevel / 30)
   effectiveMax = MaxSightRange x (1 + AimingLevel / 30) x (EagleEyed ? 1.2 : 1.0)

At aiming 10, the minimum shrinks by 33% and the max grows by 33%, which widens the window significantly. When the trait `Short Sighted <https://pzwiki.net/wiki/Short_Sighted>`_ is present and the character doesn't wear glasses, the ``effectiveMax`` equals ``effectiveMin``\ , making the entire bonus window disappear.

Inside the the ``effectiveMin`` and ``effectiveMax`` window, the bonus follows a `Gaussian <https://en.wikipedia.org/wiki/Bell-shaped_function>`_ with the bonus peaking at the midpoint. Aim-delay penalty is also reduced inside the window.

Below ``effectiveMin``\ , a small linear penalty is applied as the gun is not suited for point-blank. Above ``effectiveMax``\ , a growing quadratic penalty is applied, the bonus degrades rapidly past the edge.

A CQC gun should have a low `MaxSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-maxsightrange>`_ while a marksman riffle should have a high `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minsightrange>`_ with a wide window.


.. _scripts-item-mechanicsitem:

.. attribute:: MechanicsItem
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-mediacategory:

.. attribute:: MediaCategory
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-medical:

.. attribute:: Medical
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-metalvalue:

.. attribute:: MetalValue
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-micrange:

.. attribute:: MicRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-minangle:

.. attribute:: MinAngle
   :noindex:

:Type: float

:Default: ``1.0``

For `IsAimedFirearm <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-isaimedfirearm>`_ set to ``true``\ , the ballistics controller handles target detection and does not use `MinAngle <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minangle>`_ in the ranged hit-chance formula. These serve one narrow purpose: the ``isMeleeTargetTooCloseToShoot()`` check, detecting if a target is so close it should trigger a melee strike instead of a shot.

``MinAngle`` is a dot-product threshold (-1 to 1). Values near 1.0 mean the target must be almost directly in front to trigger the melee-swap check, while lower values widen the angle.

`AimingPerkMinAngleModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-aimingperkminanglemodifier>`_ is parsed and stored and impacts the minimum angle with the following formula:

.. code-block:: java

   effectiveMinAngle = MinAngle - AimingPerkMinAngleModifier * Aiming level


.. _scripts-item-minchannel:

.. attribute:: MinChannel
   :noindex:

:Type: integer

:Default: ``88000``

No description provided.


.. _scripts-item-mindamage:

.. attribute:: MinDamage
   :noindex:

:Type: float

See parameter :ref:`MaxDamage <scripts-item-maxdamage>`.


.. _scripts-item-minimumswingtime:

.. attribute:: MinimumSwingtime
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-minrange:

.. attribute:: MinRange
   :noindex:

:Type: float

Hard minimum attack distance. If the target is closer than ``MinRange``\ , the ballistics controller does not register the shot and the game may force a melee swap. This is a binary threshold, not a penalty band. Separate from `MinSightRange <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-minsightrange>`_.

Long rifles should be hard to use in tight spaces. ``0.2`` to ``0.35`` is a small gap but ``0.61`` is noticeably limiting indoors.


.. _scripts-item-minsightrange:

.. attribute:: MinSightRange
   :noindex:

:Type: float

See parameter :ref:`MaxSightRange <scripts-item-maxsightrange>`.


.. _scripts-item-minutestoburn:

.. attribute:: MinutesToBurn
   :noindex:

:Type: float

:Default: ``120.0``

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-minutestocook:

.. attribute:: MinutesToCook
   :noindex:

:Type: float

:Default: ``60.0``

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-modelweaponpart:

.. attribute:: ModelWeaponPart
   :noindex:

:Type: array (array of string, separator: ' ')

No description provided.


.. _scripts-item-mounton:

.. attribute:: MountOn
   :noindex:

:Type: array (array of string, separator: ';')

No description provided.


.. _scripts-item-multiplehitconditionaffected:

.. attribute:: MultipleHitConditionAffected
   :noindex:

:Type: boolean

:Default: ``True``

No description provided.


.. _scripts-item-muzzleflashmodelkey:

.. attribute:: MuzzleFlashModelKey
   :noindex:

:Type: block (block: :ref:`model <scripts-model>`)

No description provided.


.. _scripts-item-neckprotectionmodifier:

.. attribute:: NeckProtectionModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-needtobeclosedoncereload:

.. attribute:: needtobeclosedoncereload
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-noiseduration:

.. attribute:: NoiseDuration
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-noiserange:

.. attribute:: NoiseRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-notransmit:

.. attribute:: NoTransmit
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-npcsoundboost:

.. attribute:: NPCSoundBoost
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-numberofpages:

.. attribute:: NumberOfPages
   :noindex:

:Type: integer

:Default: ``-1``

See parameter :ref:`SkillTrained <scripts-item-skilltrained>`.


.. _scripts-item-numlevelstrained:

.. attribute:: NumLevelsTrained
   :noindex:

:Type: integer

:Default: ``1``

See parameter :ref:`SkillTrained <scripts-item-skilltrained>`.


.. _scripts-item-onattach:

.. attribute:: OnAttach
   :noindex:

:Type: callback

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-onbreak:

.. attribute:: OnBreak
   :noindex:

:Type: callback

Triggered when the item condition drops below 0.


.. _scripts-item-oncooked:

.. attribute:: OnCooked
   :noindex:

:Type: callback

No description provided.


.. _scripts-item-oncreate:

.. attribute:: OnCreate
   :noindex:

:Type: callback

Triggered when the item is instantiated.


.. _scripts-item-ondetach:

.. attribute:: OnDetach
   :noindex:

:Type: callback

See parameter :ref:`CanAttach <scripts-item-canattach>`.


.. _scripts-item-oneat:

.. attribute:: OnEat
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-onlyacceptcategory:

.. attribute:: OnlyAcceptCategory
   :noindex:

:Type: string

Makes sure only items with the specified `ItemCategory <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/itemcategory.html>`_ corresponding to the provided value of this parameter can be inserted into the container.


.. _scripts-item-openingrecipe:

.. attribute:: OpeningRecipe
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-opensound:

.. attribute:: OpenSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-originx:

.. attribute:: OriginX
   :noindex:

:Type: integer

Seems to indicate the coordinates this item is associate to, mostly used for keys.


.. _scripts-item-originy:

.. attribute:: OriginY
   :noindex:

:Type: integer

See parameter :ref:`OriginX <scripts-item-originx>`.


.. _scripts-item-originz:

.. attribute:: originZ
   :noindex:

:Type: integer

See parameter :ref:`OriginX <scripts-item-originx>`.


.. _scripts-item-otherhandrequire:

.. attribute:: OtherHandRequire
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-otherhanduse:

.. attribute:: OtherHandUse
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-packaged:

.. attribute:: Packaged
   :noindex:

:Type: boolean

Setting this to ``true`` will add readable content on the food item, which will display the `nutrional information <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-calories>`_ of the food item.


.. _scripts-item-padlock:

.. attribute:: Padlock
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-pagetowrite:

.. attribute:: PageToWrite
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-painreduction:

.. attribute:: painReduction
   :noindex:

:Type: integer

See parameter :ref:`fluReduction <scripts-item-flureduction>`.


.. _scripts-item-parttype:

.. attribute:: PartType
   :noindex:

:Type: string

Marks the `WeaponPart <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_ as a specific type of part. For proper tooltip of your weapon part, you need to either use one of the existing parts or use a custom part type but provide a translation entry inside `Tooltip.json <https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html#tooltip>`_ as ``Tooltip_weapon_`` followed by that part type value. For example, if you set ``PartType = customPart``\ , you need to provide a translation entry as ``Tooltip_weapon_customPart`` with the name of your part.

Here are the available part types in the base game:


* RecoilPad
* Clip
* Canon
* Scope
* Sling
* Stock

There are also some indirect part types. If the item has the `TorchCone <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-torchcone>`_ parameter, that part will be valid as a torch attachment. If it has the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtag>`_ ``base:optics``\ , it will be valid as an optics attachment.

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

.. attribute:: PhysicsObject
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

Provides another item (or itself) as a throwable object. When used, the item will be thrown instead of used as an actual in hands weapon.


.. _scripts-item-piercingbullets:

.. attribute:: PiercingBullets
   :noindex:

:Type: boolean

See parameter :ref:`MaxHitcount <scripts-item-maxhitcount>`.


.. _scripts-item-placedsprite:

.. attribute:: PlacedSprite
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-placemultiplesound:

.. attribute:: PlaceMultipleSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-placeonesound:

.. attribute:: PlaceOneSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-poison:

.. attribute:: Poison
   :noindex:

:Type: boolean

:Is useless: True

:Default: ``False``

See parameter :ref:`PoisonPower <scripts-item-poisonpower>`.


.. _scripts-item-poisondetectionlevel:

.. attribute:: PoisonDetectionLevel
   :noindex:

:Type: integer

See parameter :ref:`PoisonPower <scripts-item-poisonpower>`.


.. _scripts-item-poisonpower:

.. attribute:: PoisonPower
   :noindex:

:Type: integer

`PoisonPower <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-poisonpower>`_ defines the strength of the poison, where a positive value will make the food poisonous.

`PoisonDetectionLevel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-poisondetectionlevel>`_ doesn't seem to be useful, where a positive value will make it pass all the checks anyway, so increasing that value doesn't do anything.]

You can also mark an item to be shown as poisonous to the player by adding the `ItemTag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtag>`_ ``base:showpoison``.

The parameters `Poison <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-poison>`_ and `UseForPoison <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-useforpoison>`_ look unused.


.. _scripts-item-pourtype:

.. attribute:: PourType
   :noindex:

:Type: string

Sets an identifier for the pouring type. This will set the ``PourType`` `condition <https://pzwiki.net/wiki/Conditions>`_ of `AnimNode <https://pzwiki.net/wiki/AnimNode>`_ to the provided value when doing different actions:


* pouring, dumping, adding liquid etc
* fertilizing
* curing a plant

Specific values have different effects:


* ``Bucket`` will cause the item to play the sound ``Base.PourLiquidOnGroundMetal`` with the `tag <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-tags>`_ ``base:hasmetal`` when pouring liquid.
* ``Pot`` will also play ``Base.PourLiquidOnGroundMetal`` but without the need for the tag.
* Other values will play ``Base.PourLiquidOnGround`` when pouring liquid.


.. _scripts-item-primaryanimmask:

.. attribute:: primaryAnimMask
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-projectilecount:

.. attribute:: Projectilecount
   :noindex:

:Type: integer

:Default: ``1``

Only active when the weapon is ranged and has `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-rangefalloff>`_ set to ``true``. In that mode, the ballistics controller generates multiple spread projectiles. The field is never read when `RangeFalloff <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-rangefalloff>`_ is ``false``.

Inert for standard rifles. Required only for shotgun-style spread.


.. _scripts-item-projectilespread:

.. attribute:: ProjectileSpread
   :noindex:

:Type: float

Projectile spread seems to be mostly a visual effect and doesn't affect the actual hit chance of the weapon. The spread will be calculated following a formula close to the following:

.. code-block::

   spread = ProjectileSpread * 10 degrees +/- 2 degrees

With the ``spread`` value being the total cone angle of the projectiles.


.. _scripts-item-projectilespreadmodifier:

.. attribute:: ProjectileSpreadModifier
   :noindex:

:Type: float

No description provided.


.. _scripts-item-projectileweightcenter:

.. attribute:: ProjectileWeightCenter
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-protectfromrainwhenequipped:

.. attribute:: ProtectFromRainWhenEquipped
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-proteins:

.. attribute:: Proteins
   :noindex:

:Type: float

See parameter :ref:`Calories <scripts-item-calories>`.


.. _scripts-item-pushbackmod:

.. attribute:: PushBackMod
   :noindex:

:Type: float

:Default: ``1.0``

Scales the magnitude of the hit-reaction push applied to the target character. A higher value will increase the time the target is staggered. It will also impact the spread of blood.

Higher gives a more weighty, impactful feel.


.. _scripts-item-putinsound:

.. attribute:: PutInSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-rackaftershoot:

.. attribute:: RackAfterShoot
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-racksound:

.. attribute:: RackSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-rainfactor:

.. attribute:: RainFactor
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-ranged:

.. attribute:: Ranged
   :noindex:

:Type: boolean

See parameter :ref:`IsAimedFirearm <scripts-item-isaimedfirearm>`.


.. _scripts-item-rangefalloff:

.. attribute:: RangeFalloff
   :noindex:

:Type: boolean

No description provided.


.. _scripts-item-readtype:

.. attribute:: ReadType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-recoildelay:

.. attribute:: RecoilDelay
   :noindex:

:Type: Unknown

`RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelay>`_ is a stat which is directly applied to a `HandWeapon <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/HandWeapon.html>`_ while `AimingTimeModifier <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelaymodifier>`_ is applied to `weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_. Weapon attachments will add or subtract from `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelay>`_ directly.

Controls how long post-shot recovery takes before aim settling can begin. High values means the gun has a huge kick and forces a pause. Lower values is a flat, fast and snappy gun. `Strength <https://pzwiki.net/wiki/Strength>`_ and `aiming <https://pzwiki.net/wiki/Aiming>`_ will both reduce the recoil delay. Holding the gun one-handed will negatively impact the recoil handling. The following formula is used:

.. code-block:: java

   effectiveDelay = RecoilDelay
                 * (1 - AimingLevel / 40)
                 * (1 - (StrengthLevel * 2 - 10) / 40)
                 * (one-handed penalty: * 1.3 if primary hand only, secondary empty)

Aim countdown starts when the recoil delay counter is less than ``effectiveDelay * AimingLevel / 30``. Higher aiming also lets aim recovery start earlier in the recoil window.

See also:

- :ref:`RecoilDelayModifier <scripts-item-recoildelaymodifier>`
- :ref:`AimingTime <scripts-item-aimingtime>`
- :ref:`HitChance <scripts-item-hitchance>`


.. _scripts-item-recoildelaymodifier:

.. attribute:: RecoilDelayModifier
   :noindex:

:Type: Unknown

See parameter :ref:`RecoilDelay <scripts-item-recoildelay>`.

See also:

- :ref:`RecoilDelay <scripts-item-recoildelay>`
- :ref:`AimingTime <scripts-item-aimingtime>`
- :ref:`AimingTimeModifier <scripts-item-aimingtimemodifier>`
- :ref:`HitChance <scripts-item-hitchance>`


.. _scripts-item-reduceinfectionpower:

.. attribute:: ReduceInfectionPower
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-reloadtime:

.. attribute:: Reloadtime
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-reloadtimemodifier:

.. attribute:: ReloadTimeModifier
   :noindex:

:Type: integer

No description provided.


.. _scripts-item-remotecontroller:

.. attribute:: RemoteController
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-remoterange:

.. attribute:: RemoteRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-removenegativeeffectoncooked:

.. attribute:: RemoveNegativeEffectOnCooked
   :noindex:

:Type: boolean

See parameter :ref:`IsCookable <scripts-item-iscookable>`.


.. _scripts-item-removeonbroken:

.. attribute:: RemoveOnBroken
   :noindex:

:Type: boolean

:Default: ``True``

No description provided.


.. _scripts-item-removeunhappinesswhencooked:

.. attribute:: RemoveUnhappinessWhenCooked
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-replaceinprimaryhand:

.. attribute:: ReplaceInPrimaryHand
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-replaceinsecondhand:

.. attribute:: ReplaceInSecondHand
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-replaceoncooked:

.. attribute:: ReplaceOnCooked
   :noindex:

:Type: array (array of string, separator: ';')

A list of `items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html>`_ that will replace the cooked item by adding them to the player's inventory.


.. _scripts-item-replaceondeplete:

.. attribute:: ReplaceOnDeplete
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

When providing a `ReplaceOnDeplete <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-replaceondeplete>`_\ , the moment the item is depleted (e.g. a drainable item has no uses left anymore), it will be replaced by the item defined in this parameter. If this is empty, the item will be deleted without any replacement. This can notably be used to replace towels with a `wet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-wet>`_ towel.

`ReplaceOnExtinguish <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-replaceonextinguish>`_ on the other hand is used for `light sources items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-lightstrength>`_ to swap between the lit and unlit version of the item when it is fully drained.

`ReplaceOnRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-replaceonrotten>`_ is used for food items to swap to a different rotten version of items when they are fully rotten. This is actually not used to make an item rotten, which is natively handled by the game when providing `DaysFresh <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-daysfresh>`_ and `DaysTotallyRotten <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-daystotallyrotten>`_ but instead when the item isn't necessary bad to eat after the days rotten duration, like ice cream becoming melted for example.

`ReplaceOnUse <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-replaceonuse>`_ is used whenever an item is used, to replace it with another item. Used for containers containing food items to provide the container back after the food is eaten, or for dirty items getting cleaned.


.. _scripts-item-replaceonextinguish:

.. attribute:: ReplaceOnExtinguish
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-item-replaceonrotten:

.. attribute:: ReplaceOnRotten
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-item-replaceonuse:

.. attribute:: ReplaceOnUse
   :noindex:

:Type: block (block: :ref:`item <scripts-item>`, with :ref:`scripts-module`)

No description provided.


.. _scripts-item-replaceonuseon:

.. attribute:: ReplaceOnUseOn
   :noindex:

:Type: array (array of string, separator: '-')

Unclear what this does exactly.


.. _scripts-item-requireinhandorinventory:

.. attribute:: RequireInHandOrInventory
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-requiresequippedbothhands:

.. attribute:: RequiresEquippedBothHands
   :noindex:

:Type: boolean

No description provided.


.. _scripts-item-researchablerecipes:

.. attribute:: Researchablerecipes
   :noindex:

:Type: array (array of block, separator: ';')

No description provided.


.. _scripts-item-runanim:

.. attribute:: RunAnim
   :noindex:

:Type: string

:Default: ``Run``

No description provided.


.. _scripts-item-runspeedmodifier:

.. attribute:: RunSpeedModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-scaleworldicon:

.. attribute:: ScaleWorldIcon
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-scratchdefense:

.. attribute:: ScratchDefense
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-secondaryanimmask:

.. attribute:: secondaryAnimMask
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-sensorrange:

.. attribute:: SensorRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-sharpness:

.. attribute:: Sharpness
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-shellfallsound:

.. attribute:: ShellFallSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-shoutmultiplier:

.. attribute:: ShoutMultiplier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-shouttype:

.. attribute:: ShoutType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-skilltrained:

.. attribute:: SkillTrained
   :noindex:

:Type: string

:Default: (empty)

`SkillTrained <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-skilltrained>`_ is used to determine which skill the player will start training when reading this literature.

`LvlSkillTrained <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-lvlskilltrained>`_ indicates at what level this literature can be used to start training the skill. `NumLevelsTrained <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-numlevelstrained>`_ marks how many level can be trained thanks to this literature.


.. _scripts-item-smokerange:

.. attribute:: SmokeRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-soundgain:

.. attribute:: SoundGain
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-soundmap:

.. attribute:: SoundMap
   :noindex:

:Type: object (object: string->>block, kv: ' ', pairs: ';')

No description provided.


.. _scripts-item-soundparameter:

.. attribute:: SoundParameter
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-soundradius:

.. attribute:: SoundRadius
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-soundvolume:

.. attribute:: SoundVolume
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-spawnwith:

.. attribute:: SpawnWith
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-spice:

.. attribute:: Spice
   :noindex:

:Type: boolean

Marks this item as a spice, which can be used in the `evolved recipes <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html>`_ system.


.. _scripts-item-splatbloodonnodeath:

.. attribute:: SplatBloodOnNoDeath
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-splatnumber:

.. attribute:: SplatNumber
   :noindex:

:Type: integer

:Default: ``2``

No description provided.


.. _scripts-item-splatsize:

.. attribute:: SplatSize
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-staticmodel:

.. attribute:: StaticModel
   :noindex:

:Type: block (block: :ref:`model <scripts-model>`, with :ref:`scripts-module`)

`StaticModel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-staticmodel>`_ is used to define the model of the item being held in hands. On the other hand, `WorldStaticModel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-worldstaticmodel>`_ is used to define the model of the item being placed in the world. The two models can be different, for example a bucket can have a handle that is up when held in hands, but down when placed in the world.

See also:

- :ref:`WeaponSprite <scripts-item-weaponsprite>`
- :ref:`WorldStaticModel <scripts-item-worldstaticmodel>`
- :ref:`StaticModelsByIndex <scripts-item-staticmodelsbyindex>`
- :ref:`WorldStaticModelsByIndex <scripts-item-worldstaticmodelsbyindex>`


.. _scripts-item-staticmodelsbyindex:

.. attribute:: StaticModelsByIndex
   :noindex:

:Type: array (array of string, separator: ';')

`StaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-staticmodelsbyindex>`_ and `WorldStaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-worldstaticmodelsbyindex>`_ can be used to define multiple models for the same item definition, which is useful for variants of the same item (e.g. a weapon with different skins). You can use `IconsForTexture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-iconsfortexture>`_ alongside those to define different `icons <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-icon>`_ for each variant. Here's an example usage with three variants of the same item:

.. code-block:: cpp

   StaticModelsByIndex = AK47;AK47_Desert;AK47_Woodland,
   WorldStaticModelsByIndex = AK47;AK47_Desert;AK47_Woodland,
   IconsForTexture = AK47;AK47_Desert;AK47_Woodland,

See also:

- :ref:`StaticModel <scripts-item-staticmodel>`
- :ref:`WorldStaticModel <scripts-item-worldstaticmodel>`
- :ref:`IconsForTexture <scripts-item-iconsfortexture>`


.. _scripts-item-stomppower:

.. attribute:: StompPower
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-stoppower:

.. attribute:: StopPower
   :noindex:

:Type: float

:Default: ``5.0``

See parameter :ref:`CriticalChance <scripts-item-criticalchance>`.


.. _scripts-item-stresschange:

.. attribute:: StressChange
   :noindex:

:Type: float

When positive, the item being consumed will decrease the `player's stress <https://pzwiki.net/wiki/Stressed>`_\ , with ``100`` the maximum amount of stress of a player.

See also:

- :ref:`HungerChange <scripts-item-hungerchange>`
- :ref:`ThirstChange <scripts-item-thirstchange>`
- :ref:`UnhappyChange <scripts-item-unhappychange>`
- :ref:`BoredomChange <scripts-item-boredomchange>`


.. _scripts-item-subcategory:

.. attribute:: SubCategory
   :noindex:

:Type: string

:Default: (empty)

No description provided.


.. _scripts-item-survivalgear:

.. attribute:: SurvivalGear
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-suspensioncompression:

.. attribute:: suspensionCompression
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-suspensiondamping:

.. attribute:: suspensionDamping
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-swingamountbeforeimpact:

.. attribute:: SwingAmountBeforeImpact
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-swinganim:

.. attribute:: SwingAnim
   :noindex:

:Type: string

:Default: ``Rifle``

No description provided.


.. _scripts-item-swingsound:

.. attribute:: SwingSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

:Default: ``BaseballBatSwing``

No description provided.


.. _scripts-item-swingtime:

.. attribute:: Swingtime
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-tags:

.. attribute:: Tags
   :noindex:

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

.. attribute:: ThirstChange
   :noindex:

:Type: float

When positive, the item being consumed will decrease the `player's thirst <https://pzwiki.net/wiki/Thirsty>`_\ , with ``100`` the maximum amount of thirst of a player.

See also:

- :ref:`HungerChange <scripts-item-hungerchange>`
- :ref:`UnhappyChange <scripts-item-unhappychange>`
- :ref:`StressChange <scripts-item-stresschange>`
- :ref:`BoredomChange <scripts-item-boredomchange>`


.. _scripts-item-ticksperequipuse:

.. attribute:: ticksPerEquipUse
   :noindex:

:Type: integer

:Default: ``30``

No description provided.


.. _scripts-item-tohitmodifier:

.. attribute:: ToHitModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-tooltip:

.. attribute:: Tooltip
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-torchcone:

.. attribute:: TorchCone
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-torchdot:

.. attribute:: TorchDot
   :noindex:

:Type: float

:Default: ``0.96``

No description provided.


.. _scripts-item-transmitrange:

.. attribute:: TransmitRange
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-trap:

.. attribute:: Trap
   :noindex:

:Type: boolean

:Default: ``False``

No description provided.


.. _scripts-item-treedamage:

.. attribute:: TreeDamage
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-triggerexplosiontimer:

.. attribute:: triggerExplosionTimer
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-twohandweapon:

.. attribute:: TwoHandWeapon
   :noindex:

:Type: boolean

`TwoHandWeapon <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-twohandweapon>`_ marks the weapon as a two-handed weapon. `RecoilDelay <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-recoildelay>`_ gets a x1.3 penalty when the weapon is held one-handed instead of two handed. `RequiresEquippedBothHands <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-requiresequippedbothhands>`_ enforces the equip restriction in the context menu.


.. _scripts-item-twoway:

.. attribute:: TwoWay
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-type:

.. attribute:: Type
   :noindex:

:Type: Unknown

:Deprecated: {'replacedBy': 'ItemType', 'version': '42.13.0'}

Used to set the class of the item, which will influence parameters available.


.. _scripts-item-unequipsound:

.. attribute:: UnequipSound
   :noindex:

:Type: block (block: :ref:`sound <scripts-sound>`)

No description provided.


.. _scripts-item-unhappychange:

.. attribute:: UnhappyChange
   :noindex:

:Type: float

When positive, the item being consumed will decrease the `player's unhappiness <https://pzwiki.net/wiki/Unhappy>`_\ , with ``100`` the maximum amount of unhappiness of a player.

See also:

- :ref:`HungerChange <scripts-item-hungerchange>`
- :ref:`ThirstChange <scripts-item-thirstchange>`
- :ref:`StressChange <scripts-item-stresschange>`
- :ref:`BoredomChange <scripts-item-boredomchange>`


.. _scripts-item-usedelta:

.. attribute:: UseDelta
   :noindex:

:Type: float

:Default: ``0.03125``

Used to set the number of `uses <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/InventoryItem.html#getCurrentUses(>`_\ ) for the item where its durability has a value of ``1`` when full and ``0`` when empty. For example, a `base:drainable <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_ item with a ``UseDelta`` of ``0.03125`` (the default value) will have 32 uses ($1/0.03125$) before it is depleted.

When used for `Clothing items <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemtype>`_\ , the ``UseDelta`` is used to indicate the amount of durability lost for `oxygen tanks <https://pzwiki.net/wiki/Oxygen_Tank>`_ for items with the `ItemTag <https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html>`_ ``base:scba`` or `gas mask filters <https://pzwiki.net/wiki/Gas_Mask_Filter>`_ for items with the ItemTags ``base:gasmask``\ , ``base:respirator`` or ``base:improvisedgasmask``.

Some vanilla food items are using that parameter but it doesn't seem to be used for those anywhere. There's uses for it in the Java for Drainable, Weapon and Radio items, but it doesn't seem to be limited to those.


.. _scripts-item-useendurance:

.. attribute:: UseEndurance
   :noindex:

:Type: boolean

:Default: ``True``

If ``true``\ , the weapon will consume stamina on use based on the weapon `weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-weight>`_\ , `EnduranceMod <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-endurancemod>`_\ , fatigue modifiers and traits.

For guns, it is preferable to keep this as ``False``.


.. _scripts-item-useforpoison:

.. attribute:: UseForPoison
   :noindex:

:Type: integer

:Default: ``0``

No description provided.


.. _scripts-item-usesbattery:

.. attribute:: UsesBattery
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-useself:

.. attribute:: UseSelf
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-usewhileequipped:

.. attribute:: UseWhileEquipped
   :noindex:

:Type: boolean

:Default: ``True``

No description provided.


.. _scripts-item-usewhileunequipped:

.. attribute:: UseWhileUnequipped
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-useworlditem:

.. attribute:: UseWorldItem
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-vehiclepartmodel:

.. attribute:: VehiclePartModel
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-vehicletype:

.. attribute:: VehicleType
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-visionmodifier:

.. attribute:: VisionModifier
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-visualaid:

.. attribute:: VisualAid
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-waterresistance:

.. attribute:: WaterResistance
   :noindex:

:Type: float

`WaterResistance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-waterresistance>`_ is used to define how much the clothing item will resist water. The higher the value, the more resistant the clothing item will be to water. A value of ``1.0`` means the clothing item is fully waterproof, while a value of ``0.0`` means it is not waterproof at all.

This is the exact same process for `WindResistance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-windresistance>`_ but for wind instead of water.


.. _scripts-item-weaponhitarmoursound:

.. attribute:: WeaponHitArmourSound
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-weaponlength:

.. attribute:: WeaponLength
   :noindex:

:Type: float

:Default: ``0.4``

No description provided.


.. _scripts-item-weaponreloadtype:

.. attribute:: WeaponReloadType
   :noindex:

:Type: string

:Default: ``handgun``

Used to select the reload workflow of the gun. Notably affects rack-after-shot, insertion style and animations. The provided value references the `variable condition <https://pz-wiki-modding.github.io/PZ-API-Docs/xml/animnode.html#m-conditions>`_ ``WeaponReloadType`` in `AnimNodes <https://pzwiki.net/wiki/AnimNodes>`_. The game has the following values available by default:


* ``handgun``
* ``shotgun``
* ``boltactionnomag``
* ``boltaction``
* ``revolver``
* ``doublebarrelshotgun``
* ``doublebarrelshotgunsawn``

A custom ``WeaponReloadType`` can be used if the relevant animations and condition logic are properly set up in a custom `AnimNode <https://pzwiki.net/wiki/AnimNodes>`_.

See also:

- :ref:`AmmoType <scripts-item-ammotype>`
- :ref:`MagazineType <scripts-item-magazinetype>`


.. _scripts-item-weaponsprite:

.. attribute:: WeaponSprite
   :noindex:

:Type: block (block: :ref:`model <scripts-model>`, with :ref:`scripts-module`)

Defines the model of the weapon. If `StaticModel <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-staticmodel>`_ is not provided, the static model will be WeaponSprite. You can also define variants of a weapon model by using `StaticModelsByIndex <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-staticmodelsbyindex>`_.

See also:

- :ref:`StaticModel <scripts-item-staticmodel>`
- :ref:`WorldStaticModel <scripts-item-worldstaticmodel>`
- :ref:`StaticModelsByIndex <scripts-item-staticmodelsbyindex>`


.. _scripts-item-weaponspritesbyindex:

.. attribute:: WeaponSpritesByIndex
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-weaponweight:

.. attribute:: WeaponWeight
   :noindex:

:Type: float

:Default: ``1.0``

No description provided.


.. _scripts-item-weight:

.. attribute:: Weight
   :noindex:

:Type: float

:Default: ``1.0``

:Minimum: ``0.0``

`Weight <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-weight>`_ sets the weight of the item, or more commonly refered to as a `encumbrance <https://pzwiki.net/wiki/Heavy_load>`_. `Weapon parts <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/types/WeaponPart.html>`_ will impact the weight of the weapon when attached. Will also impact stamina drain when `UseEndurance <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-useendurance>`_ is ``true``. You need to make sure to add a `translation <https://pzwiki.net/wiki/Item_(scripts>`_\ #Display_name) to the item or the weight will not work in-game.

`WeightEmpty <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-weightempty>`_ is used to set the weight of a drainable when it is empty.

`WeightWet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-weightwet>`_ is used to set the weight of a clothing item when it is wet. The weight of the clothing item will be interpolated between ``Weight`` and ``WeightWet`` based on the `wetness <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/InventoryItem.html#getWetness(>`_\ ) of the clothing item.


.. _scripts-item-weightempty:

.. attribute:: WeightEmpty
   :noindex:

:Type: Unknown

See parameter :ref:`Weight <scripts-item-weight>`.


.. _scripts-item-weightmodifier:

.. attribute:: WeightModifier
   :noindex:

:Type: float

No description provided.


.. _scripts-item-weightreduction:

.. attribute:: WeightReduction
   :noindex:

:Type: integer

:Minimum: ``0``

:Maximum: ``100``

Percentage of the total contained weight in the bag that will be reduced. If the bag's content weights 10 and the reduction is 65, the bag content will only weight


.. _scripts-item-weightwet:

.. attribute:: WeightWet
   :noindex:

:Type: Unknown

See parameter :ref:`Weight <scripts-item-weight>`.


.. _scripts-item-wet:

.. attribute:: Wet
   :noindex:

:Type: boolean

`Wet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-wet>`_ marks the item as being wet. This is notably used for towels alongside the `WetCooldown <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-wetcooldown>`_ which indicates how long the item will stay wet before drying out.

When the item is dry, it is another item marked with the parameter `ItemWhenDry <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html#scripts-item-itemwhendry>`_.


.. _scripts-item-wetcooldown:

.. attribute:: WetCooldown
   :noindex:

:Type: float

:Default: ``-1.0``

See parameter :ref:`Wet <scripts-item-wet>`.


.. _scripts-item-wheelfriction:

.. attribute:: wheelFriction
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-windresistance:

.. attribute:: WindResistance
   :noindex:

:Type: Unknown

See parameter :ref:`WaterResistance <scripts-item-waterresistance>`.


.. _scripts-item-withdrainable:

.. attribute:: WithDrainable
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-withoutdrainable:

.. attribute:: WithoutDrainable
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-worldobjectsprite:

.. attribute:: WorldObjectSprite
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-worldrender:

.. attribute:: WorldRender
   :noindex:

:Type: Unknown

No description provided.


.. _scripts-item-worldstaticmodel:

.. attribute:: WorldStaticModel
   :noindex:

:Type: block (block: :ref:`model <scripts-model>`, with :ref:`scripts-module`)

See parameter :ref:`StaticModel <scripts-item-staticmodel>`.


.. _scripts-item-worldstaticmodelsbyindex:

.. attribute:: WorldStaticModelsByIndex
   :noindex:

:Type: array (array of string, separator: ';')

See parameter :ref:`StaticModelsByIndex <scripts-item-staticmodelsbyindex>`.


