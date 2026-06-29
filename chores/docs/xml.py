if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

from pathlib import Path

from documentation import Documentation, code_value_formatter
from project import PROJECT_ROOT, sanitize_description
from utility.metadata import metadata
from utility.rst import headers




TOC_DESCRIPTION = """
Reference documentation for XML file formats used in Project Zomboid. With this documentation, comes settings that you can use for `VSCode <https://pzwiki.net/wiki/Visual_Studio_Code>`_ alongside the `RedHat XML <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`_ extension to automatically verify your files. You can find `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/out/settings.json>`_ these settings.
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

def _link_to_type_formatter(object_type: str, object_data: dict, type_name: str, type_data: str) -> str:
    """Format the type name as a link to its documentation."""
    types = object_data.get("types", {})
    sanitized_to_list = type_data if isinstance(type_data, list) else [type_data]
    out = ""
    is_first = True
    for type_data in sanitized_to_list:
        if is_first is False:
            out += ", "
        is_first = False
        if type_data not in types:
            out += f"``{type_data}``"
        else:
            label = get_type_label(object_type, type_data)
            out += f":ref:`{type_data} <{label}>`"
    return out


## METADATA TYPES
# used for root element metadata
root_metadata = metadata({
    "Element": {"access_key": "name"}, # required in dataset
})

# used for type definitions
type_metadata = metadata({
    "Type": {"access_key": "type", "formatter": _link_to_type_formatter}, # required in dataset
    "Composition": {"access_key": "composition", "default": "all"}, # composition defaults to "all" in the schema generator
})

element_metadata = metadata({
    "Minimum occurence": {"access_key": "minOccurs", "default": "0"},
    "Maximum occurence": {"access_key": "maxOccurs", "default": "unbounded"},
    "Type": {"access_key": "type", "formatter": _link_to_type_formatter},
})

attribute_metadata = metadata({
    "Type": {"access_key": "type", "formatter": _link_to_type_formatter},
    "Use": {"access_key": "use", "default": "optional"},
})


## FORMATTERS
def _make_type_definition(object_type: str, object_data: dict, type_name: str, type_data: dict, title: bool = True) -> str:
    # init
    out = ""

    # make title if requested
    if title:
        label = get_type_label(object_type, type_name)
        out += headers.SUBSECTION.make(type_name, label)

    # make type metadata
    out += type_metadata.generate(object_type, type_data, {
        "type": type_name,
        "description": type_data.get("description", "No description provided."),
    }) + "\n\n"

    # make element list
    elements = type_data.get("elements", [])
    if elements:
        # title with label
        out += headers.SUBSUBSECTION.make("Elements")
        for element_data in elements:
            out += _make_element_definition(object_type, object_data, element_data)
    
    # make attributes list
    attributes = type_data.get("attributes", [])
    if attributes:
        # title with label
        out += headers.SUBSUBSECTION.make("Attributes")
        for attribute_data in attributes:
            out += _make_attribute_definition(object_type, object_data, attribute_data)

    # make restrictions list
    restrictions = type_data.get("restrictions", [])
    if restrictions:
        out += headers.SUBSUBSECTION.make("Restrictions")
        out += _make_restriction_definition(object_type, object_data, restrictions)
        
    return out

def _make_element_definition(object_type: str, object_data: dict, element_data: dict) -> str:
    element_name = element_data['name']
    out = headers.PARAGRAPH.make(element_name)

    # make element metadata
    out += element_metadata.generate(object_type, object_data, element_data['metadata']) + "\n\n"

    # description
    description = element_data.get("description", "No description provided.")
    sanitized_description = sanitize_description(description)
    out += sanitized_description.strip() + "\n\n"

    return out

def _make_attribute_definition(object_type: str, object_data: dict, attribute_data: dict) -> str:
    out = headers.PARAGRAPH.make(attribute_data['name'])

    # make attribute metadata
    out += attribute_metadata.generate(object_type, object_data, attribute_data['metadata']) + "\n\n"

    # description
    description = attribute_data.get("description", "No description provided.")
    sanitized_description = sanitize_description(description)
    out += sanitized_description.strip() + "\n\n"

    return out

def _make_restriction_definition(object_type: str, object_data: dict, restrictions: dict) -> str:
    out = ""

    # base type
    base = restrictions.get("base", None)
    if base is not None:
        out += metadata.format_metadata("Base", code_value_formatter(object_type, "base", base)) + "\n"

    # enumerations
    enumeration = restrictions.get("enumeration", [])
    if enumeration:
        out += metadata.format_metadata("Enumeration", "") + "\n"
        for i, enum in enumerate(enumeration):
            md = enum.get("metadata", {})
            out += "* " + code_value_formatter(object_type, "enumeration", md['value']) + "\n"
    
    return out

## MAIN SUBCLASS

class XMLDocumentation(Documentation):
    title = "XML"
    doc_type = "xml"
    data_path = PROJECT_ROOT / "pz-xml-data" / "out" / "data.json"
    toc_path = PROJECT_ROOT / "docs" / "source" / "xml.rst"
    toc_description = TOC_DESCRIPTION

    def pre_toc(self) -> None:
        for xml_type in self.data.keys():
            xml_file_path = Path(f"xml/{xml_type}")
            self.toc_elements.append(xml_file_path)

    # def generate_instructions(self) -> str | None:
    #     return "Test"

    def get_object_content(self, object_type: str, object_data: dict) -> str:
        """Get the content for a specific XML object."""
        
        # init
        content = "\n"

        # create file pattern doc for the XML file
        patterns = object_data.get("patterns", [])
        if patterns:
            content += headers.SUBSECTION.make(PATTERN_TITLE)
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
        content += headers.SUBSECTION.make(ROOT_TITLE, label)
        content += root_metadata.generate(object_type, object_data, root_element) + "\n\n"
        content += ROOT_DESCRIPTION.strip() + "\n\n"

        # make root type doc
        content += _make_type_definition(object_type,
                                         object_data,
                                         root_type,
                                         root_type_data,
                                         title=False) + "\n"
        
        # make doc for each type
        for type_name, type_data in types.items():
            # skip root_type since already documented
            if type_name == root_type:
                continue

            # make per type doc
            content += _make_type_definition(object_type, object_data, type_name, type_data) + "\n"

        return content