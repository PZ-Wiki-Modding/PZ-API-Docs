#!/usr/bin/env python3
"""
Generate tile properties documentation from tile_properties.json and write to tile_properties.rst
"""

import json
from m2r import convert
from pathlib import Path


def generate_tile_properties_docs():
    """Generate and write tile properties documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    tile_properties_json_path = repo_root / "tile-properties-data" / "out" / "tile_properties.json"
    tile_properties_rst_path = repo_root / "docs" / "source" / "mapping" / "tile_properties.rst"
    
    # Read tile properties from JSON
    if not tile_properties_json_path.exists():
        print(f"Error: {tile_properties_json_path} not found")
        return False
    
    try:
        with open(tile_properties_json_path, 'r') as f:
            tile_properties = json.load(f)
    except Exception as e:
        print(f"Error reading tile_properties.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(tile_properties)
    
    # Ensure output directory exists
    tile_properties_rst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to RST file
    try:
        with open(tile_properties_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {tile_properties_rst_path}")
        print(f"Total properties: {len(tile_properties)}")
        return True
    except Exception as e:
        print(f"Error writing to tile_properties.rst: {e}")
        return False


def _format_metadata(prop_data: dict) -> str:
    """Format property metadata as RST field list."""
    rst = ""
    
    field_name = prop_data.get('field', '')
    prop_type = prop_data.get('type', {})
    default_value = prop_data.get('default', '')
    values = prop_data.get('values', [])
    
    # Add field name
    if field_name:
        rst += f":Field: ``TilePropertyKey.{field_name}``\n"
    
    # Add type information if present
    if prop_type:
        main_type = prop_type.get('main', '')
        if main_type:
            rst += f":Type: ``{main_type}``\n"
            
            # Add type constraints if present
            if 'min' in prop_type or 'max' in prop_type:
                range_parts = []
                if 'min' in prop_type:
                    range_parts.append(f"Min: {prop_type['min']}")
                if 'max' in prop_type:
                    range_parts.append(f"Max: {prop_type['max']}")
                if range_parts:
                    rst += f":Range: {', '.join(range_parts)}\n"
    
    # Add default value if present
    if default_value is not None and default_value != '':
        rst += f":Default: ``{default_value}``\n"
    
    # Add blank line after field list if there was any content
    if rst:
        rst += "\n"
    
    return rst


def generate_rst_content(tile_properties: dict) -> str:
    """Generate RST formatted content for tile properties."""
    
    content = """Tile Properties
===============

Reference documentation for tile properties that define the characteristics and behavior of tiles in the game world. The field is the identifier used in the Java and Lua code for this tile property, if you ever need to refer to it in `Lua <https://pzwiki.net/wiki/Lua_(API)>`_ code.

"""
    
    # Sort properties alphabetically by name
    sorted_properties = sorted(tile_properties.items(), key=lambda x: x[0].lower())
    
    for prop_name, prop_data in sorted_properties:
        description = prop_data.get('description', '')
        values = prop_data.get('values', [])
        prop_type = prop_data.get('type', {})

        desc_ref = prop_data.get('#desc', '')
        if desc_ref:
            description = f"See the description of the :ref:`{desc_ref} <tile-property-{desc_ref}>` property."
        
        # Add anchor label for reference
        anchor = f"tile-property-{prop_name}"
        content += f".. _{anchor}:\n\n"
        
        # Add property header (level 2)
        content += f"{prop_name}\n"
        content += "^" * len(prop_name) + "\n\n"
        
        # Add metadata as field list
        content += _format_metadata(prop_data)
        
        # Add description if present
        if description:
            content += f"{convert(description)}\n\n"
        
        # Add enum values from type if present
        if prop_type and 'values' in prop_type:
            type_values = prop_type['values']
            content += "Possible values:\n\n"
            for value in type_values:
                content += f"    - ``{value}``\n"
            content += "\n"
        
        # Add additional values if present
        if len(values) > 0:
            content += "Allowed values:\n\n"
            for value in values:
                content += f"    - ``{value}``\n"
            content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_tile_properties_docs()
    exit(0 if success else 1)
