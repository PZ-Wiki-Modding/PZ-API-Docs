#!/usr/bin/env python3
"""
Generate language codes documentation from languageCodes.json and write to language_codes.rst
"""

import json
import os
from pathlib import Path


def generate_language_codes_docs():
    """Generate and write language codes documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    lang_codes_json_path = repo_root / "pz-translation-data" / "data" / "languageCodes.json"
    lang_codes_rst_path = repo_root / "docs" / "source" / "translations" / "language_codes.rst"
    
    # Read language codes from JSON
    if not lang_codes_json_path.exists():
        print(f"Error: {lang_codes_json_path} not found")
        return False
    
    try:
        with open(lang_codes_json_path, 'r') as f:
            language_codes = json.load(f)
    except Exception as e:
        print(f"Error reading languageCodes.json: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(language_codes)
    
    # Write to RST file
    try:
        with open(lang_codes_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {lang_codes_rst_path}")
        print(f"Total language codes: {len(language_codes)}")
        return True
    except Exception as e:
        print(f"Error writing to language_codes.rst: {e}")
        return False


def generate_rst_content(language_codes: dict) -> str:
    """Generate RST formatted content for language codes."""
    
    content = """Language Codes
==============

Available language codes, full language names and encoding.

"""
    
    # Sort by code name
    sorted_codes = sorted(language_codes.items(), key=lambda x: x[0])
    
    for code, data in sorted_codes:
        lang_name = data.get('languageName', code)
        encoding = data.get('encoding', 'UTF-8')
        
        # Create a reference label for this language code
        content += f".. _{code.lower()}-language:\n\n"
        content += f"{code} - {lang_name}\n"
        content += "-" * (len(f"{code} - {lang_name}") + 1) + "\n\n"
        
        content += ".. list-table::\n"
        content += "   :widths: auto\n\n"
        content += f"   * - Code\n"
        content += f"     - ``{code}``\n"
        content += f"   * - Language Name\n"
        content += f"     - {lang_name}\n"
        content += f"   * - Encoding\n"
        content += f"     - {encoding}\n\n"
    
    return content


if __name__ == "__main__":
    success = generate_language_codes_docs()
    exit(0 if success else 1)
