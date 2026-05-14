#!/usr/bin/env python3
"""
Generate item tags documentation from item_tags.json and write to item_tags.rst
"""

import json
import os
from pathlib import Path


def generate_item_tags_docs():
    """Generate and write item tags documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    item_tags_json_path = repo_root / "pz-java-parser" / "out" / "item_tags.json"
    item_tags_rst_path = repo_root / "docs" / "source" / "java" / "item_tags.rst"
    
    # Read item tags from JSON
    if not item_tags_json_path.exists():
        print(f"Error: {item_tags_json_path} not found")
        return False
    
    try:
        with open(item_tags_json_path, 'r') as f:
            item_tags = json.load(f)
    except Exception as e:
        print(f"Error reading item_tags.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(item_tags)
    
    # Write to RST file
    try:
        with open(item_tags_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {item_tags_rst_path}")
        print(f"Total item tags: {len(item_tags)}")
        return True
    except Exception as e:
        print(f"Error writing to item_tags.rst: {e}")
        return False


def generate_rst_content(item_tags: list) -> str:
    """Generate RST formatted content for item tags."""
    
    content = """Item Tags
=========

Available item tags accessible from Lua code. Each tag can be accessed using ``ItemTag.FIELD_NAME`` and corresponds to a script name.

.. list-table:: Item Tags
   :widths: 20 30 50
   :header-rows: 1

   * - Lua Field
     - Script Name
     - Description
"""
    
    # Sort by field name
    sorted_tags = sorted(item_tags, key=lambda x: x['field'])
    
    for tag in sorted_tags:
        field = tag.get('field', '')
        name = tag.get('name', '')
        
        content += f"   * - ``ItemTag.{field}``\n"
        content += f"     - ``{name}``\n"
        content += f"     - \n"
    
    return content


if __name__ == "__main__":
    success = generate_item_tags_docs()
    exit(0 if success else 1)
