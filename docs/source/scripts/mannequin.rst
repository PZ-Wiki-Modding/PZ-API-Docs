.. _scripts-mannequin:

mannequin
=========

.. attribute:: Soft Override

   Unknown

Used to define `mannequins <https://pzwiki.net/wiki/Mannequin>`_\ , which can be used in `mapping <https://pzwiki.net/wiki/Mapping>`_ to create mannequins in the world.

To get a list of available mannequins, see `this <https://pzwiki.net/wiki/Mannequin_(scripts>`_\ #Available_mannequins).


Hierarchy
---------

This block can be a child of the following blocks:

- :ref:`module <scripts-module>`



ID
--

This block can have an ID.

.. attribute:: Optional

   False

.. attribute:: Can have spaces

   False


Parameters
----------

.. _scripts-mannequin-animset:

animSet
^^^^^^^

.. attribute:: Type

   string

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


.. _scripts-mannequin-animstate:

animState
^^^^^^^^^

.. attribute:: Type

   string

See parameter :ref:`animSet <scripts-mannequin-animset>`.


.. _scripts-mannequin-female:

female
^^^^^^

.. attribute:: Type

   boolean

.. attribute:: Default

   ``True``

Set to ``true`` to mark the mannequin as female, which wil change its body type.


.. _scripts-mannequin-model:

model
^^^^^

.. attribute:: Type

   block (block: :ref:`model <scripts-model>`)

The `model <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html>`_ used by the mannequin. Some of the models available are:


* FemaleBody
* MaleBody
* Mannequin_Scarecrow
* Mannequin_Skeleton

By combining it with the `texture <https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html#mannequin-texture>`_ parameter, you can create a variety of mannequin appearances.


.. _scripts-mannequin-outfit:

outfit
^^^^^^

.. attribute:: Type

   string

.. attribute:: Can be empty

   True

The outfit used by the mannequin.


.. _scripts-mannequin-pose:

pose
^^^^

.. attribute:: Type

   string

See parameter :ref:`animSet <scripts-mannequin-animset>`.


.. _scripts-mannequin-texture:

texture
^^^^^^^

.. attribute:: Type

   string

Used to chose the texture that will be rendered on the mannequin model. The texture needs to be in the ``media/textures/body`` folder.


