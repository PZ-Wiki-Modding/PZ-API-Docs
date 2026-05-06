#!/usr/bin/env python3
"""
Generate procedural distributions documentation from procedural_distributions.json
and write to procedural_distributions.rst
"""

import json
from pathlib import Path
from collections import defaultdict


WIKI_LINK = Path("https://pzwiki.net/wiki")


def generate_procedural_distributions_docs():
    """Generate and write procedural distributions documentation to RST file."""
    
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    distributions_json_path = repo_root / "pz-lua-parser" / "out" / "procedural_distributions.json"
    distributions_rst_path = repo_root / "docs" / "source" / "distribution" / "procedural_distributions.rst"
    
    # Read distributions from JSON
    if not distributions_json_path.exists():
        print(f"Error: {distributions_json_path} not found")
        return False
    
    try:
        with open(distributions_json_path, 'r') as f:
            distributions = json.load(f)
    except Exception as e:
        print(f"Error reading procedural_distributions.json: {e}")
        return False
    
    # Load item names
    item_names_path = repo_root / "pz-lua-parser" / "out" / "item_names.json"
    try:
        with open(item_names_path, 'r') as f:
            item_names = json.load(f)
    except Exception as e:
        print(f"Error reading item_names.json: {e}")
        item_names = {}
    
    # Generate RST content
    rst_content = generate_rst_content(distributions, item_names)
    
    # Ensure output directory exists
    distributions_rst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to RST file
    try:
        with open(distributions_rst_path, 'w') as f:
            f.write(rst_content)
        print(f"Successfully generated {distributions_rst_path}")
        print(f"Total procedural distributions: {len(distributions)}")
        return True
    except Exception as e:
        print(f"Error writing to procedural_distributions.rst: {e}")
        return False


def generate_rst_content(distributions: dict, item_names: dict) -> str:
    """Generate RST formatted content for procedural distributions."""
    
    content = """Procedural distributions
========================

Detailed procedural distribution lists of items with estimated chances.

The calculation of the estimated chance is not fully accurate. It sums up the weights of the item, divide it by the total weight of the procedural distribution, then multiply it by the rolls multiplier.

"""
    
    # Sort distributions alphabetically
    sorted_distributions = sorted(distributions.keys(), key=str.lower)
    
    for dist_name in sorted_distributions:
        dist_data = distributions[dist_name]
        
        # Add anchor label for reference
        anchor = f"procedural-distribution-{dist_name}"
        content += f".. _{anchor}:\n\n"
        
        # Add distribution header (level 2)
        content += f"{dist_name}\n"
        content += "-" * len(dist_name) + "\n\n"
        
        # Get rolls value
        rolls = dist_data.get('rolls', 1)
        
        # Collect all items and their weights from both items and junk lists
        item_weights = defaultdict(float)
        
        # Process items list
        if isinstance(dist_data, dict):
            items_list = dist_data.get('items', [])
            if items_list:
                # items list is a list of [item_name, weight] pairs
                for item_pair in items_list:
                    if isinstance(item_pair, list) and len(item_pair) >= 2:
                        item_name = item_pair[0]
                        weight = item_pair[1]
                        try:
                            item_weights[item_name] += float(weight)
                        except (ValueError, TypeError):
                            pass
            
            # Process junk list (which contains an items entry)
            junk_data = dist_data.get('junk', {})
            if isinstance(junk_data, dict):
                junk_items_list = junk_data.get('items', [])
                if junk_items_list:
                    # junk items list is a list of [item_name, weight] pairs
                    for item_pair in junk_items_list:
                        if isinstance(item_pair, list) and len(item_pair) >= 2:
                            item_name = item_pair[0]
                            weight = item_pair[1]
                            try:
                                item_weights[item_name] += float(weight)
                            except (ValueError, TypeError):
                                pass
        
        # If no items found, add note
        if not item_weights:
            content += "*No items defined.*\n\n"
            continue
        
        # Calculate total weight
        total_weight = sum(item_weights.values())
        
        # Calculate chances with rolls multiplier and prepare for sorting
        item_chances = []
        for item_name, weight in item_weights.items():
            if total_weight > 0:
                chance = (weight / total_weight) * 100 * rolls
            else:
                chance = 0
            item_chances.append((item_name, chance))
        
        # Sort by chance descending
        item_chances.sort(key=lambda x: x[1], reverse=True)
        
        # Add table for items with estimated chances
        content += ".. list-table::\n"
        content += "   :header-rows: 1\n"
        content += "   :widths: auto\n\n"
        content += "   * - Item\n"
        content += "     - Estimated Chance\n"
        
        for item_name, chance in item_chances:
            link = WIKI_LINK / ".".join(item_name.split('.')[1:])
            item_name = item_names.get(item_name, f"{item_name}")  # Get human-readable name if available
            chance_str = f"{chance:.2f}%"
            content += f"   * - `{item_name} <{link}>`_\n"
            content += f"     - {chance_str}\n"
        
        content += "\n"
    
    return content


if __name__ == "__main__":
    success = generate_procedural_distributions_docs()
    exit(0 if success else 1)
