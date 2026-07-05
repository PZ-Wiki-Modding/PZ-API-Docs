if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

import json
from pathlib import Path

from documentation import Documentation, DocObject, DocObjectT, code_value_formatter
from project import PROJECT_ROOT, sanitize_description
from utility.metadata import Metadata
from utility.rst import headers


## DEFINITIONS

TOC_DESCRIPTION = """
This section provides detailed documentation for all available `script <https://pzwiki.net/wiki/Scripts>`_ blocks.
"""

ITEMTYPE_PARAMETERS_PATH = PROJECT_ROOT / "pz-scripts-data" / "out" / "itemParameters.json"
ITEMTYPE_PARAMETERS_DESCRIPTION = """
Specific parameters are only available for certain :ref:`item-itemtype`. The following lists for each ItemType will show what parameter is only saved for that specific ItemType script class (sub classes to `Item <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/Item.html>`_), which means using them for other classes doesn't make any sense as they will simply not be loaded in by the game.
"""


## UTILITY

def _load_itemtype_parameters() -> dict[str, list[str]]:
    with open(ITEMTYPE_PARAMETERS_PATH, "r") as f:
        data = json.load(f)
    return data
itemtype_parameters: dict[str, list[str]] = _load_itemtype_parameters()

def _sanitize_id(block_name: str) -> str:
    """Get the documentation page name for a block."""
    l = block_name.lower()
    return l.replace(' ', '-')

def _is_block(block_name: str, source_obj: "ScriptsDocObject") -> "ScriptsDocObject | None":
    """Check if a block is a valid script block."""
    for obj in source_obj.doc.objects:
        if obj.data["name"] == block_name:
            return obj
    return None

def _get_block_label(block_name: str) -> str:
    """Get the label for a block."""
    return f"scripts-{_sanitize_id(block_name)}"

def _get_parameter_label(block_name: str, parameter_name: str) -> str:
    """Get the label for a parameter."""
    return f"{_get_block_label(block_name)}-{_sanitize_id(parameter_name)}"

def _make_ref_label(text: str, label: str) -> str:
    """Make a reference label for a given label."""
    return f":ref:`{text} <{label}>`"

def _block_link_formatter(obj: "ScriptsDocObject", key: str, other_block_name: str) -> str:
    """Format the block name as a link to its documentation."""
    # this shouldn't be necessary, but just in case
    if not _is_block(other_block_name, obj):
        return code_value_formatter(obj.name, key, other_block_name)
    label = _get_block_label(other_block_name)
    return _make_ref_label(other_block_name, label)

def _list_formatter(obj: "ScriptsDocObject", key: str, value_list: list) -> str:
    """Format a list of values for metadata output."""
    if not isinstance(value_list, list):
        return code_value_formatter(obj.name, key, value_list)
    out = ""
    for i, v in enumerate(value_list):
        out += f"* {code_value_formatter(obj.name, key, v)}\n"
    return "\n" + out.strip()

def _block_link_list_formatter(obj: "ScriptsDocObject", key: str, value_list: list) -> str:
    for i, v in enumerate(value_list):
        value_list[i] = _block_link_formatter(obj, key, v)
    return _list_formatter(obj, key, value_list)

def _parameter_link_list_formatter(obj: "ScriptsDocObject", key: str, value_list: list) -> str:
    for i, v in enumerate(value_list):
        block_name = obj.data['name']
        label = _get_parameter_label(block_name, v)
        value_list[i] = _make_ref_label(v, label)
    return _list_formatter(obj, key, value_list)

def _variant_list_formatter(obj: "ScriptsDocObject", key: str, isVariant: bool) -> str:
    variants = obj.data.get('variants', [])
    if not variants:
        raise ValueError(f"Block '{obj.data['name']}' has no ID values to check for variants.")
    return _block_link_list_formatter(obj, key, variants)

def _type_formatter(obj: "ScriptsDocObject", key: str, type_data: dict) -> str:
    """Format type information from the parameter type object."""
    main_type = type_data.get('main', 'Any')
    type_str = main_type
    
    # Add block information
    block_info = type_data.get('block')
    if block_info:
        block_name = block_info.get('name', '')
        full_type = block_info.get('fullType', False)
        if block_name:
            type_str += f" (block: {_block_link_formatter(obj, '', block_name)}"
            if full_type:
                type_str += ", with :ref:`module`"
            type_str += ")"
    
    # Add array information
    array_info = type_data.get('array')
    if array_info:
        array_type = array_info.get('type', 'string')
        separator = array_info.get('separator', ',')
        type_str += f" (array of {array_type}, separator: '{separator}')"
    
    # Add object information
    object_info = type_data.get('object')
    if object_info:
        key_type = object_info.get('keyType', 'string')
        value_type = object_info.get('valueType', 'string')
        kv_sep = object_info.get('keyValueSeparator', ':')
        pairs_sep = object_info.get('pairsSeparator', ',')
        type_str += f" (object: {key_type}->>{value_type}, kv: '{kv_sep}', pairs: '{pairs_sep}')"
    
    return type_str

## METADATA

block_metadata = Metadata({
    "Deprecated": {"access_key": "deprecated", "default": None},
    "Soft Override": {"access_key": "softOverride", "default": "Unknown"},
    "Is Root": {"access_key": "isRoot", "default": None},
    "Is Variant of": {"access_key": "isVariant", "formatter": _block_link_formatter, "default": None},
    "No comma": {"access_key": "noComma", "default": None},
})

id_metadata = Metadata({
    "Optional": {"access_key": "optional", "default": "False"},
    "Can have spaces": {"access_key": "canHaveSpace", "default": "False"},
    "Allowed ID": {"access_key": "values", "formatter": _list_formatter, "default": None},
    "Forbidden ID": {"access_key": "forbidden", "formatter": _list_formatter, "default": None},
    "Variants": {"access_key": "asType", "formatter": _variant_list_formatter, "default": None},
    "No ID for parents": {"access_key": "parentsWithout", "formatter": _block_link_list_formatter, "default": None},
})

