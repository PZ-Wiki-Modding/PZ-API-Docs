#!/usr/bin/env python3
"""
Generate item body locations documentation from item_body_locations.json and write to item_body_locations.rst
"""

import json
from pathlib import Path


def generate_item_body_location_docs():
    """Generate and write item body locations documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent.parent
    repo_root = script_dir.parent
    item_body_locations_json_path = repo_root / "external" / "pz-java-parser" / "out" / "item_body_locations.json"
    item_body_locations_rst_path = repo_root / "docs" / "source" / "java" / "item_body_locations.rst"
    
    # Read item body locations from JSON
    if not item_body_locations_json_path.exists():
        print(f"Error: {item_body_locations_json_path} not found")
        return False
    
    try:
        with open(item_body_locations_json_path, 'r') as f:
            item_body_locations = json.load(f)
    except Exception as e:
        print(f"Error reading item_body_locations.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(item_body_locations)
    
    # Write to RST file
    try:
        with open(item_body_locations_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {item_body_locations_rst_path}")
        print(f"Total item body locations: {len(item_body_locations)}")
        return True
    except Exception as e:
        print(f"Error writing to item_body_locations.rst: {e}")
        return False


def generate_rst_content(item_body_locations: list) -> str:
    """Generate RST formatted content for item body locations."""
    
    content = """ItemBodyLocation
================

Available `item body location <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/ItemBodyLocation.html>`_ enum values for specifying where items can be worn on the body.

.. list-table:: Item Body Locations
   :widths: 40 40
   :header-rows: 1

   * - Name
     - `Field <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/inventory/ItemBodyLocation.html#enum-constant-summary>`_
"""
    
    # Sort by name
    sorted_locations = sorted(item_body_locations, key=lambda x: x['name'])
    
    for location in sorted_locations:
        name = location.get('name', '')
        field = location.get('field', '')
        
        content += f"   * - {name}\n"
        content += f"     - ``ItemBodyLocation.{field}``\n"
    
    return content


if __name__ == "__main__":
    success = generate_item_body_location_docs()
    exit(0 if success else 1)
