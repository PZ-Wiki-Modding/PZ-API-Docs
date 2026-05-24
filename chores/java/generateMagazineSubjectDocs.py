#!/usr/bin/env python3
"""
Generate magazine subject documentation from magazine_subject.json and write to magazine_subject.rst
"""

import json
from pathlib import Path


def generate_magazine_subject_docs():
    """Generate and write magazine subject documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    magazine_subject_json_path = repo_root / "pz-java-parser" / "out" / "magazine_subject.json"
    magazine_subject_rst_path = repo_root / "docs" / "source" / "java" / "magazine_subject.rst"
    
    # Read magazine subject data from JSON
    if not magazine_subject_json_path.exists():
        print(f"Error: {magazine_subject_json_path} not found")
        return False
    
    try:
        with open(magazine_subject_json_path, 'r') as f:
            magazine_subject_data = json.load(f)
    except Exception as e:
        print(f"Error reading magazine_subject.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(magazine_subject_data)
    
    # Write to RST file
    try:
        with open(magazine_subject_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {magazine_subject_rst_path}")
        print(f"Total magazine subjects: {len(magazine_subject_data)}")
        return True
    except Exception as e:
        print(f"Error writing to magazine_subject.rst: {e}")
        return False


def generate_rst_content(magazine_subject_data: list) -> str:
    """Generate RST formatted content for magazine subjects."""
    
    content = """Magazine Subject
================

Available `magazine subjects <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/MagazineSubject.html>`_ accessible used for the :ref:`item-magazine_subject` property.

.. list-table:: Magazine Subjects
   :widths: 25 25
   :header-rows: 1

   * - `Field <https://demiurgequantified.github.io/ProjectZomboidJavaDocs/zombie/scripting/objects/MagazineSubject.html#field-summary>`_
     - Script Name
"""
    
    # Sort by field name
    sorted_data = sorted(magazine_subject_data, key=lambda x: x['field'])
    
    for item in sorted_data:
        field = item.get('field', '')
        name = item.get('name', '')
        
        content += f"   * - ``MagazineSubject.{field}``\n"
        content += f"     - {name}\n"
    
    return content


if __name__ == "__main__":
    success = generate_magazine_subject_docs()
    exit(0 if success else 1)
