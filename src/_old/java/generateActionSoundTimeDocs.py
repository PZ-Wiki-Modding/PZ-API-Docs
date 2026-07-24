#!/usr/bin/env python3
"""
Generate action sound time documentation from action_sound_time.json and write to action_sound_time.rst
"""

import json
from pathlib import Path


def generate_action_sound_time_docs():
    """Generate and write action sound time documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent.parent
    repo_root = script_dir.parent
    action_sound_time_json_path = repo_root / "external" / "pz-java-parser" / "out" / "action_sound_time.json"
    action_sound_time_rst_path = repo_root / "docs" / "source" / "java" / "action_sound_time.rst"
    
    # Read action sound time data from JSON
    if not action_sound_time_json_path.exists():
        print(f"Error: {action_sound_time_json_path} not found")
        return False
    
    try:
        with open(action_sound_time_json_path, 'r') as f:
            action_sound_time_data = json.load(f)
    except Exception as e:
        print(f"Error reading action_sound_time.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(action_sound_time_data)
    
    # Write to RST file
    try:
        with open(action_sound_time_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {action_sound_time_rst_path}")
        print(f"Total action sound times: {len(action_sound_time_data)}")
        return True
    except Exception as e:
        print(f"Error writing to action_sound_time.rst: {e}")
        return False


def generate_rst_content(action_sound_time_data: list) -> str:
    """Generate RST formatted content for action sound time."""
    
    content = """ActionSoundTime
===============

Available `action sound time <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/ActionSoundTime.html>`_ events accessible for :ref:`scripts-timedaction-soundtime`.

.. list-table:: Action Sound Time Events
   :widths: 30 30
   :header-rows: 1

   * - `Enum <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/ActionSoundTime.html#enum-constant-summary>`_
     - Script Name
"""
    
    # Sort by enum name
    sorted_data = sorted(action_sound_time_data, key=lambda x: x['enum'])
    
    for item in sorted_data:
        enum = item.get('enum', '')
        name = item.get('name', '')
        
        content += f"   * - ``{enum}``\n"
        content += f"     - ``{name}``\n"
    
    return content


if __name__ == "__main__":
    success = generate_action_sound_time_docs()
    exit(0 if success else 1)
