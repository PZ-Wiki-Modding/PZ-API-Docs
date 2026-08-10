if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

import json
from pathlib import Path
from typing import Any

from documentation import (
    Documentation, make_toc_tree,
    DocObject, DocObjectT, 
    code_value_formatter, list_formatter, code_list_formatter,
    TOC_TITLE
)
from project import PROJECT_ROOT, sanitize_description, DOC_LINK
from utility.metadata import Metadata, Rule
from utility.rst import Headers, Attribute, make_ref_label


## DEFINITIONS

TOC_DESCRIPTION = """
This section provides detailed documentation for all available `script <https://pzwiki.net/wiki/Scripts>`_ blocks.
"""

TOC_INSTRUCTIONS = f"""
Each script block has its own documentation page. These will each contain metadata about the block (soft overides, is variant etc), a description and a few sections:

* Explaining the block's hierarchy in relation to other blocks (parents, children, mandatory children)
* About the block's ID
* A list of all parameters

A variant block means it is a block that will have completely different behavior from the original block and other variants based on conditions. These conditions are usually the ID of the block.

Each parameter will contain the following information based on what is provided by the game and the currently documented data from `pz-scripts-data <https://github.com/PZ-Wiki-Modding/pz-scripts-data>`_:

* The type of the parameter, which can be a simple type (string, number, boolean), a block type (which will link to the block's documentation), an array type (with a separator), or an object type (with key and value types, and separators)
* If the parameter is deprecated or not
* If the parameter is required or not
* If the parameter can be empty or not
* The default value of the parameter, if any
* The minimum and maximum values of the parameter, if any
* A list of allowed values for the parameter, if any

The type will always be provided, and if not yet documented it will show as `Unknown`. The other ones may not be provided due to a lack of information or these simply don't exist for the parameter.
"""

TOC_CONTRIBUTING = """
You can contribute to this documentation by editing the `pz-scripts-data <https://github.com/PZ-Wiki-Modding/pz-scripts-data>`_ repository. You can read more about it `here <https://github.com/PZ-Wiki-Modding/pz-scripts-data/blob/main/CONTRIBUTING.md>`_.
"""

ROOT_FILES_DESCRIPTION = """
Root files are the base files that contain the script block and their parameters. Different script blocks go in different root files, which are listed below. They are handled similarly to other script blocks to them following similar behavior:

* children blocks
* parameters (in some cases)

They are your starting point for creating your own script blocks. The pattern values are used as validators for a root file path and are partial indicators of where the root file is located in the game or mod files but the description will usually contain better detail about its expected location.
"""

