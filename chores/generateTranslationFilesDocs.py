#!/usr/bin/env python3
"""
Generate translation files documentation from translationFiles.json and write to translation_files.rst
"""

import json
import os
from pathlib import Path


def generate_translation_files_docs():
    """Generate and write translation files documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    trans_files_json_path = repo_root / "pz-translation-data" / "data" / "translationFiles.json"
    trans_files_rst_path = repo_root / "docs" / "source" / "translations" / "translation_files.rst"
    
    # Read translation files from JSON
    if not trans_files_json_path.exists():
        print(f"Error: {trans_files_json_path} not found")
        return False
    
    try:
        with open(trans_files_json_path, 'r') as f:
            translation_files = json.load(f)
    except Exception as e:
        print(f"Error reading translationFiles.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(translation_files)
    
    # Write to RST file
    try:
        with open(trans_files_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {trans_files_rst_path}")
        print(f"Total translation files: {len(translation_files)}")
        return True
    except Exception as e:
        print(f"Error writing to translation_files.rst: {e}")
        return False


def generate_rst_content(translation_files: dict) -> str:
    """Generate RST formatted content for translation files."""
    
    content = """Translation Files
=================

Available translation file types, their descriptions and properties.

"""
    
    # Sort by file name
    sorted_files = sorted(translation_files.items(), key=lambda x: x[1].get('fileName', x[0]))
    
    for file_key, data in sorted_files:
        name = data.get('name', file_key)
        description = data.get('description', '')
        file_name = data.get('fileName', name)
        function = data.get('function', 'N/A')
        key_prefix = data.get('keyPrefix', '')
        
        # Create a reference label for this translation file
        content += f".. _{file_key.lower()}-translation:\n\n"
        content += f"{name}\n"
        content += "-" * (len(name) + 1) + "\n\n"
        
        if description:
            content += f"{description}\n\n"
        
        content += ".. list-table::\n"
        content += "   :widths: auto\n\n"
        content += f"   * - File Name\n"
        content += f"     - ``{file_name}``\n"
        content += f"   * - Function\n"
        content += f"     - ``{function}``\n"
        
        if key_prefix:
            content += f"   * - Key Prefix\n"
            content += f"     - ``{key_prefix}``\n"
        
        # Add pattern properties if available
        pattern_props = data.get('patternProperties', [])
        if pattern_props:
            content += f"   * - Pattern Properties\n"
            patterns = [f"``{prop.get('pattern', '')}``" for prop in pattern_props]
            content += f"     - {', '.join(patterns)}\n"
        
        # Add keys if available
        keys = data.get('keys', [])
        if keys:
            content += f"   * - Keys\n"
            key_names = [f"``{key.get('name', '')}``" for key in keys]
            content += f"     - {', '.join(key_names)}\n"
        
        content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_translation_files_docs()
    exit(0 if success else 1)
