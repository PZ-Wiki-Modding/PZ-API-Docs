#!/usr/bin/env python3
"""
Generate ItemPickerContainer properties documentation from ItemPickerContainer_properties.yaml
and write to item_picker_container_properties.rst
"""

import yaml
from pathlib import Path
from m2r import convert


def generate_properties_docs():
    """Generate and write properties documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    properties_yaml_path = repo_root / "pz-lua-parser" / "data" / "ItemPickerContainer_properties.yaml"
    properties_rst_path = repo_root / "docs" / "source" / "distribution" / "item_picker_container_properties.rst"
    
    # Read properties from YAML
    if not properties_yaml_path.exists():
        print(f"Error: {properties_yaml_path} not found")
        return False
    
    try:
        with open(properties_yaml_path, 'r') as f:
            properties = yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading ItemPickerContainer_properties.yaml: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(properties)
    
    # Ensure output directory exists
    properties_rst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to RST file
    try:
        with open(properties_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {properties_rst_path}")
        print(f"Total properties: {len(properties)}")
        return True
    except Exception as e:
        print(f"Error writing to item_picker_container_properties.rst: {e}")
        return False


def generate_rst_content(properties: list) -> str:
    """Generate RST formatted content for properties."""
    
    content = """ItemPickerContainer properties
==============================

Reference documentation for ItemPickerContainer procedural list entry properties. Those are used to define the procedural distributions which will be used for the containers of the rooms.

"""
    
    for prop in properties:
        name = prop.get('name', '')
        description = convert(prop.get('description', '')).strip()
        prop_type = prop.get('type', {})
        is_useless = prop.get('isUseless', False)
        
        # Add anchor label for reference
        anchor = f"item-picker-property-{name}"
        content += f".. _{anchor}:\n\n"
        
        # Add property header (level 2)
        content += f"{name}\n"
        content += "-" * len(name) + "\n\n"
        
        # Add description if present
        if description:
            content += f"{description}\n\n"
        
        # Add type information if present
        if prop_type:
            content += "**Type:**\n\n"
            if isinstance(prop_type, dict):
                main_type = prop_type.get('main', '')
                separator = prop_type.get('separator', '')
                
                if main_type:
                    content += f"- Main: ``{main_type}``\n"
                if separator:
                    content += f"- Separator: ``{separator}``\n"
                content += "\n"
            else:
                content += f"- ``{prop_type}``\n\n"
        
        # Add warning for useless properties
        if is_useless:
            content += ".. warning::\n"
            content += "\n"
            content += "   This property does nothing and has no effect.\n"
            content += "\n"
        
        content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_properties_docs()
    exit(0 if success else 1)
