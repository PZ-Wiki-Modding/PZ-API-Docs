.PHONY: help clean html generate serve pdf

SHELL := /bin/bash

help:
	@echo "Sphinx documentation builder"
	@echo "Available targets:"
	@echo "  generate  - Generate RST files from YAML block definitions"
	@echo "  html      - Build HTML documentation"
	@echo "  pdf       - Build PDF documentation"
	@echo "  clean     - Remove generated documentation"
	@echo "  serve     - Serve documentation on http://localhost:8000"

clean:
	rm -rf build
	rm -rf source/blocks

generate:
	python3 ../chores/generateDocs.py

html: generate
	sphinx-build -b html source build/html

serve: html
	cd build/html && python3 -m http.server 8000

pdf: generate
	sphinx-build -b latex source build/latex
	cd build/latex && make
