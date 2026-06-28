#!/usr/bin/env python3
"""
Generate metabolics documentation from metabolics.json and write to metabolics.rst
"""

import json
from pathlib import Path


def generate_metabolics_docs():
    """Generate and write metabolics documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    metabolics_json_path = repo_root / "pz-java-parser" / "out" / "metabolics.json"
    metabolics_rst_path = repo_root / "docs" / "source" / "java" / "metabolics.rst"
    
    # Read metabolics data from JSON
    if not metabolics_json_path.exists():
        print(f"Error: {metabolics_json_path} not found")
        return False
    
    try:
        with open(metabolics_json_path, 'r') as f:
            metabolics_data = json.load(f)
    except Exception as e:
        print(f"Error reading metabolics.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(metabolics_data)
    
    # Write to RST file
    try:
        with open(metabolics_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {metabolics_rst_path}")
        print(f"Total metabolic levels: {len(metabolics_data)}")
        return True
    except Exception as e:
        print(f"Error writing to metabolics.rst: {e}")
        return False


def generate_rst_content(metabolics_data: list) -> str:
    """Generate RST formatted content for metabolics."""
    
    content = """Metabolics
==========

Available `metabolic levels <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/BodyDamage/Metabolics.html>`_ which are used for the :ref:`timedaction-metabolics` property.

.. list-table:: Metabolic Levels
   :widths: 30 20
   :header-rows: 1

   * - `Enum <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/characters/BodyDamage/Metabolics.html#enum-constant-summary>`_
     - Metabolic Rate
"""
    
    # Sort by value (metabolic rate)
    sorted_data = sorted(metabolics_data, key=lambda x: x['value'])
    
    for item in sorted_data:
        enum = item.get('enum', '')
        value = item.get('value', 0)
        
        content += f"   * - ``{enum}``\n"
        content += f"     - {value}\n"
    
    return content


if __name__ == "__main__":
    success = generate_metabolics_docs()
    exit(0 if success else 1)