ITEMTYPE_PARAMETERS_PATH = PROJECT_ROOT / "external" / "pz-scripts-data" / "out" / "itemParameters.json"
ITEMTYPE_PARAMETERS_DESCRIPTION = f"""
Specific parameters are only available for certain `ItemType <{DOC_LINK}/scripts/item.html#ItemType>`_. The following lists for each ItemType will show what parameter is only saved for that specific ItemType script class (sub classes to `Item <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/Item.html>`_), which means using them for other classes doesn't make any sense as they will simply not be loaded in by the game.
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
        if obj.data.get("name") == block_name:
            return obj
    return None

def _get_block_label(block_name: str) -> str:
    """Get the label for a block."""
    return f"scripts-{_sanitize_id(block_name)}"

def _get_parameter_label(block_name: str, parameter_name: str) -> str:
    """Get the label for a parameter."""
    return f"{_get_block_label(block_name)}-{_sanitize_id(parameter_name)}"

def _block_link_formatter(obj: "ScriptsDocObject", key: str, other_block_name: str) -> str:
    """Format the block name as a link to its documentation."""
    # this shouldn't be necessary, but just in case
    if not _is_block(other_block_name, obj):
        return code_value_formatter(obj.name, key, other_block_name)
    label = _get_block_label(other_block_name)
    return make_ref_label(other_block_name, label)

def _block_link_list_formatter(obj: "ScriptsDocObject", key: str, value_list: list) -> str:
    for i, v in enumerate(value_list):
        value_list[i] = _block_link_formatter(obj, key, v)
    return list_formatter(obj, key, value_list)

def _parameter_link_list_formatter(obj: "ScriptsDocObject", key: str, value_list: list) -> str:
    for i, v in enumerate(value_list):
        block_name = obj.data['name']
        label = _get_parameter_label(block_name, v)
        value_list[i] = make_ref_label(v, label)
    return list_formatter(obj, key, value_list)

def _variant_list_formatter(obj: "ScriptsDocObject", key: str, variantOf: bool) -> str:
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
                type_str += ", with :ref:`scripts-module`"
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
    "Deprecated":         Rule(access_key="deprecated",       default=None                                      ),
    "Soft Override":      Rule(access_key="softOverride",     default="Unknown"                                 ),
    "Is Root":            Rule(access_key="isRoot",           default=None                                      ),
    "Is Variant of":      Rule(access_key="variantOf",        default=None,      formatter=_block_link_formatter),
    "No comma":           Rule(access_key="noComma",          default=None                                      ),
    "Root patterns":      Rule(access_key="pattern",          default=None,      formatter=code_list_formatter  ),
})

id_metadata = Metadata({
    "Optional":           Rule(access_key="optional",         default="False"                                     ),
    "Can have spaces":    Rule(access_key="canHaveSpace",     default="False"                                     ),
    "Allowed ID":         Rule(access_key="values",           default=None,      formatter=code_list_formatter       ),
    "Forbidden ID":       Rule(access_key="forbidden",        default=None,      formatter=code_list_formatter       ),
    "No ID for parents":  Rule(access_key="parentsWithout",   default=None,      formatter=_block_link_list_formatter),
})

parameter_metadata = Metadata({
    "Type":               Rule(access_key="type",             default="Unknown", formatter=_type_formatter               ),
    "Deprecated":         Rule(access_key="deprecated",       default=None                                               ),
    "Is useless":         Rule(access_key="isUseless",        default=None                                               ),
    "Required":           Rule(access_key="required",         default=None                                               ),
    "Allowed duplicates": Rule(access_key="allowDuplicates",  default=None                                               ),
    "Can be empty":       Rule(access_key="canBeEmpty",       default=None                                               ),
    "Default":            Rule(access_key="default",          default=None,      formatter=code_value_formatter          ),
    "Minimum":            Rule(access_key="minimum",          default=None,      formatter=code_value_formatter          ),
    "Maximum":            Rule(access_key="maximum",          default=None,      formatter=code_value_formatter          ),
    "Allowed values":     Rule(access_key="values",           default=None,      formatter=code_list_formatter           ),
    "Incompatible with":  Rule(access_key="incompatibleWith", default=None,      formatter=_parameter_link_list_formatter),
})

## MAIN SUBCLASS

class ScriptsDocObject(DocObject):
    doc: 'ScriptsDocumentation'
    data: dict
    headerMetadata = block_metadata

    # def sanitize_id(self, name: str) -> str:
    #     # isRoot = self.data.get("isRoot", False)
    #     id = super().sanitize_id(name)
    #     # if isRoot:
    #     #     return id.replace('root-', '')
    #     return id

    def get_object_path(self) -> Path:
        """Retrieve the output path for a specific object's documentation."""
        # default output path is the toc path directory with the toc path's stem
        object_out_dir = self.doc.toc_path.parent / self.doc.toc_path.stem
        id = self.id

        isRoot = self.data.get("isRoot", None)
        variantOf = self.data.get("variantOf", None)
        if isRoot is not None:
            object_out_dir = object_out_dir / 'root_files'
            id = id.replace('root-', '')
        elif variantOf is not None:
            variant_out_path = None
            for object in self.doc.objects:
                if object.data.get("name") == variantOf:
                    variant_out_path = object.get_object_path()
                    break
            if variant_out_path is None:
                raise ValueError(f"Variant parent block '{variantOf}' not found for block '{self.data['name']}'.")
            # remove .rst from variant_out_path
            object_out_dir = variant_out_path.parent / variant_out_path.stem
        return object_out_dir / f"{id}.rst"

    def get_object_content(self) -> str:
        """Get the content for a specific script block."""

        # init
        content = "\n"
        name = self.data['name']

        # make hierarchy section
        parent_blocks: list[str] = self.data.get("parents", []).copy()
        children_blocks: list[str] = self.data.get("children", []).copy()
        needsChildren: list[str] | None = self.data.get("needsChildren", None)
        if parent_blocks or children_blocks:
            content += Headers.SUBSECTION.make("Hierarchy")

            # valid parent blocks
            if parent_blocks:
                parent_blocks = sorted(parent_blocks, key=lambda x: x.lower())
                content += "This block can be a child of the following blocks:\n\n"
                for parent in parent_blocks:
                    content += f"- {_block_link_formatter(self, 'parents', parent)}\n"
                content += "\n"

            # mandatory children
            if needsChildren is not None:
                # if there are needsChildren, remove them from the children list
                # to avoid duplicates
                children_blocks = sorted([child for child in children_blocks if child not in needsChildren], key=lambda x: x.lower())

                content += "This block requires these following children to be valid:\n\n"
                for child in needsChildren:
                    content += f"- {_block_link_formatter(self, 'needsChildren', child)}\n"

            # children
            if children_blocks:
                content += "This block can have the following child blocks:\n\n"
                for child in children_blocks:
                    content += f"- {_block_link_formatter(self, 'children', child)}\n"
                content += "\n"

            content += "\n\n"

        # make ID section
        content += Headers.SUBSECTION.make("ID")
        id_data = self.data.get("ID", None)
        if id_data is None:
            content += "This block should have no ID.\n\n\n"
        else:
            content += "This block can have an ID.\n\n"
            content += id_metadata.generate(self, id_data) + "\n\n\n"

        # make variants section
        variants = self.data.get("variants", [])
        if variants:
            content += Headers.SUBSECTION.make("Variants")
            content += "This block has variants, that is blocks that will have different behavior from this block under certain conditions.\n\n"
            content += Documentation.make_toc_tree(self.doc, [], toc_depth=3, glob=f"{name}/*", title=None)
            content += "\n\n"

        # generate specific ItemType list for item block
        if self.data['name'] == "item":
            content += Headers.SUBSECTION.make("ItemType parameters")
            content += ITEMTYPE_PARAMETERS_DESCRIPTION.strip()
            content += "\n\n"

            for itemtype, parameters in self.doc.itemtype_parameters_data.items():
                if parameters:
                    content += Headers.SUBSUBSECTION.make(itemtype)
                    for parameter in parameters:
                        label = _get_parameter_label(name, parameter)
                        content += f"- {make_ref_label(parameter, label)}\n"
                    content += "\n"
            content += "\n\n"

        # generate parameter section
        parameters = self.data.get("parameters", {})
        content += Headers.SUBSECTION.make("Parameters")
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
                    description = f"See parameter {make_ref_label(parameter_name, ref_label)}."
                sanitized_description = sanitize_description(description)

                # make parameter subsection
                label = _get_parameter_label(name, parameter['name'])
                # content += Headers.SUBSUBSECTION.make(parameter['name'], label)
                content += Attribute.make(parameter['name'], label)
                content += parameter_metadata.generate(self, parameter) + "\n\n"
                content += sanitized_description + "\n\n"
                content += "\n"

        return content


