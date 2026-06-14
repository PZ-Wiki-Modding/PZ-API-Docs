#!/usr/bin/env python3
"""
Generate XML documentation from pz-xml-data/out/data.json and write to RST files.
Creates individual RST files for each XML type in docs/source/xml/<type>.rst
and generates a main xml.rst file with toctree.
"""

import json
from m2r import convert
from pathlib import Path
from typing import Dict, List, Any, Optional


def generate_xml_docs() -> bool:
    """Generate and write XML documentation to RST files."""
    
    # Define paths
    script_dir = Path(__file__).parent.parent
    repo_root = script_dir.parent
    data_json_path = repo_root / "pz-xml-data" / "out" / "data.json"
    xml_docs_dir = repo_root / "docs" / "source" / "xml"
    xml_rst_path = repo_root / "docs" / "source" / "xml.rst"
    
    # Read data from JSON
    if not data_json_path.exists():
        print(f"Error: {data_json_path} not found")
        return False
    
    try:
        with open(data_json_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading data.json: {e}")
        return False
    
    # Ensure output directory exists
    xml_docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate individual RST files for each XML type
    xml_types = []
    for xml_type, type_data in sorted(data.items()):
        rst_content = generate_type_rst_content(xml_type, type_data)
        type_file = xml_docs_dir / f"{xml_type}.rst"
        
        try:
            with open(type_file, 'w') as f:
                f.write(rst_content)
            print(f"Successfully generated {type_file}")
            xml_types.append(xml_type)
        except Exception as e:
            print(f"Error writing to {type_file}: {e}")
            return False
    
    # Generate main xml.rst file with toctree
    main_rst_content = generate_main_rst_content(xml_types)
    
    try:
        with open(xml_rst_path, 'w') as f:
            f.write(main_rst_content)
        print(f"Successfully generated {xml_rst_path}")
        print(f"Total XML types: {len(xml_types)}")
        return True
    except Exception as e:
        print(f"Error writing to xml.rst: {e}")
        return False


def generate_main_rst_content(xml_types: List[str]) -> str:
    """Generate RST content for the main XML documentation file."""
    
    content = """XML
===

Reference documentation for XML file formats used in Project Zomboid.

.. toctree::
   :maxdepth: 2
   :titlesonly:

"""
    
    for xml_type in xml_types:
        content += f"   xml/{xml_type}\n"
    
    return content


def generate_type_rst_content(xml_type: str, type_data: Dict[str, Any]) -> str:
    """Generate RST content for a specific XML type."""

    description = type_data.get('description', 'No description available.')
    
    content = f"""{xml_type}
{'=' * len(xml_type)}

"""
    
    # Convert description from HTML/markdown to RST
    if description:
        converted_desc = convert(description).strip()
        content += f"{converted_desc}\n\n"
    
    # Add patterns section if available
    patterns = type_data.get('patterns', [])
    if patterns:
        content += "File Patterns\n"
        content += "-" * len("File Patterns") + "\n\n"
        for pattern in patterns:
            content += f"- ``{pattern}``\n"
        content += "\n"
    
    # Add root element section with root type documentation
    root = type_data.get('root', {})
    root_type_name = None
    if root:
        root_name = root.get('name', '')
        root_type = root.get('type', '')
        root_type_name = root_type
        
        content += "Root Element\n"
        content += "-" * len("Root Element") + "\n\n"
        content += f":Element: ``<{root_name}>``\n"
        
        if root_type:
            content += f":Type: ``{root_type}``\n"
        
        content += "\n"
    
    # Add structure overview section
    types = type_data.get('types', {})
    if types:
        content += "Structure\n"
        content += "-" * len("Structure") + "\n\n"
        
        # Find the root type and describe its structure
        if root and root.get('type'):
            root_type_name = root.get('type')
            root_type_info = types.get(root_type_name, {})
            
            if root_type_info:
                type_class = root_type_info.get('type', '')
                if type_class == 'complex':
                    composition = root_type_info.get('composition', '')
                    elements = root_type_info.get('elements', [])
                    attributes = root_type_info.get('attributes', [])
                    
                    if composition:
                        comp_text = "choice" if composition == "choice" else "sequence"
                        content += f"The root element uses a **{comp_text}** composition, meaning it can contain any combination of the following elements:\n\n"
                    else:
                        content += "The root element can contain the following elements:\n\n"
                    
                    if elements:
                        for element in elements:
                            info = element.get('info', {})
                            element_name = info.get('name', '')
                            element_type = info.get('type', '')
                            min_occurs = info.get('minOccurs', 0)
                            max_occurs = info.get('maxOccurs', 1)
                            
                            # Determine if optional or required
                            if min_occurs == 0:
                                req_text = "(optional)"
                            else:
                                req_text = "(required)"
                            
                            # Handle type list
                            if isinstance(element_type, list):
                                formatted_types = []
                                for t in element_type:
                                    formatted_types.append(_format_type_reference(t, xml_type))
                                element_type_str = " | ".join(formatted_types)
                            else:
                                element_type_str = _format_type_reference(element_type, xml_type)
                            
                            # Create link to detailed documentation for this element
                            # Use root_type_name to get the correct label
                            element_label = f"{xml_type}.{root_type_name}.{element_name}"
                            content += f"- :ref:`<{element_name}> <{element_label}>` {req_text}: {element_type_str}\n"
                        content += "\n"
                    
                    if attributes:
                        content += "**Attributes:**\n\n"
                        for attribute in attributes:
                            info = attribute.get('info', {})
                            attr_name = info.get('name', '')
                            attr_type = info.get('type', '')
                            use = info.get('use', 'optional')
                            
                            # Create link to detailed documentation for this attribute
                            attr_label = f"{xml_type}.{root_type_name}.{attr_name}"
                            content += f"- :ref:`{attr_name} <{attr_label}>`: ``{attr_type}`` ({use})\n"
                        content += "\n"
        
        # Add the root type documentation right after structure
        if root_type_name and root_type_name in types:
            content += "Root Type Details\n"
            content += "-" * len("Root Type Details") + "\n\n"
            root_type_info = types[root_type_name]
            content += _generate_single_type_documentation(root_type_name, root_type_info, xml_type)
            content += "\n"
        
        # Add other types in schema reference
        content += "Schema Reference\n"
        content += "-" * len("Schema Reference") + "\n\n"
        content += _generate_types_documentation(types, xml_type, root_type_name)
    
    return content


def _generate_types_documentation(types: Dict[str, Any], xml_type: str, skip_type: Optional[str] = None) -> str:
    """Generate documentation for all types defined in the XML schema.
    
    Args:
        types: Dictionary of type definitions
        xml_type: The XML file type name
        skip_type: Optional type name to skip (e.g., to avoid duplicating the root type)
    """
    
    content = ""
    
    # Sort types for consistent output
    for type_name in sorted(types.keys()):
        # Skip the root type if specified (it was already documented)
        if skip_type and type_name == skip_type:
            continue
        
        type_info = types[type_name]
        content += _generate_single_type_documentation(type_name, type_info, xml_type)
    
    return content


def _generate_single_type_documentation(type_name: str, type_info: Dict[str, Any], xml_type: str) -> str:
    """Generate documentation for a single type."""
    
    label = f"{xml_type}.{type_name}"
    content = f".. _{label}:\n\n"
    content += f"{type_name}\n"
    content += "~" * len(type_name) + "\n\n"
    
    type_class = type_info.get('type', '')
    
    if type_class == 'complex':
        content += _generate_complex_type_documentation(type_info, xml_type, type_name)
    elif type_class == 'simple':
        content += _generate_simple_type_documentation(type_info, type_name)
    else:
        content += f":Type: {type_class}\n\n"
    
    return content


def _format_element_metadata(element: Dict[str, Any], xml_type: str) -> str:
    """Format element metadata as RST field list."""
    rst = ""
    
    info = element.get('info', {})
    element_type = info.get('type', 'unknown')
    min_occurs = info.get('minOccurs', 0)
    max_occurs = info.get('maxOccurs', 1)
    
    # Handle type that can be a list
    if isinstance(element_type, list):
        formatted_types = []
        for t in element_type:
            formatted_types.append(_format_type_reference(t, xml_type))
        element_type_str = " | ".join(formatted_types)
    else:
        element_type_str = _format_type_reference(element_type, xml_type)
    
    # Format occurrence
    if max_occurs == 1 and min_occurs == 1:
        occurrence = "Required (exactly once)"
    elif max_occurs == 1 and min_occurs == 0:
        occurrence = "Optional (0 or 1)"
    elif max_occurs == "unbounded":
        if min_occurs == 0:
            occurrence = "Zero or more"
        else:
            occurrence = f"One or more"
    else:
        occurrence = f"[{min_occurs}..{max_occurs}]"
    
    rst += f":Occurrence: {occurrence}\n"
    rst += f":Type: {element_type_str}\n"
    
    # Add blank line after field list
    if rst:
        rst += "\n"
    
    return rst


def _format_attribute_metadata(attribute: Dict[str, Any]) -> str:
    """Format attribute metadata as RST field list."""
    rst = ""
    
    info = attribute.get('info', {})
    attr_type = info.get('type', 'unknown')
    use = info.get('use', 'optional')
    
    # Format use as human readable
    if use == 'required':
        use_text = "Required"
    elif use == 'optional':
        use_text = "Optional"
    else:
        use_text = use.capitalize()
    
    rst += f":Type: ``{attr_type}``\n"
    rst += f":Use: {use_text}\n"
    
    # Add blank line after field list
    if rst:
        rst += "\n"
    
    return rst


def _format_type_reference(type_name: str, xml_type: str) -> str:
    """Format a type reference, creating a cross-reference link for custom types."""
    # Check if it's a custom type (starts with type_ or enum_)
    if type_name.startswith('type_') or type_name.startswith('enum_'):
        label = f"{xml_type}.{type_name}"
        return f":ref:`{type_name} <{label}>`"
    else:
        # Standard XML Schema type
        return f"``{type_name}``"


def _generate_complex_type_documentation(type_info: Dict[str, Any], xml_type: str, type_name: str) -> str:
    """Generate documentation for a complex type."""
    
    content = ":Type: Complex\n"
    
    # Add composition if present
    composition = type_info.get('composition', '')
    if composition:
        content += f":Composition: {composition}\n"
    
    # Add blank line after field list
    content += "\n"
    
    # Add elements section
    elements = type_info.get('elements', [])
    if elements:
        content += "Elements\n"
        content += "^" * len("Elements") + "\n\n"
        
        for element in elements:
            info = element.get('info', {})
            description = element.get('description', '')
            
            element_name = info.get('name', 'unknown')
            element_type = info.get('type', 'unknown')
            
            # Create label with xml_type and type_name prefix to avoid collisions
            label = f"{xml_type}.{type_name}.{element_name}"
            content += f".. _{label}:\n\n"
            content += f"{element_name}\n"
            content += "^" * len(element_name) + "\n\n"
            
            # Add metadata as field list
            content += _format_element_metadata(element, xml_type)
            
            # Add description if present - convert from HTML/markdown to RST
            if description:
                # Convert HTML/markdown to RST using m2r
                converted_desc = convert(description).strip()
                content += f"{converted_desc}\n\n"
    
    # Add attributes section
    attributes = type_info.get('attributes', [])
    if attributes:
        content += "Attributes\n"
        content += "^" * len("Attributes") + "\n\n"
        
        for attribute in attributes:
            info = attribute.get('info', {})
            description = attribute.get('description', '')
            
            attr_name = info.get('name', 'unknown')
            
            # Create label with xml_type and type_name prefix
            label = f"{xml_type}.{type_name}.{attr_name}"
            content += f".. _{label}:\n\n"
            content += f"{attr_name}\n"
            content += "^" * len(attr_name) + "\n\n"
            
            # Add metadata as field list
            content += _format_attribute_metadata(attribute)
            
            # Add description if present
            if description:
                converted_desc = convert(description).strip()
                content += f"{converted_desc}\n\n"
    
    return content


def _generate_simple_type_documentation(type_info: Dict[str, Any], type_name: str) -> str:
    """Generate documentation for a simple type."""
    
    content = ":Type: Simple\n"
    
    restriction = type_info.get('restriction', {})
    if restriction:
        base = restriction.get('base', '')
        if base:
            content += f":Base Type: ``{base}``\n"
        
        enumeration = restriction.get('enumeration', [])
        if enumeration:
            content += "\n"
            content += "Allowed Values\n"
            content += "^" * len("Allowed Values") + "\n\n"
            for enum_item in enumeration:
                # Handle both string and object enumeration values
                if isinstance(enum_item, str):
                    value = enum_item
                elif isinstance(enum_item, dict):
                    # Extract value from nested info object
                    info = enum_item.get('info', {})
                    value = info.get('value', str(enum_item))
                else:
                    value = str(enum_item)
                
                content += f"- ``{value}``\n"
            content += "\n"
        else:
            content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_xml_docs()
    exit(0 if success else 1)
