#!/usr/bin/env python3
"""
Generate colors documentation from colors.json and write to colors.rst
"""

import json
from pathlib import Path


def generate_colors_docs():
    """Generate and write colors documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    colors_json_path = repo_root / "pz-java-parser" / "out" / "colors.json"
    colors_rst_path = repo_root / "docs" / "source" / "java" / "colors.rst"
    
    # Read colors from JSON
    if not colors_json_path.exists():
        print(f"Error: {colors_json_path} not found")
        return False
    
    try:
        with open(colors_json_path, 'r') as f:
            colors = json.load(f)
    except Exception as e:
        print(f"Error reading colors.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(colors)
    
    # Write to RST file
    try:
        with open(colors_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {colors_rst_path}")
        print(f"Total colors: {len(colors)}")
        return True
    except Exception as e:
        print(f"Error writing to colors.rst: {e}")
        return False


def get_scripts_usage(fct: str) -> str:
    """Determine if a color has scripts usage based on function type."""
    if fct in ("addColor", "AddGameColor"):
        return "True"
    elif fct == "addColorCB":
        return "False"
    else:
        return "Unknown"


def rgb_to_hex(r: float, g: float, b: float) -> str:
    """Convert RGB float values (0.0-1.0) to hex color code."""
    r_int = int(round(r * 255))
    g_int = int(round(g * 255))
    b_int = int(round(b * 255))
    return f"#{r_int:02x}{g_int:02x}{b_int:02x}"


def generate_rst_content(colors: list) -> str:
    """Generate RST formatted content for colors."""
    
    content = """Colors
======

Available colors accessible from Lua code or usable inside Scripts.

.. list-table:: Colors
   :header-rows: 1

   * - Name
     - `Lua Field <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/core/Colors.html#field-summary>`_
     - RGB Hex
     - Scripts Usage
"""
    
    # Sort by field name
    sorted_colors = sorted(colors, key=lambda x: x['field'])
    
    for color in sorted_colors:
        name = color.get('name', '')
        field = color.get('field', '')
        r = color.get('r', 0.0)
        g = color.get('g', 0.0)
        b = color.get('b', 0.0)
        fct = color.get('fct', '')
        
        hex_color = rgb_to_hex(r, g, b)
        scripts_usage = get_scripts_usage(fct)
        
        content += f"   * - {name}\n"
        content += f"     - ``Colors.{field}``\n"
        content += f"     - ``{hex_color}``\n"
        content += f"     - {scripts_usage}\n"
    
    return content


if __name__ == "__main__":
    success = generate_colors_docs()
    exit(0 if success else 1)
