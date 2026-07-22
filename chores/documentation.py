import json, m2r
from pathlib import Path
from typing import Any, TypeVar, Generic, TYPE_CHECKING, overload

from project import PROJECT_ROOT, INDENT, sanitize_description
from utility import echo
from utility.rst import Headers

if TYPE_CHECKING:
    from utility.metadata import Metadata


TOC_INSTRUCTIONS_TITLE = "Documentation Instructions"
TOC_TITLE = "Table of Contents"

## UTILITY

def make_toc_tree(toc_elements: list[Path], toc_depth: int = 2) -> str:
    """Create a TOC tree string for the provided elements."""
    out = Headers.SUBSECTION.make(TOC_TITLE)
    out += ".. toctree::" + "\n"
    out += f"   :maxdepth: {toc_depth}\n"
    out += "   :titlesonly:\n\n"
    for element in toc_elements:
        out += f"{INDENT}{element}\n"
    return out

def code_value_formatter(object_type: str, key: str, value: str) -> str:
    """Format the value for metadata output."""
    return f"``{value}``"

def list_formatter(obj: "DocObject", key: str, value_list: list) -> str:
    """Format a list of values for metadata output."""
    if not isinstance(value_list, list):
        return code_value_formatter(obj.name, key, value_list)
    out = ""
    for i, v in enumerate(value_list):
        out += f"* {code_value_formatter(obj.name, key, v)}\n"
    return "\n" + out.strip()


## MAIN CLASS



class DocObject:
    headerMetadata: 'Metadata | None' = None
    def __init__(self, object_type: str, object_data: Any, doc: "Documentation", source_data: dict) -> None:
        self.name = object_type
        #FIXME: this is not stable across changes to object_type, use manifest of some sort ?
        self.id = self.sanitize_id(object_type)
        self.data = object_data
        self.doc = doc
        self.source_data = source_data
    
    def sanitize_id(self, name: str) -> str:
        return name.lower().replace(' ', '-')



    def get_object_path(self) -> Path:
        """Retrieve the output path for a specific object's documentation."""
        # default output path is the toc path directory with the toc path's stem
        object_out_dir = self.doc.toc_path.parent / self.doc.toc_path.stem
        return object_out_dir / f"{self.id}.rst"

    def generate_object(self) -> str:
        """Associate the generic header for the object documentation with the content."""
        header = self.get_header()
        content = self.get_object_content()
        out = f"{header}\n\n{content}"
        return out

    def get_name(self) -> str:
        return self.name # default to original object_type

    def get_label(self) -> str:
        """Retrieve the label for a specific object's documentation."""
        return f"{self.doc.doc_type}-{self.id}"

    def get_header(self) -> str:
        """Retrieve the header for a specific object's documentation. This should be a RST header with the object's title and description."""
        description = self.data.get("description")
        if description is None or not description.strip():
            description = "No description provided."
        sanitized_description = sanitize_description(description)
        label = self.get_label()
        name = self.get_name()
        header = Headers.SECTION.make(name, label = label)
        if self.headerMetadata is not None:
            header += self.headerMetadata.generate(self, self.data) + "\n\n"
        header += sanitized_description
        return header

    def get_object_content(self) -> str:
        return ""

DocObjectT = TypeVar('DocObjectT', bound=DocObject)



class Documentation(Generic[DocObjectT]):
    _doc_types: dict[str, type] = {}

    # derived attributes
    title: str = "__BASE_TITLE"
    doc_type: str = "__BASE"
    data_path: Path = PROJECT_ROOT
    data: dict = {}

    docObject: type[DocObjectT]
    objects: list[DocObjectT] = []

    toc_path: Path
    toc_elements: list[Path] = []
    toc_description: str = "Documentation description not provided."
    toc_depth: int = 2

    def __init__(self):
        self.preload_data()
        self.prepare_data()
        self.pre_toc()
        self.generate_toc()
        self.generate()

    def __init_subclass__(cls, **kwargs):
        # when a subclass is created, register it in the _doc_types dictionary
        super().__init_subclass__(**kwargs)
        doc_type = cls.doc_type
        Documentation._doc_types[doc_type] = cls

    @staticmethod
    def create(doc_type: str) -> "Documentation":
        """Factory method to create a documentation instance based on the provided type.

        Args:
            doc_type (str): The type of documentation to create.

        Raises:
            ValueError: If the provided documentation type is unknown.

        Returns:
            Documentation: An instance of the requested documentation type.
        """
        if doc_type in Documentation._doc_types:
            return Documentation._doc_types[doc_type]()
        raise ValueError(f"Unknown documentation type: {doc_type}")

## subclass methods
    def preload_data(self) -> None:
        """Preload the documentation data."""
        assert self.data_path.exists(), f"Data path does not exist: {self.data_path}"
        with open(self.data_path, "r") as f:
            self.data = json.load(f)
    
    def prepare_data(self) -> None:
        for object_type, object_data in self.data.items():
            obj = self.docObject(object_type, object_data, self, self.data)
            self.objects.append(obj)

    def pre_toc(self) -> None:
        """Prepare the table of contents (TOC) elements."""
        pass

    def generate_toc(self) -> None:
        """Generate the table of contents (TOC) for the documentation."""
        # retrieve toc path
        toc_path = self.toc_path
        toc_path.parent.mkdir(parents=True, exist_ok=True)
        echo.path(toc_path.relative_to(PROJECT_ROOT), prefix="Creating TOC file:")

        # sort toc elements
        toc_elements = sorted(self.toc_elements, key=lambda p: str(p))
        
        # format toc text
        title = self.title
        out = Headers.SECTION.make(title)
        out += self.toc_description.strip() + "\n\n"

        # make reading instructions
        instructions = self.generate_instructions()
        if instructions is not None:
            out += Headers.SUBSECTION.make(TOC_INSTRUCTIONS_TITLE)
            out += instructions.strip() + "\n\n"

        # make contributing section
        contribute = self.generate_contributing()
        if contribute is not None:
            out += Headers.SUBSECTION.make("Contributing")
            out += contribute.strip() + "\n\n"

        # make toc tree
        out += make_toc_tree(toc_elements, self.toc_depth)

        # output toc file
        with open(toc_path, "w") as f:
            f.write(out)

    def generate_instructions(self) -> str | None:
        return None

    def generate_contributing(self) -> str | None:
        return None

    def generate(self) -> None:
        """Generate the documentation."""
        for obj in self.objects:
            out = obj.generate_object()

            # retrieve doc element path
            out_path = obj.get_object_path()
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w") as f:
                f.write(out)
                echo.path(out_path, prefix="Creating object file:")
