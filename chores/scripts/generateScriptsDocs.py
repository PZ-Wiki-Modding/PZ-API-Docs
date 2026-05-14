#!/usr/bin/env python3
"""
Auto-generates Sphinx documentation from YAML block definitions.
"""

import os, sys, yaml, shutil, json
from m2r import convert
from pathlib import Path
from typing import Dict, List, Any, Optional


def _get_block_link(block_name: str) -> str:
    """Get the documentation page name for a block."""
    l = block_name.lower()
    return l.replace(' ', '-')

def _get_param_label(block_name: str, param_name: str) -> str:
    """Get the documentation label for a parameter."""
    block_link = _get_block_link(block_name)
    param_link = param_name.replace(' ', '-').lower()
    return f"{block_link}-{param_link}"


def _dict_to_rst_csv(data: Dict[str, Any]) -> str:
    """Convert a dictionary to an RST CSV table."""
    rst = ".. csv-table::\n"
    rst += "   :header: " + ", ".join(f'"{key}"' for key in data.keys()) + "\n"
    rst += "   :widths: " + ", ".join("20" for _ in data) + "\n\n"
    
    # Add the single row of data
    rst += "   " + ", ".join(f'"{value}"' for value in data.values()) + "\n\n"
    
    return rst



children_map: dict[str, List['ScriptBlock']] = {}
variant_map: dict[str, List['ScriptBlock']] = {}
blocks_map: dict[str, 'ScriptBlock'] = {}
class ScriptBlock:
    """Represents a script block definition."""
    
    def __init__(self, name: str, data: Dict[str, Any], output_dir: Path):
        self.name = name
        self.data = data
        self.output_dir = output_dir

    def _format_description(self, text: Optional[str]) -> str:
        """Format the block description for RST."""
        if not text:
            return ""
        # Remove extra whitespace and format
        return convert(text).strip()
    
    def _format_type_info(self, param_type: dict) -> str:
        """Format type information from the parameter type object."""
        main_type = param_type.get('main', 'Any')
        type_str = main_type
        
        # Add block information
        block_info = param_type.get('block')
        if block_info:
            block_name = block_info.get('name', '')
            full_type = block_info.get('fullType', False)
            if block_name:
                type_str += f" (block: :ref:`{block_name}`"
                if full_type:
                    type_str += ", with :ref:`module`"
                type_str += ")"
        
        # Add array information
        array_info = param_type.get('array')
        if array_info:
            array_type = array_info.get('type', 'string')
            separator = array_info.get('separator', ',')
            type_str += f" (array of {array_type}, separator: '{separator}')"
        
        # Add object information
        object_info = param_type.get('object')
        if object_info:
            key_type = object_info.get('keyType', 'string')
            value_type = object_info.get('valueType', 'string')
            kv_sep = object_info.get('keyValueSeparator', ':')
            pairs_sep = object_info.get('pairsSeparator', ',')
            type_str += f" (object: {key_type}->>{value_type}, kv: '{kv_sep}', pairs: '{pairs_sep}')"
        
        return type_str
    
    def _format_parameter_metadata(self, param: Dict[str, Any]) -> str:
        """Format parameter metadata as a literal block (code box)."""
        lines = []
        
        # Type information
        param_type = param.get('type', {})
        type_str = self._format_type_info(param_type)
        
        required = param.get('required', False)
        type_line = f"Type: {type_str}"
        if required:
            type_line += " (required)"
        lines.append(type_line)
        
        # Minimum and maximum values
        minimum = param.get('minimum')
        maximum = param.get('maximum')
        if minimum is not None or maximum is not None:
            range_parts = []
            if minimum is not None:
                range_parts.append(f"Min: {minimum}")
            if maximum is not None:
                range_parts.append(f"Max: {maximum}")
            if range_parts:
                lines.append("Range: " + ", ".join(range_parts))
        
        # Default value
        default = param.get('default')
        if default is not None and default != "":
            if isinstance(default, list):
                default_str = ", ".join(str(v) for v in default) if default else ""
            else:
                default_str = str(default)
            if default_str:
                lines.append(f"Default: {default_str}")
        
        # Additional attributes
        if param.get('allowedDuplicate'):
            lines.append("Can be duplicated: ✓")
        if param.get('canBeEmpty'):
            lines.append("Can be empty: ✓")
        if param.get('isUseless'):
            lines.append("Useless: ✓")
        
        parents_only = param.get('parentsOnly', [])
        if parents_only:
            parents_str = ", ".join(parents_only)
            lines.append(f"Only for parents: {parents_str}")
        
        incompatible_with = param.get('incompatibleWith', [])
        if incompatible_with:
            incompatible_str = ", ".join(incompatible_with)
            lines.append(f"Incompatible with: {incompatible_str}")
        
        # Format as literal block with 4-space indentation
        if lines:
            return "\n".join(f"    {line}" for line in lines) + "\n\n"
        return ""
    
    def _generate_properties_table(self) -> str:
        properties = {
            "Parent blocks": ", ".join(self.data.get('parents', [])) if self.data.get('parents') else "None",
            "Required child blocks": ", ".join(self.data.get('needsChildren', [])) if self.data.get('needsChildren') else "None",
            "Possible child blocks": ", ".join(child.name for child in children_map.get(self.name, [])) if children_map.get(self.name) else "None",
            "Soft Override": "Yes" if self.data.get('softOverride', False) else "No",
        }
        return _dict_to_rst_csv(properties)
    
    def _generate_hierarchy_section(self) -> str:
        """Generate RST documentation for block hierarchy."""
        block_data = self.data
        
        rst = "\nHierarchy\n---------\n\n"
        block_name = block_data.get('name', '')
        
        should_have_parent = block_data.get('shouldHaveParent', False)
        if should_have_parent:
            parents = block_data.get('parents', [])
            if parents:
                rst += "**Valid Parent Blocks:**\n\n"
                for parent in parents:
                    parent_data = blocks_map.get(parent, None)
                    if parent_data is None or 'deprecated' in parent_data.data:
                        continue
                    rst += f"- :ref:`{_get_block_link(parent)}`\n"
                rst += "\n"
            else:
                rst += "This block should have a parent block.\n\n"
        else:
            rst += "This block does not require a parent block.\n\n"
        
        needs_children = block_data.get('needsChildren', [])
        if needs_children:
            rst += "**Required Child Blocks:**\n\n"
            for child in needs_children:
                rst += f"- :ref:`{_get_block_link(child)}`\n"
            rst += "\n"
        
        # Show all possible child blocks
        possible_children = children_map.get(block_name, [])
        if possible_children:
            rst += "**Possible Child Blocks:**\n\n"
            # Sort and display all possible children
            for child in sorted(possible_children, key=lambda x: x.name.lower()):
                rst += f"- :ref:`{_get_block_link(child.name)}`\n"
            rst += "\n"
        
        return rst
    
    def _generate_id_section(self) -> str:
        """Generate RST documentation for ID properties."""

        rst = "\nID Properties\n-------------\n\n"

        id_info: dict|None = self.data.get('ID', None)
        if id_info is None:
            rst += "This block should not have an ID.\n\n"
            return rst

        rst += "This block should have an ID.\n\n"
        
        as_type = id_info.get('asType', False)
        values = id_info.get('values', [])
        if as_type:
            rst += "Using a specific ID will make this block have different properties.\n\n"
            # for value in values:
            #     rst += f"- :ref:`{value} <{self._get_block_link(f"{block_name} {value}")}>`\n"
            # rst += "\n"
        
        if values:
            rst += "**Allowed ID Values:**\n\n"
            for value in values:
                if as_type:
                    rst += f"- :ref:`{value} <{_get_block_link(f"{self.name} {value}")}>`\n"
                else:
                    rst += f"- ``{value}``\n"
            rst += "\n"
        
        parents_without = id_info.get('parentsWithout', [])
        if parents_without:
            rst += "**Incompatible Parents:**\n\n"
            for parent in parents_without:
                rst += f"- {parent}\n"
            rst += "\n"
        
        return rst
    
    def _generate_parameters_section(self) -> str:
        """Generate RST documentation for parameters."""
        parameters = self.data.get('parameters', None)
        if not parameters:
            return ""
        
        rst = "\nParameters\n----------\n\n"

        # sort parameters by their lowcase name
        parameters = sorted(parameters.values(), key=lambda p: p.get('name', '').lower())
        
        for param in parameters:
            name = param.get('name', 'Unknown')
            description = self._format_description(param.get('description', 'No description'))
            
            # Add RST reference label for anchor linking
            label = _get_param_label(self.name, name)
            rst += f".. _{label}:\n\n"
            
            # Parameter name as definition with clickable permalink icon
            rst += f"{name}\n"
            rst += "^" * len(name) + "\n\n"

            ref = param.get('#ref', None)
            isRef = ref is not None
            if isRef:
                block_name, param_name = ref.split('/')
                rst += f" (see :ref:`{_get_param_label(block_name, param_name)}`)\n"

            
            # Type and metadata as literal block
            rst += self._format_parameter_metadata(param)
            
            # Description
            if "#desc" in param:
                desc_ref = param["#desc"]
                block_name, param_name = desc_ref.split('/')
                description = f"See :ref:`{_get_param_label(block_name, param_name)}` for more details."
                rst += f"{description}\n\n"
            elif description:
                indented_description = "\n".join(description.split("\n"))
                rst += f"{indented_description}\n\n"
            
            # Allowed values
            values = param.get('values', [])
            if values:
                rst += "Allowed values:\n\n"
                for value in values:
                    rst += f"    - ``{value}``\n"
                rst += "\n"
            
            # Deprecation information
            deprecated = param.get('deprecated', None)
            if deprecated:
                rst += ".. warning::\n\n"
                rst += "   **Deprecated**"
                
                version = deprecated.get('version')
                if version:
                    rst += f" (since version {version})"
                rst += "\n\n"
                
                replaced_by = deprecated.get('replacedBy')
                if replaced_by:
                    replaced_label = _get_param_label(self.name, replaced_by)
                    rst += f"   Use :ref:`{replaced_label}` instead.\n\n"
                
                deprecation_desc = deprecated.get('description')
                if deprecation_desc:
                    deprecation_desc = self._format_description(deprecation_desc)
                    indented_deprecation = "\n   ".join(deprecation_desc.split("\n"))
                    rst += f"   {indented_deprecation}\n\n"
        
        return rst

    def generate_doc(self) -> str:
        """Generate RST documentation for this block."""
        # Header
        rst = f".. _{_get_block_link(self.name)}:\n\n"
        rst += f"{self.name}\n"
        rst += "=" * len(self.name) + "\n\n"

        # Description
        description = self._format_description(self.data.get('description', 'No description available.'))
        rst += f"{description}\n\n"

        if self.name in variant_map:
            rst += ".. toctree::\n"
            rst += "   :maxdepth: 4\n"
            rst += "   :titlesonly:\n"
            rst += f"   :caption: Variants\n\n"
            for variant in variant_map[self.name]:
                rst += f"   {variant.get_block_index()}\n"

        # rst += self._generate_properties_table()

        # Soft override info
        if self.data.get('softOverride', False):
            rst += "This block can be soft overridden in scripts.\n\n"

        # Hierarchy section
        rst += self._generate_hierarchy_section()

        # ID Properties section
        rst += self._generate_id_section()

        # Parameters section
        rst += self._generate_parameters_section()

        return rst
    
    def get_block_index(self) -> str:
        safe_name = _get_block_link(self.name)
        filename = f'{safe_name}'

        isVariant = self.data.get('isVariant', False)
        if isVariant:
            return f"{isVariant}/{filename}"

        return f"scripts/{filename}"
    
    def get_path(self) -> Path:
        safe_name = _get_block_link(self.name)
        filename = f'{safe_name}.rst'

        isVariant = self.data.get('isVariant', False)
        if isVariant:
            return self.output_dir /  f"scripts/{isVariant}/{filename}"

        return self.output_dir /  f"scripts/{filename}"



