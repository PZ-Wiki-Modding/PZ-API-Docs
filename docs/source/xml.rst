XML
===

Reference documentation for XML file formats used in Project Zomboid. With this documentation, comes settings that you can use for `VSCode <https://pzwiki.net/wiki/Visual_Studio_Code>`_ alongside the `RedHat XML <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`_ extension to automatically verify your files. You can find `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/out/settings.json>`_ these settings.

Documentation Instructions
--------------------------

Each XML file has its own documentation page. These will each detail variouus data and elements this file can contain. A small description of the file is first provided to explain what it is used for, providing generic resources about the file and how it is formatted and written. Multiple sections are used:
* File patterns will explain what valid path the XML file can be found in.
* Details about the root element of the XML file, which is the top-level element that contains all other elements in the XML file. For example:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <rootElement>
        <childElement1>
            <grandchildElement1 />
        </childElement1>
        <childElement2 />
    </rootElement>


* A section for each type definition, which will detail the elements and attributes that can be used for that type. The root element is itself a type that can contain other various elements with their own types.

Contributing
------------

You can contribute to this documentation by editing the `pz-xml-data <https://github.com/PZ-Wiki-Modding/pz-xml-data>`_ repository. You can read more about it `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/CONTRIBUTING.md>`_.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   xml/animnode
   xml/clothing
   xml/clothingdecals
   xml/clothingitem
   xml/fileguidtable
