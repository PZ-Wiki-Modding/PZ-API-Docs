

from pathlib import Path

if __name__ != "__main__":
    from documentation import Documentation
    from project import PROJECT_ROOT
else:
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")





class XMLDocumentation(Documentation):
    title = "XML"
    doc_type = "xml"
    data_path = PROJECT_ROOT / "pz-xml-data" / "out" / "data.json"
    toc_path = PROJECT_ROOT / "docs" / "xml.rst"

    def generate(self) -> None:
        print("Generating XML documentation...")

