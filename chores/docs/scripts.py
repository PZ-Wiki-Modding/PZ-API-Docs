if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

from pathlib import Path

from documentation import Documentation
from project import PROJECT_ROOT, sanitize_description
from utility.metadata import metadata
from utility.rst import headers


## DEFINITIONS

TOC_DESCRIPTION = """
This section provides detailed documentation for all available `script <https://pzwiki.net/wiki/Scripts>`_ blocks.
"""


## METADATA


## UTILITY

def _get_block_link(block_name: str) -> str:
    """Get the documentation page name for a block."""
    l = block_name.lower()
    return l.replace(' ', '-')


## MAIN SUBCLASS

class ScriptsDocumentation(Documentation):
    title = "ScriptsDocs"
    doc_type = "scripts"
    data_path = PROJECT_ROOT / "pz-scripts-data" / "out" / "scriptBlocks.json"

    toc_path = PROJECT_ROOT / "docs" / "source" / "scripts.rst"
    toc_description = TOC_DESCRIPTION
    toc_depth = 4

    def pre_toc(self) -> None:
        default_path = Path("scripts")
        for block_data in self.data.values():
            script_file_path = default_path

            block_name = block_data['name']

            isVariant = block_data.get("isVariant", None)
            if isVariant is not None:
                # script_file_path = script_file_path / _get_block_link(isVariant)
                continue

            script_file_path = script_file_path / _get_block_link(block_name)
            self.toc_elements.append(script_file_path)

        def get_object_content(self, object_type: str, object_data: dict) -> str:
            """Get the content for a specific script block."""

            # init
            content = "\n"


            return content

