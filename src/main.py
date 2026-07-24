import argparse

from documentation import Documentation

# load documentation types
# from docs import xml
import docs


# don't run this file if not main
if __name__ != "__main__":
    exit(1)


arg_parser = argparse.ArgumentParser(description="Generate documentation pages")
arg_parser.add_argument("type", type=str, help="Type of documentation to generate")
args = arg_parser.parse_args()

doc_type = args.type
try:
    documentation = Documentation.create(doc_type)
    print(f"Created documentation of type: {doc_type}")
except ValueError as e:
    print(e)
