if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

from pathlib import Path

from documentation import Documentation, DocObject, code_value_formatter
from project import PROJECT_ROOT, sanitize_description
from utility.metadata import Metadata
from utility.rst import Headers



## DEFINITIONS

TOC_DESCRIPTION = """
Reference documentation for XML file formats used in Project Zomboid. With this documentation, comes settings that you can use for `VSCode <https://pzwiki.net/wiki/Visual_Studio_Code>`_ alongside the `RedHat XML <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`_ extension to automatically verify your files. You can find `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/out/settings.json>`_ these settings.
"""

TOC_INSTRUCTIONS = """
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
"""

TOC_CONTRIBUTING = """
You can contribute to this documentation by editing the `pz-xml-data <https://github.com/PZ-Wiki-Modding/pz-xml-data>`_ repository. You can read more about it `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/CONTRIBUTING.md>`_.
"""

PATTERN_TITLE = "File Patterns"
PATTERN_DESCRIPTION = """
The following file patterns are used to determine what the valid path for the XML file can be, relative to the `media <https://pzwiki.net/wiki/Mod_structure#Media_folder>`_ folder.
"""

ROOT_TITLE = "Root Details"
ROOT_DESCRIPTION = """
The root element is the top-level XML element that contains all other elements in the XML file.
"""

## UTILITY
def get_type_label(object_type: str, type_name: str) -> str:
    return f"{object_type}-{type_name}".lower()

# def get_parameter_label(object_type: str, type_name: str, parameter_name: str) -> str:
#     return get_type_label(object_type, type_name) + f"-{parameter_name}"

def _link_to_type_formatter(obj: "XMLDocObject", type_name: str, type_data: str|list) -> str:
    """Format the type name as a link to its documentation."""
    object_type = obj.name
    object_data = obj.data

    types = object_data.get("types", {})
    if not isinstance(type_data, list):
        type_data = [type_data]
    out = ""
    is_first = True
    for v in type_data:
        if is_first is False:
            out += ", "
        is_first = False
        if v not in types:
            out += f"``{v}``"
        else:
            label = get_type_label(object_type, v)
            out += f":ref:`{v} <{label}>`"
    return out


## METADATA TYPES
# used for root element metadata
root_metadata = Metadata({
    "Element": {"access_key": "name"}, # required in dataset
})

# used for type definitions
type_metadata: Metadata["XMLDocObject"] = Metadata({
    # "Type": {"access_key": "type", "formatter": _link_to_type_formatter}, # required in dataset
    "Composition": {"access_key": "composition", "default": "all"}, # composition defaults to "all" in the schema generator
})

element_metadata: Metadata["XMLDocObject"] = Metadata({
    "Minimum occurence": {"access_key": "minOccurs", "default": "0"},
    "Maximum occurence": {"access_key": "maxOccurs", "default": "unbounded"},
    "Type": {"access_key": "type", "formatter": _link_to_type_formatter},
})

attribute_metadata: Metadata["XMLDocObject"] = Metadata({
    "Type": {"access_key": "type", "formatter": _link_to_type_formatter},
    "Use": {"access_key": "use", "default": "optional"},
})


## FORMATTERS
def _make_type_definition(obj: "XMLDocObject", type_name: str, type_data: dict, title: bool = True) -> str:
    # init
    out = ""
    object_type = obj.name
    object_data = obj.data

    # make title if requested
    if title:
        label = get_type_label(object_type, type_name)
        out += Headers.SUBSECTION.make(type_name, label)

    # make type metadata
    out += type_metadata.generate(obj, {
        # "type": type_name,
        "description": type_data.get("description", "No description provided."),
    }) + "\n\n"

    # make element list
    elements = type_data.get("elements", [])
    if elements:
        # title with label
        out += Headers.SUBSUBSECTION.make("Elements")
        for element_data in elements:
            out += _make_element_definition(obj, element_data)
    
    # make attributes list
    attributes = type_data.get("attributes", [])
    if attributes:
        # title with label
        out += Headers.SUBSUBSECTION.make("Attributes")
        for attribute_data in attributes:
            out += _make_attribute_definition(obj, attribute_data)

    # make restrictions list
    restrictions = type_data.get("restrictions", [])
    if restrictions:
        out += Headers.SUBSUBSECTION.make("Restrictions")
        out += _make_restriction_definition(object_type, object_data, restrictions)
        
    return out

