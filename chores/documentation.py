import json, m2r
from pathlib import Path

from project import PROJECT_ROOT







class Documentation:
    _doc_types: dict[str, type] = {}

    # derived attributes
    title: str = "__BASE_TITLE"
    doc_type: str = "__BASE"
    data_path: Path = PROJECT_ROOT
    data: dict = {}
    toc_path: Path
    toc_elements: list[Path] = []

    def __init__(self):
        self.preload_data()
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
    
# subclass methods
    def preload_data(self) -> None:
        """Preload the documentation data."""
        assert self.data_path.exists(), f"Data path does not exist: {self.data_path}"
        with open(self.data_path, "r") as f:
            self.data = json.load(f)

    def generate(self) -> None:
        """Generate the documentation.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError(f"Subclasses must implement the 'generate' method.")
    
    def generate_toc(self) -> None:
        """Generate the table of contents (TOC) for the documentation."""
        with open(self.toc_path, "w") as f:
            pass


