#!/usr/bin/env python3
"""
Generate room documentation from rooms.json and write to rooms.rst
"""

import json
import os
from pathlib import Path


def generate_room_docs():
    """Generate and write room documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    rooms_json_path = repo_root / "pz-lua-parser" / "out" / "rooms.json"
    rooms_rst_path = repo_root / "docs" / "source" / "distribution" / "rooms.rst"
    
    # Read rooms from JSON
    if not rooms_json_path.exists():
        print(f"Error: {rooms_json_path} not found")
        return False
    
    try:
        with open(rooms_json_path, 'r') as f:
            rooms = json.load(f)
    except Exception as e:
        print(f"Error reading rooms.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(rooms)
    
    # Write to RST file
    try:
        with open(rooms_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {rooms_rst_path}")
        print(f"Total rooms: {len(rooms)}")
        return True
    except Exception as e:
        print(f"Error writing to rooms.rst: {e}")
        return False


def generate_rst_content(rooms: list) -> str:
    """Generate RST formatted content for rooms."""
    
    content = """Room names
==========

Available room types.

"""
    
    # content += f"Total rooms: {len(rooms)}\n\n"
    
    content += ".. list-table::\n"
    content += "   :header-rows: 1\n"
    content += "   :widths: auto\n\n"
    content += "   * - Room Name\n"
    
    rooms.sort(key=str.lower)

    for room in rooms:
        content += f"   * - ``{room}``\n"
    
    return content


if __name__ == "__main__":
    success = generate_room_docs()
    exit(0 if success else 1)
