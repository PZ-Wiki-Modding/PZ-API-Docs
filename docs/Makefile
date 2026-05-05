.PHONY: help clean html generate serve pdf
.ONESHELL:

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
	rm -rf source/scripts

generate:
	source ../.venv/bin/activate
	python3 ../chores/generateScriptsDocs.py
	python3 ../chores/generateRoomsDocs.py
	python3 ../chores/generateRoomsDistributionDocs.py
	python3 ../chores/generateProceduralDistributionsDocs.py
	python3 ../chores/generateItemPickerContainerPropertiesDocs.py

html: generate
	source ../.venv/bin/activate
	sphinx-build -b html source build/html

serve: html
	source ../.venv/bin/activate
	cd build/html && python3 -m http.server 8000

pdf: generate
	source ../.venv/bin/activate
	sphinx-build -b latex source build/latex
	cd build/latex && make
