if __name__ == "__main__":
    raise ImportError("This module is not intended to be run directly. Please import it from the main script.")

import json
from pathlib import Path
from typing import Any

from documentation import Documentation, DocObject, DocObjectT, code_value_formatter, list_formatter
from project import PROJECT_ROOT, sanitize_description, INDENT
from utility.metadata import Metadata
from utility.rst import Headers, make_ref_label


## DEFINITIONS


## UTILITY

def patternFormatter(v: list[dict[str, str]]):
    patterns = [val['pattern'] for val in v]
    out = ", ".join([code_value_formatter("", "", val) for val in patterns])
    return out

## METADATA


## MAIN SUBCLASS

class _GenericTranslationDocObject(DocObject):
    description: str
    generic_name: str
    metadata_keys: list[dict[str, Any]] = []

    #FIXME: should use `-`, not `_`, but was kept for retro compatibility
    def sanitize_id(self, name: str) -> str:
        return name.lower().replace(' ', '_')

    # specific methods for translation doc objects
    def get_item_label(self, name: str) -> str:
        return f"{self.doc.doc_type}-{self.generic_name}-{name}"
        # return make_ref_label(self.doc.doc_type, f"{self.generic_name}-{name}")

    #TODO: should probably use something like for metadata
    def get_item_table(self, item: dict) -> str:
        if len(item) == 0:
            return ""

        out = f".. list-table::\n{INDENT}:widths: auto\n\n"
        for mk in self.metadata_keys:
            key = mk['key']
            if key not in item:
                continue
            name = mk['name']
            v = item[key]

            # format to code if needed
            if mk.get('formatter', None) is not None:
                v = mk['formatter'](v)
            elif mk.get('to_code', False):
                v = code_value_formatter("", "", v)
            out += f"{INDENT}* - {name}\n{INDENT}  - {v}\n"
        return out + "\n"

    def get_label(self) -> str:
        return f"{self.doc.doc_type}-{self.generic_name}"

    def get_header(self) -> str:
        description = self.description
        sanitized_description = sanitize_description(description)
        label = self.get_label()
        name = self.get_name()
        header = Headers.SECTION.make(name, label = label)
        header += sanitized_description
        return header

    def get_object_content(self) -> str:
        """Generate the content for a specific object's documentation."""
        out = ""
        data = sorted(self.data.values(), key=lambda x: x['name'].lower())
        for item in data:
            name = item['name']
            out += f"{Headers.SUBSECTION.make(name, label = self.get_item_label(name))}"

            out += self.get_item_table(item)

            # add description if available
            description = item.get('description', None)
            if description is not None:
                sanitized_description = sanitize_description(description)
                out += f"{sanitized_description}\n\n"
        return out

class FilesDocObject(_GenericTranslationDocObject):
    description: str = """
Available translation file types, their descriptions and properties. The majority of the time the key prefix for translation keys need to be included or they won't work. While this is not always the case, it's preferable to follow these guidelines to avoid issues with missing translations and to make it cleaner when referencing the translation keys in code or scripts.

The pattern properties are patterns that the translation keys must match in order to be valid, they are simply more specific rules than just the prefix if you are interested in knowing the details. Those were defined from the vanilla translation files for the most part and might be incomplete or too specific.
"""
    generic_name: str = "files"
    metadata_keys: list[dict[str, Any]] = [
        {"key": "fileName", "name": "File Name"},
        {"key": "function", "name": "Function", "to_code": True},
        {"key": "keyPrefix", "name": "Key Prefix", "to_code": True},
        {"key": "patternProperties", "name": "Pattern Properties", "formatter": patternFormatter},
    ]


class CodesDocObject(_GenericTranslationDocObject):
    description: str = """
Available language codes, full language names and encoding.
"""
    generic_name: str = "codes"
    metadata_keys: list[dict[str, Any]] = [
        {"key": "languageName", "name": "Language Name"},
        {"key": "encoding", "name": "Encoding"},
    ]

class TranslationDocumentation(Documentation):
    title = "Translations"
    doc_type = "translation"

    data_path_files = PROJECT_ROOT / "external" / "pz-translation-data" / "out" / "translationFiles.json"
    data_path_codes = PROJECT_ROOT / "external" / "pz-translation-data" / "out" / "languageCodes.json"

    toc_path = PROJECT_ROOT / "docs" / "source" / "translations.rst"

    docObjectFiles = FilesDocObject
    docObjectCodes = CodesDocObject

    translation_files: dict[str, dict] = {}
    language_codes: dict[str, dict] = {}


    def preload_data(self) -> None:
        """Preload translation data from JSON files."""
        with open(self.data_path_files, 'r', encoding='utf-8') as f:
            self.translation_files = json.load(f)
        with open(self.data_path_codes, 'r', encoding='utf-8') as f:
            self.language_codes = json.load(f)

    def prepare_data(self) -> None:
        """
        Prepare translation data for documentation.
        
        Each dataset type gets its own page, no need to split into multiple pages,
        the data is small enough to fit on one page each.
        """
        obj = self.docObjectFiles("Translation Files", self.translation_files, self, self.translation_files)
        self.objects.append(obj)

        obj = self.docObjectCodes("Language Codes", self.language_codes, self, self.language_codes)
        self.objects.append(obj)
