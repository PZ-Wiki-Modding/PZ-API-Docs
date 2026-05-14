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

generate_scripts:
	source ./.venv/bin/activate
	python3 ./chores/scripts/generateScriptsDocs.py

generate_distributions:
	source ./.venv/bin/activate
	python3 ./chores/distributions/generateRoomsDocs.py
	python3 ./chores/distributions/generateRoomsDistributionDocs.py
	python3 ./chores/distributions/generateItemPickerContainerPropertiesDocs.py
	python3 ./chores/distributions/generateProceduralDistributionsDocs.py
	python3 ./chores/translations/generateLanguageCodesDocs.py
	python3 ./chores/translations/generateTranslationFilesDocs.py

generate: generate_scripts generate_distributions

html: generate
	source ./.venv/bin/activate
	cd docs
	sphinx-build -b html source build/html

serve: html
	source ./.venv/bin/activate
	cd docs
	cd build/html && python3 -m http.server 8000

pdf: generate
	source ./.venv/bin/activate
	cd docs
	sphinx-build -b latex source build/latex
	cd build/latex && make
