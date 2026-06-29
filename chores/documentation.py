import json, m2r
from pathlib import Path

from project import PROJECT_ROOT, INDENT, sanitize_description
from utility import echo
from utility.rst import headers



TOC_INSTRUCTIONS_TITLE = "Documentation Instructions"

## UTILITY

def make_toc_tree(toc_elements: list[Path], toc_depth: int = 2) -> str:
    """Create a TOC tree string for the provided elements."""
    out = headers.SUBSECTION.make("Table of Contents")
    out += ".. toctree::" + "\n"
    out += f"   :maxdepth: {toc_depth}\n"
    out += "   :titlesonly:\n\n"
    for element in toc_elements:
        out += f"{INDENT}{element}\n"
    return out

def code_value_formatter(object_type: str, key: str, value: str) -> str:
    """Format the value for metadata output."""
    return f"``{value}``"

## MAIN CLASS

class Documentation:
    _doc_types: dict[str, type] = {}

    # derived attributes
    title: str = "__BASE_TITLE"
    doc_type: str = "__BASE"
    data_path: Path = PROJECT_ROOT
    data: dict = {}
    
    toc_path: Path
    toc_elements: list[Path] = []
    toc_description: str = "Documentation description not provided."
    toc_depth: int = 2

    def __init__(self):
        self.preload_data()
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
        out = headers.SECTION.make(title)
        out += self.toc_description.strip() + "\n\n"

        # make reading instructions
        instructions = self.generate_instructions()
        if instructions is not None:
            out += headers.SUBSECTION.make(TOC_INSTRUCTIONS_TITLE)
            out += instructions.strip() + "\n\n"

        # make toc tree
        out += make_toc_tree(toc_elements, self.toc_depth)

        # output toc file
        with open(toc_path, "w") as f:
            f.write(out)

    def generate_instructions(self) -> str | None:
        return None

    def generate(self) -> None:
        """Generate the documentation."""
        for object_type, object_data in self.data.items():
            out = self.generate_object(object_type, object_data)

            # retrieve doc element path
            out_path = self.get_object_path(object_type, object_data)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w") as f:
                f.write(out)


## object doc generation

    def get_object_path(self, object_type: str, object_data: dict) -> Path:
        """Retrieve the output path for a specific object's documentation."""
        # default output path is the toc path directory with the toc path's stem
        object_out_dir = self.toc_path.parent / self.toc_path.stem
        return object_out_dir / f"{object_type}.rst"

    def generate_object(self, object_type: str, object_data: dict) -> str:
        """Associate the generic header for the object documentation with the content."""
        header = self.get_object_header(object_type, object_data)
        content = self.get_object_content(object_type, object_data)
        out = f"{header}\n\n{content}"
        return out
    
    def get_object_label(self, object_type: str, object_data: dict) -> str:
        """Retrieve the label for a specific object's documentation."""
        return f"{self.doc_type}-{object_type.lower().replace(' ', '-')}"

    def get_object_header(self, object_type: str, object_data: dict) -> str:
        """Retrieve the header for a specific object's documentation. This should be a RST header with the object's title and description."""
        description = object_data.get("description", "No description provided.")
        sanitized_description = sanitize_description(description)
        label = self.get_object_label(object_type, object_data)
        header = headers.SECTION.make(object_type, label = label)
        header += sanitized_description.strip()
        return header

    def get_object_content(self, object_type: str, object_data: dict) -> str:
        return ""