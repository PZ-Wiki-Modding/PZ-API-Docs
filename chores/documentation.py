import argparse








class Documentation:
    doc_type: str = "__"
    doc_types: dict[str, type] = {}

    def __init__(self):
        self.generate()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        doc_type = cls.doc_type
        print(doc_type)
        Documentation.doc_types[doc_type] = cls

    @staticmethod
    def create(doc_type):
        if doc_type in Documentation.doc_types:
            return Documentation.doc_types[doc_type]()
        raise ValueError(f"Unknown documentation type: {doc_type}")
    
    def generate(self):
        raise NotImplementedError(f"Subclasses must implement the 'generate' method.")


class XMLDocumentation(Documentation):
    doc_type = "xml"




if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Generate documentation pages")
    arg_parser.add_argument("type", type=str, help="Type of documentation to generate")
    args = arg_parser.parse_args()

    doc_type = args.type
    try:
        documentation = Documentation.create(doc_type)
        print(f"Created documentation of type: {doc_type}")
    except ValueError as e:
        print(e)

















