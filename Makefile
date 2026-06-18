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

generate_mapping:
	source ./.venv/bin/activate
	python3 ./chores/mapping/generateRoomsDocs.py
	python3 ./chores/mapping/generateRoomsDistributionDocs.py
	python3 ./chores/mapping/generateItemPickerContainerPropertiesDocs.py
	python3 ./chores/mapping/generateProceduralDistributionsDocs.py
	python3 ./chores/mapping/generateTilePropertiesDocs.py

generate_java:
	source ./.venv/bin/activate
	python3 ./chores/java/generateColorsDocs.py
	python3 ./chores/java/generateItemTagsDocs.py
	python3 ./chores/java/generateActionSoundTimeDocs.py
	python3 ./chores/java/generateMagazineSubjectDocs.py
	python3 ./chores/java/generateMetabolicsDocs.py
	python3 ./chores/java/generateItemBodyLocationDocs.py

generate_translations:
	source ./.venv/bin/activate
	python3 ./chores/translations/generateLanguageCodesDocs.py
	python3 ./chores/translations/generateTranslationFilesDocs.py

generate_xml:
	source ./.venv/bin/activate
	python3 ./chores/xml/generateXMLDocs.py

generate: generate_scripts generate_mapping generate_java generate_translations generate_xml

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