class RootsDocPage(ScriptsDocObject):
    def get_object_path(self) -> Path:
        """Retrieve the output path for a specific object's documentation."""
        # default output path is the toc path directory with the toc path's stem
        object_out_dir = self.doc.toc_path.parent / self.doc.toc_path.stem
        return object_out_dir / f"root_files.rst"

    def get_label(self) -> str:
        """Retrieve the label for the root files documentation page."""
        return f"{self.doc.doc_type}-root-files-toc"

    def get_header(self) -> str:
        """Retrieve the header for the root files documentation page."""
        title = "Root Files"
        label = self.get_label()
        header = Headers.SECTION.make(title, label=label)
        header += ROOT_FILES_DESCRIPTION.strip()
        return header

    def get_object_content(self) -> str:
        """Get the content for the root files documentation page."""
        out = ""
        out += make_toc_tree([], toc_depth=4, title=None, glob="root_files/*")
        return out



class ScriptsDocumentation(Documentation[ScriptsDocObject]):
    title = "ScriptsDocs"
    doc_type = "scripts"
    data_path = PROJECT_ROOT / "external" / "pz-scripts-data" / "out" / "scriptsBlocks.json"
    roots_data_path = PROJECT_ROOT / "external" / "pz-scripts-data" / "out" / "roots.json"
    itemtype_data_path = PROJECT_ROOT / "external" / "pz-scripts-data" / "out" / "itemParameters.json"

    data: dict[str, dict[str, Any]] = {}
    roots_data: dict[str, dict[str, Any]] = {}
    itemtype_parameters_data: dict[str, list[str]] = itemtype_parameters

    docObject = ScriptsDocObject
    objects: list[ScriptsDocObject|RootsDocPage] = []

    toc_path = PROJECT_ROOT / "docs" / "source" / "scripts.rst"
    toc_description = TOC_DESCRIPTION
    toc_depth = 4

    def preload_data(self) -> None:
        """Preload the script blocks data from the JSON file."""
        super().preload_data() # load scripts blocks data

        # load other data files
        with open(self.roots_data_path, "r") as f:
            self.roots_data = json.load(f)
        with open(self.itemtype_data_path, "r") as f:
            self.itemtype_parameters_data = json.load(f)

    def prepare_data(self) -> None:
        """Prepare the script blocks data for documentation generation."""
        # add the root files documentation page first
        self.objects.append(RootsDocPage("root_files", {}, self, self.roots_data))

        # then add roots data
        for root_name, root_data in self.roots_data.items():
            root_obj = self.docObject(root_name, root_data, self, self.roots_data)
            self.objects.append(root_obj)

        # add scripts blocks data
        super().prepare_data()

    def pre_toc(self) -> None:
        """Prepare the table of contents (TOC) elements."""
        for obj in self.objects:
            if (isinstance(obj, RootsDocPage) 
                or obj.data.get("isRoot", False)
                or obj.data.get("variantOf", None) is not None):
                continue

            # get the relative path of the script file to the toc path's parent
            object_file_path = obj.get_object_path().relative_to(self.toc_path.parent)

            # remove .rst part
            object_file_path = object_file_path.parent / object_file_path.stem

            # store
            self.toc_elements.append(object_file_path)

    def make_toc_tree(self, 
                      toc_elements: list[Path], 
                      toc_depth: int | None = 2, 
                      title: str | None = TOC_TITLE, 
                      glob: str | None = None) -> str:
        """Create a TOC string for the script blocks and root files."""

        out = ""
        # out += super().make_toc_tree([], toc_depth, title="Root Files", glob="scripts/roots/*")
        out += super().make_toc_tree([Path("scripts/root_files")], toc_depth, title="Root Files")
        out += "\n\n"

        # we can't use glob "scripts/*" because it would duplicate "Root Files" entry
        # which we add manually in the toc above already so it goes above everything else
        out += super().make_toc_tree(toc_elements, toc_depth)

        return out

    def generate_instructions(self) -> str | None:
        return TOC_INSTRUCTIONS

    def generate_contributing(self) -> str | None:
        return TOC_CONTRIBUTING
