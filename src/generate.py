import argparse

import documentation
import docs # needed to load every doc types

# don't run this file if not main
if __name__ != "__main__":
    raise RuntimeError("This file should not be imported. It is meant to be run as a script.")


arg_parser = argparse.ArgumentParser(description="Generate documentation pages")
arg_parser.add_argument("type", type=str, help="Type of documentation to generate")
args = arg_parser.parse_args()

doc_type = args.type
try:
    documentation = documentation.create_documentation(doc_type)
    print(f"Created documentation of type: {doc_type}")
except ValueError as e:
    print(e)
