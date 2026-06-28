

from pathlib import Path

if __name__ != "__main__":
    from documentation import Documentation
    from project import PROJECT_ROOT
else:
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")




TOC_DESCRIPTION = """
Reference documentation for XML file formats used in Project Zomboid. With this documentation, comes settings that you can use for `VSCode <https://pzwiki.net/wiki/Visual_Studio_Code>`_ alongside the `RedHat XML <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`_ extension to automatically verify your files. You can find `here <https://github.com/PZ-Wiki-Modding/pz-xml-data/blob/main/out/settings.json>`_ these settings.
"""



class XMLDocumentation(Documentation):
    title = "XML"
    doc_type = "xml"
    data_path = PROJECT_ROOT / "pz-xml-data" / "out" / "data.json"
    toc_path = PROJECT_ROOT / "docs" / "source" / "xml.rst"
    toc_description = TOC_DESCRIPTION

    def pre_toc(self) -> None:
        for xml_type, type_data in self.data.items():
            xml_file_path = Path(f"xml/{xml_type}")
            self.toc_elements.append(xml_file_path)