parameter_metadata = Metadata({
    "Type": {"access_key": "type", "formatter": _type_formatter, "default": "Unknown"},
    "Deprecated": {"access_key": "deprecated", "default": None},
    "Is useless": {"access_key": "isUseless", "default": None},
    "Required": {"access_key": "required", "default": None},
    "Allowed duplicates": {"access_key": "allowDuplicates", "default": None},
    "Can be empty": {"access_key": "canBeEmpty", "default": None},
    "Default": {"access_key": "default", "default": None, "formatter": code_value_formatter},
    "Minimum": {"access_key": "minimum", "default": None, "formatter": code_value_formatter},
    "Maximum": {"access_key": "maximum", "default": None, "formatter": code_value_formatter},
    "Allowed values": {"access_key": "values", "formatter": _list_formatter, "default": None},
    "Incompatible with": {"access_key": "incompatibleWith", "formatter": _parameter_link_list_formatter, "default": None},
})

## MAIN SUBCLASS

class ScriptsDocObject(DocObject):
    data: dict
    headerMetadata = block_metadata

    def get_object_path(self) -> Path:
        """Retrieve the output path for a specific object's documentation."""
        # default output path is the toc path directory with the toc path's stem
        object_out_dir = self.doc.toc_path.parent / self.doc.toc_path.stem
        isVariant = self.data.get("isVariant", None)
        if isVariant is not None:
            variant_out_path = None
            for object in self.doc.objects:
                if object.data["name"] == isVariant:
                    variant_out_path = object.get_object_path()
                    break
            if variant_out_path is None:
                raise ValueError(f"Variant parent block '{isVariant}' not found for block '{self.data['name']}'.")
            # remove .rst from variant_out_path
            object_out_dir = variant_out_path.parent / variant_out_path.stem
        return object_out_dir / f"{self.id}.rst"

    def get_object_content(self) -> str:
        """Get the content for a specific script block."""

        # init
        content = "\n"
        name = self.data['name']

        # make hierarchy section
        parent_blocks = self.data.get("parents", [])
        children_blocks = self.data.get("children", [])
        needsChildren = self.data.get("needsChildren", None)
        if parent_blocks or children_blocks:
            content += headers.SUBSECTION.make("Hierarchy")

            if parent_blocks:    
                content += "This block can be a child of the following blocks:\n\n"
                for parent in parent_blocks:
                    content += f"- {_block_link_formatter(self, 'parents', parent)}\n"
                content += "\n"
            if children_blocks:
                content += "This block can have the following child blocks:\n\n"
                for child in children_blocks:
                    content += f"- {_block_link_formatter(self, 'children', child)}\n"
                content += "\n"
            if needsChildren is not None:
                content += "This block requires these following children to be valid:\n\n"
                for child in needsChildren:
                    content += f"- {_block_link_formatter(self, 'needsChildren', child)}\n"
            content += "\n\n"

        # make ID section
        content += headers.SUBSECTION.make("ID")
        id_data = self.data.get("ID", None)
        if id_data is None:
            content += "This block should have no ID.\n\n\n"
        else:
            content += "This block can have an ID.\n\n"
            content += id_metadata.generate(self, id_data) + "\n\n\n"

        # generate specific ItemType list for item block
        if self.data['name'] == "item":
            content += headers.SUBSECTION.make("ItemType parameters")
            content += ITEMTYPE_PARAMETERS_DESCRIPTION.strip()
            content += "\n\n"

            for itemtype, parameters in itemtype_parameters.items():
                if parameters:
                    content += headers.SUBSUBSECTION.make(itemtype)
                    for parameter in parameters:
                        label = _get_parameter_label(name, parameter)
                        content += f"- {_make_ref_label(parameter, label)}\n"
                    content += "\n"
            content += "\n\n"

        # generate parameter section
        parameters = self.data.get("parameters", {})
        content += headers.SUBSECTION.make("Parameters")
        if not parameters:
            content += "This block has no parameters.\n\n"
        else:
            for parameter in parameters.values():
                # retrieve ref description source or use provided description
                ref_description = parameter.get("#desc", None)
                if ref_description is None:
                    description = parameter.get("description", "No description provided.")
                else:
                    block_name, parameter_name = ref_description.split("/")
                    ref_label = _get_parameter_label(block_name, parameter_name)
                    description = f"See parameter {_make_ref_label(parameter_name, ref_label)}."
                sanitized_description = sanitize_description(description)

                # make parameter subsection
                label = _get_parameter_label(name, parameter['name'])
                content += headers.SUBSUBSECTION.make(parameter['name'], label)
                content += parameter_metadata.generate(self, parameter) + "\n\n"
                content += sanitized_description + "\n\n"
                content += "\n"

        return content



class ScriptsDocumentation(Documentation):
    title = "ScriptsDocs"
    doc_type = "scripts"
    data_path = PROJECT_ROOT / "pz-scripts-data" / "out" / "scriptBlocks.json"

    docObject = ScriptsDocObject

    toc_path = PROJECT_ROOT / "docs" / "source" / "scripts.rst"
    toc_description = TOC_DESCRIPTION
    toc_depth = 4

    def pre_toc(self) -> None:
        default_path = Path("scripts")
        for obj in self.objects:
            # get the relative path of the script file to the toc path's parent
            script_file_path = obj.get_object_path().relative_to(self.toc_path.parent)

            # remove .rst part
            script_file_path = script_file_path.parent / script_file_path.stem

            # store
            self.toc_elements.append(script_file_path)