class BlockDocumentationGenerator:
    """Generates RST documentation from YAML block definitions."""
    
    def __init__(self, blocks_file: Path, output_dir: Path):
        """
        Initialize the generator.
        
        Args:
            blocks_file: Path to the blocks JSON file
            output_dir: Path to output documentation directory
        """
        self.blocks_file = blocks_file
        self.output_dir = output_dir
        # blocks_map: Dict[str, ScriptBlock] = {}

    def load_blocks(self) -> None:
        """Load all block definitions from the JSON file."""
        try:
            with open(self.blocks_file, 'r') as f:
                blocks_data = json.load(f)
                blocks = sorted(blocks_data.values(), key=lambda b: b.get('name', '').lower())
                for block_data in blocks:
                    if block_data and 'name' in block_data and not 'deprecated' in block_data:
                        # if block_data['name'].startswith('_'):
                        #     continue
                        blocks_map[block_data['name']] = ScriptBlock(block_data['name'], block_data, self.output_dir)
        except Exception as e:
            print(f"Error: Failed to load blocks from {self.blocks_file}: {e}")
            sys.exit(1)

        # yaml_files = sorted(self.blocks_file.glob('*.yaml'))
        
        # for yaml_file in yaml_files:
        #     try:
        #         with open(yaml_file, 'r') as f:
        #             block_data: dict = yaml.safe_load(f)
        #             if block_data and 'name' in block_data and not 'deprecated' in block_data:
        #                 # if block_data['name'].startswith('_'):
        #                 #     continue
        #                 blocks_map[block_data['name']] = ScriptBlock(block_data['name'], block_data, self.output_dir)
        #     except Exception as e:
        #         print(f"Warning: Failed to load {yaml_file}: {e}")
        
        # Build children map after all blocks are loaded
        self._build_children_map()
    
    def _build_children_map(self) -> None:
        """Build a map of which blocks can be children of which parent blocks."""
        for block_name, block in blocks_map.items():
            parents: list[str] = block.data.get('parents', [])
            for parent in parents:
                if parent not in children_map:
                    children_map[parent] = []
                children_map[parent].append(block)
            isVariant = block.data.get('isVariant', False)
            if isVariant:
                if isVariant not in variant_map:
                    variant_map[isVariant] = []
                variant_map[isVariant].append(block)
    
    def generate_blocks_index(self) -> str:
        """Generate the blocks index RST file."""
        rst = "ScriptsDocs\n"
        rst += "=" * len("ScriptsDocs") + "\n\n"
        rst += "This section provides detailed documentation for all available `script <https://pzwiki.net/wiki/Scripts>`_ blocks.\n\n"
        rst += ".. toctree::\n"
        rst += "   :maxdepth: 4\n"
        rst += "   :titlesonly:\n"
        rst += "   :caption: Blocks\n\n"
        
        # Sort blocks by name
        for block_name, block in sorted(blocks_map.items(), key=lambda item: item[0].lower()):
            if block.data.get('isVariant', False):
                continue
            rst += f"   {block.get_block_index()}\n"
        
        return rst
    
    def write_documentation(self) -> list[Path]:
        """Write generated documentation to files."""
        files: list[Path] = []
        # Create blocks index
        index_rst = self.generate_blocks_index()
        index_path = os.path.join(self.output_dir, 'scripts.rst')
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        with open(index_path, 'w') as f:
            f.write(index_rst)
            files.append(Path(index_path))
        print(f"Created {index_path}")
        
        # Create individual block files
        for block_name, block in blocks_map.items():
            doc_content = block.generate_doc()
            block_path = block.get_path()
            os.makedirs(block_path.parent, exist_ok=True)
            with open(block_path, 'w') as f:
                f.write(doc_content)
            print(f"Created {block_path}")
            files.append(block_path)
        return files

    def run(self) -> list[Path]:
        """Execute the documentation generation."""
        print("Loading block definitions...")
        self.load_blocks()
        print(f"Loaded {len(blocks_map)} blocks")
        
        print("Generating documentation...")
        files = self.write_documentation()
        print("Documentation generation complete!")
        return files


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent.parent
    root_dir = script_dir.parent  # Go up from scripts to root
    blocks_file = root_dir / 'pz-scripts-data' / 'out' / 'scriptBlocks.json'
    output_dir = root_dir / 'docs' / 'source'

    # Remove the output_dir / 'blocks' folder if it exists
    blocks_output_dir = output_dir / 'scripts'
    if blocks_output_dir.exists() and blocks_output_dir.is_dir():
        shutil.rmtree(blocks_output_dir)

    os.makedirs(output_dir, exist_ok=True)
    
    # Verify paths exist
    if not blocks_file.exists():
        print(f"Error: Blocks file not found: {blocks_file}")
        sys.exit(1)
    
    if not output_dir.exists():
        print(f"Error: Output directory not found: {output_dir}")
        sys.exit(1)
    
    # Generate documentation
    generator = BlockDocumentationGenerator(blocks_file, output_dir)
    files = generator.run()

    # # git add generated files
    # try:
    #     import subprocess
    #     for file in files:
    #         subprocess.run(['git', 'add', str(file)], check=True)
    #     print("Added generated files to git staging area.")
    # except Exception as e:
    #     print(f"Warning: Failed to add files to git: {e}")


if __name__ == '__main__':
    main()
