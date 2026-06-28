.. _mannequin:

mannequin
=========

Used to define `mannequins <https://pzwiki.net/wiki/Mannequin>`_\ , which can be used in `mapping <https://pzwiki.net/wiki/Mapping>`_ to create mannequins in the world.

To get a list of available mannequins, see `this <https://pzwiki.net/wiki/Mannequin_(scripts>`_\ #Available_mannequins).


Hierarchy
---------

**Valid Parent Blocks:**

- :ref:`module`


ID Properties
-------------

This block should have an ID.


Parameters
----------

.. _mannequin-animset:

animSet
^^^^^^^

:Type: string

`animSet <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html#mannequin-animset>`_ defines the `AnimSet <https://pzwiki.net/wiki/AnimSet>`_ used by the mannequin, which you probably should keep as ``mannequin``. `animState <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html#mannequin-animstate>`_ will set the `AnimState <https://pzwiki.net/wiki/AnimState>`_ used in the provided animSet. The `pose <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html#mannequin-pose>`_ parameter will set the `AnimNode <https://pzwiki.net/wiki/AnimNode>`_ used by the mannequin, so the file inside the animState.

For example, take the vanilla mannequin AnimSets:

.. code-block::

   📁 media
     📁 AnimSets
       📁 mannequin
         📁 female
           📄 pose01.xml
           📄 pose02.xml
           📄 pose03.xml
         📁 male
           📄 pose01.xml
           📄 pose02.xml
           📄 pose03.xml
         📁 scarecrow
           📄 pose01.xml
         📁 skeleton
           📄 pose01.xml

If we want to use the AnimState ``female`` and AnimNode ``pose01.xml``\ , we need the following parameter combination:

.. code-block:: cpp

   animNode=mannequin,
   animState=female,
   pose=pose01,

.. _mannequin-animstate:

animState
^^^^^^^^^

:Type: string

See :ref:`mannequin-animset` for more details.

.. _mannequin-female:

female
^^^^^^

:Type: boolean
:Default: ``True``

Set to ``true`` to mark the mannequin as female, which wil change its body type.

.. _mannequin-model:

model
^^^^^

:Type: block (block: :ref:`model`)

The `model <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html>`_ used by the mannequin. Some of the models available are:


* FemaleBody
* MaleBody
* Mannequin_Scarecrow
* Mannequin_Skeleton

By combining it with the `texture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html#mannequin-texture>`_ parameter, you can create a variety of mannequin appearances.

.. _mannequin-outfit:

outfit
^^^^^^

:Type: string
:Attributes: Can be empty

The outfit used by the mannequin.

.. _mannequin-pose:

pose
^^^^

:Type: string

See :ref:`mannequin-animset` for more details.

.. _mannequin-texture:

texture
^^^^^^^

:Type: string

Used to chose the texture that will be rendered on the mannequin model. The texture needs to be in the ``media/textures/body`` folder.

