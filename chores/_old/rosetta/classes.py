"""
Retrieve every available classes and their associated JavaDocs link
"""

import os
from pathlib import Path
import pprint

INPUT = Path(__file__).parent.parent.parent / "pz-rosetta-source" / "rosetta" / "java"
BASE_LINK = Path("https://demiurgequantified.github.io/ProjectZomboidJavaDocs")

# list every files and their parent directories up to the "java" directory
def list_classes(input_dir: Path) -> list[dict[str, str]]:
    classes = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".yml"):
                class_name = file[:-4]  # remove .yml extension
                relative_path = Path(root).relative_to(input_dir)
                link = BASE_LINK / relative_path / (class_name + ".html")
                classes.append({
                    "name": class_name,
                    "link": str(link).replace("\\", "/")  # ensure URL format
                })
    return classes

CLASS = list_classes(INPUT)

def find_class_link(class_name: str) -> str|None:
    for cls in CLASS:
        if cls['name'] == class_name:
            return cls['link']
    return None