def _make_element_definition(obj: "XMLDocObject", element_data: dict) -> str:
    element_name = element_data['name']
    out = Headers.PARAGRAPH.make(element_name)

    # make element metadata
    out += element_metadata.generate(obj, element_data['metadata']) + "\n\n"

    # description
    description = element_data.get("description", "No description provided.")
    sanitized_description = sanitize_description(description)
    out += sanitized_description + "\n\n"

    return out

def _make_attribute_definition(obj: "XMLDocObject", attribute_data: dict) -> str:
    out = Headers.PARAGRAPH.make(attribute_data['name'])

    # make attribute metadata
    out += attribute_metadata.generate(obj, attribute_data['metadata']) + "\n\n"

    # description
    description = attribute_data.get("description", "No description provided.")
    sanitized_description = sanitize_description(description)
    out += sanitized_description + "\n\n"

    return out

def _make_restriction_definition(object_type: str, object_data: dict, restrictions: dict) -> str:
    out = ""

    # base type
    base = restrictions.get("base", None)
    if base is not None:
        out += Metadata.format_metadata("Base", code_value_formatter(object_type, "base", base)) + "\n"

    # enumerations
    enumeration = restrictions.get("enumeration", [])
    if enumeration:
        out += Metadata.format_metadata("Enumeration", "") + "\n"
        for i, enum in enumerate(enumeration):
            md = enum.get("metadata", {})
            out += "* " + code_value_formatter(object_type, "enumeration", md['value']) + "\n"
    
    return out

## MAIN SUBCLASS


class XMLDocObject(DocObject):
    def get_object_content(self) -> str:
        """Get the content for a specific XML object."""
        
        # init
        content = "\n"
        object_type = self.name
        object_data = self.data

        # create file pattern doc for the XML file
        patterns = object_data.get("patterns", [])
        if patterns:
            content += Headers.SUBSECTION.make(PATTERN_TITLE)
            content += PATTERN_DESCRIPTION.strip() + "\n\n"
            for pattern in patterns:
                content += f"- ``{pattern}``\n"
            content += "\n\n"

        # get root data
        root_element = object_data["root"]
        types = object_data.get("types", None)
        assert types is not None, "Types data is missing in the documentation data."
        root_type = root_element["type"]
        root_type_data = types.get(root_type, None)
        assert root_type_data is not None, f"Root type data for '{root_type}' is missing in the documentation data."

        # root element
        label = get_type_label(object_type, root_type)
        content += Headers.SUBSECTION.make(ROOT_TITLE, label)
        content += root_metadata.generate(self, root_element) + "\n\n"
        content += ROOT_DESCRIPTION.strip() + "\n\n"

        # make root type doc
        content += _make_type_definition(self,
                                         root_type,
                                         root_type_data,
                                         title=False) + "\n"
        
        # make doc for each type
        for type_name, type_data in types.items():
            # skip root_type since already documented
            if type_name == root_type:
                continue

            # make per type doc
            content += _make_type_definition(self, type_name, type_data) + "\n"

        return content
    




class XMLDocumentation(Documentation):
    title = "XML"
    doc_type = "xml"
    data_path = PROJECT_ROOT / "external" / "pz-xml-data" / "out" / "data.json"

    docObject = XMLDocObject

    toc_path = PROJECT_ROOT / "docs" / "source" / "xml.rst"
    toc_description = TOC_DESCRIPTION

    def generate_instructions(self) -> str | None:
        return TOC_INSTRUCTIONS

    def generate_contributing(self) -> str | None:
        return TOC_CONTRIBUTING




