#!/usr/bin/env python3
"""
Generate procedural distributions properties documentation from YAML
and write to procedural_distributions_properties.rst
"""

import yaml
from pathlib import Path
from m2r import convert


def generate_procedural_distributions_properties_docs():
    """Generate and write procedural distributions properties documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    properties_yaml_path = repo_root / "pz-lua-parser" / "data" / "procedural_distributions_properties.yaml"
    properties_rst_path = repo_root / "docs" / "source" / "distribution" / "procedural_distributions_properties.rst"
    
    # Read properties from YAML
    if not properties_yaml_path.exists():
        print(f"Error: {properties_yaml_path} not found")
        return False
    
    try:
        with open(properties_yaml_path, 'r') as f:
            properties = yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading procedural_distributions_properties.yaml: {e}")
        return False
    
    # Generate RST content
    rst_content = generate_rst_content(properties)
    
    # Ensure output directory exists
    properties_rst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to RST file
    try:
        with open(properties_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {properties_rst_path}")
        print(f"Total properties: {len(properties) if properties else 0}")
        return True
    except Exception as e:
        print(f"Error writing to procedural_distributions_properties.rst: {e}")
        return False


def generate_rst_content(properties: list) -> str:
    """Generate RST formatted content for procedural distributions properties."""
    
    content = """Procedural distributions properties
===================================

Reference for all available properties that can be set on procedural distributions.

"""
    
    if not properties:
        return content + "No properties found.\n"
    
    for prop in sorted(properties, key=lambda x: x.get('name', '')):
        if not isinstance(prop, dict) or 'name' not in prop:
            continue
        
        prop_name = prop['name']
        description = convert(prop.get('description', 'No description available.')).strip()
        
        # Add anchor label for reference
        anchor = f"procedural-distributions-property-{prop_name}"
        content += f".. _{anchor}:\n\n"
        
        # Add property header (level 2)
        content += f"{prop_name}\n"
        content += "-" * len(prop_name) + "\n\n"
        
        # Add description
        content += f"{description}\n\n"
    
    return content


if __name__ == "__main__":
    success = generate_procedural_distributions_properties_docs()
    exit(0 if success else 1)
