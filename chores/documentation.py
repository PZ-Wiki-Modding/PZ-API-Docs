import json, m2r
from pathlib import Path

from project import PROJECT_ROOT, INDENT
from utility import echo



DEFAULT_TOC_FORMAT = """{title}
{title_line}

{toc_description}

.. toctree::
   :maxdepth: {toc_depth}
   :titlesonly:

   {toc_elements}
"""

DEFAULT_ELEMENT_FORMAT = """{title}
{title_line}

{description}"""




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
    
## utility
    def sanitize_description(self, description: str) -> str:
        """Sanitize the provided description by converting Markdown to reStructuredText."""
        return m2r.convert(description)

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
        toc_path = self.toc_path
        toc_path.parent.mkdir(parents=True, exist_ok=True)
        echo.path(toc_path.relative_to(PROJECT_ROOT), prefix="Creating TOC file:")
        toc_elements = sorted(self.toc_elements, key=lambda p: str(p))
        with open(toc_path, "w") as f:
            text = DEFAULT_TOC_FORMAT.format(
                title=self.title,
                title_line="=" * len(self.title),
                toc_description=self.toc_description.strip(),
                toc_depth=self.toc_depth,
                toc_elements=f"\n{INDENT}".join(str(el) for el in toc_elements)
            )

            f.write(text)

    def generate(self) -> None:
        """Generate the documentation."""
        for element_type, element_data in self.data.items():
            self.generate_data_element(element_type, element_data)


## element doc generation

    def generate_data_element(self, element_type: str, element_data: dict) -> str:
        header = self.get_element_header(element_type, element_data)
        out_path = self.get_element_path(element_type, element_data)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        content = self.get_element_content(element_type, element_data)
        out = f"{header}\n\n{content}"
        with open(out_path, "w") as f:
            f.write(out)

    def get_element_path(self, element_type: str, element_data: dict) -> Path:
        element_out_dir = self.toc_path.parent / self.toc_path.stem
        return element_out_dir / f"{element_type}.rst"

    def get_element_header(self, element_type: str, element_data: dict) -> str:
        description = element_data.get("description", "No description provided.")
        sanitized_description = self.sanitize_description(description)
        header = DEFAULT_ELEMENT_FORMAT.format(
            title=element_type,
            title_line="=" * len(element_type),
            description=sanitized_description.strip()
        ).strip()
        return header

    def get_element_content(self, element_type: str, element_data: dict) -> str:
        return ""