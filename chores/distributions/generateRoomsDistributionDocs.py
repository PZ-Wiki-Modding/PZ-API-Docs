#!/usr/bin/env python3
"""
Generate room distributions documentation from distributions.json and write to rooms_distributions.rst
"""

import json
import os
from pathlib import Path


def generate_distributions_docs():
    """Generate and write distributions documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    distributions_json_path = repo_root / "pz-lua-parser" / "out" / "distributions.json"
    procedural_json_path = repo_root / "pz-lua-parser" / "out" / "procedural_distributions.json"
    distributions_rst_path = repo_root / "docs" / "source" / "distribution" / "rooms_distributions.rst"
    
    # Read distributions from JSON
    if not distributions_json_path.exists():
        print(f"Error: {distributions_json_path} not found")
        return False
    
    try:
        with open(distributions_json_path, 'r') as f:
            distributions = json.load(f)
    except Exception as e:
        print(f"Error reading distributions.json: {e}")
        return False
    
    # Read procedural distributions to validate references
    valid_procedural_dists = set()
    if procedural_json_path.exists():
        try:
            with open(procedural_json_path, 'r') as f:
                procedural_dists = json.load(f)
                valid_procedural_dists = set(procedural_dists.keys())
        except Exception as e:
            print(f"Warning: Could not read procedural_distributions.json: {e}")
    
    # Generate RST content
    rst_content = generate_rst_content(distributions, valid_procedural_dists)
    
    # Ensure output directory exists
    distributions_rst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to RST file
    try:
        with open(distributions_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {distributions_rst_path}")
        print(f"Total rooms: {len(distributions)}")
        return True
    except Exception as e:
        print(f"Error writing to rooms_distributions.rst: {e}")
        return False


def generate_rst_content(distributions: dict, valid_procedural_dists: set) -> str:
    """Generate RST formatted content for distributions."""
    
    content = """Room distributions
===================

Detailed procedural distribution entries for each room and its containers.

"""
    
    # content += f"Total rooms: {len(distributions)}\n\n"
    
    # Sort rooms alphabetically
    sorted_rooms = sorted(distributions.keys(), key=str.lower)
    
    for room_name in sorted_rooms:
        containers = distributions[room_name]
        
        # Add room header
        content += f"{room_name}\n"
        content += "-" * len(room_name) + "\n\n"
        
        # If room has no containers, add note
        if not containers:
            content += "*No distributions defined.*\n\n"
            continue
        
        # Sort containers alphabetically
        sorted_containers = sorted(containers.keys(), key=str.lower)
        
        for container_name in sorted_containers:
            proclist = containers[container_name]
            
            # Add container name (bold and underlined)
            content += f"**{container_name}**\n\n"
            # content += "=" * len(container_name) + "\n\n"
            
            # If container has no proclist entries, add note
            if not proclist:
                content += "*No entries.*\n\n"
                continue
            
            # Add table for proclist entries
            content += ".. list-table::\n"
            content += "   :header-rows: 1\n"
            content += "   :widths: auto\n\n"
            content += "   * - :ref:`item-picker-property-name`\n"
            content += "     - :ref:`item-picker-property-min`\n"
            content += "     - :ref:`item-picker-property-max`\n"
            content += "     - :ref:`item-picker-property-weightChance`\n"
            content += "     - :ref:`item-picker-property-forceForItems`\n"
            content += "     - :ref:`item-picker-property-forceForTiles`\n"
            content += "     - :ref:`item-picker-property-forceForRooms`\n"
            
            for entry in proclist:
                name = entry.get('name', '')
                min_val = entry.get('min', '-')
                max_val = entry.get('max', '-')
                weight_chance = entry.get('weightChance', '-')
                force_for_items = entry.get('forceForItems', [])
                force_for_tiles = entry.get('forceForTiles', [])
                force_for_rooms = entry.get('forceForRooms', [])
                
                # Create link to procedural distribution if it exists
                if name in valid_procedural_dists:
                    content += f"   * - :ref:`procedural-distribution-{name}`\n"
                else:
                    content += f"   * - {name}\n"
                content += f"     - {min_val}\n"
                content += f"     - {max_val}\n"
                content += f"     - {weight_chance}\n"
                
                # Format force for items list
                if force_for_items:
                    if isinstance(force_for_items, list):
                        content += "     - \n"
                        for item in force_for_items:
                            content += f"       - {item}\n"
                    else:
                        content += f"     - {force_for_items}\n"
                else:
                    content += "     - \n"
                
                # Format force for tiles list
                if force_for_tiles:
                    if isinstance(force_for_tiles, list):
                        content += "     - \n"
                        for tile in force_for_tiles:
                            content += f"       - {tile}\n"
                    else:
                        content += f"     - {force_for_tiles}\n"
                else:
                    content += "     - \n"
                
                # Format force for rooms list
                if force_for_rooms:
                    if isinstance(force_for_rooms, list):
                        content += "     - \n"
                        for room in force_for_rooms:
                            content += f"       - {room}\n"
                    else:
                        content += f"     - {force_for_rooms}\n"
                else:
                    content += "     - \n"
            
            content += "\n"
        
        content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_distributions_docs()
    exit(0 if success else 1)
