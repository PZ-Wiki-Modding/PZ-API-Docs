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
	./.venv/bin/python ./chores/scripts/generateScriptsDocs.py

generate_mapping:
	./.venv/bin/python ./chores/mapping/generateRoomsDocs.py
	./.venv/bin/python ./chores/mapping/generateRoomsDistributionDocs.py
	./.venv/bin/python ./chores/mapping/generateItemPickerContainerPropertiesDocs.py
	./.venv/bin/python ./chores/mapping/generateProceduralDistributionsDocs.py
	./.venv/bin/python ./chores/mapping/generateTilePropertiesDocs.py

generate_java:
	./.venv/bin/python ./chores/java/generateColorsDocs.py
	./.venv/bin/python ./chores/java/generateItemTagsDocs.py
	./.venv/bin/python ./chores/java/generateActionSoundTimeDocs.py
	./.venv/bin/python ./chores/java/generateMagazineSubjectDocs.py
	./.venv/bin/python ./chores/java/generateMetabolicsDocs.py

generate_translations:
	./.venv/bin/python ./chores/translations/generateLanguageCodesDocs.py
	./.venv/bin/python ./chores/translations/generateTranslationFilesDocs.py

generate: generate_scripts generate_mapping generate_java generate_translations

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
