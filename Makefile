.PHONY: help clean html generate serve pdf
.ONESHELL:

SHELL := /bin/bash
QUICK ?= 0

help:
	@echo "Sphinx documentation builder"
	@echo "Available targets:"
	@echo "  setup     - Setup the required Python environment"
	@echo "  clean     - Remove generated documentation"
	@echo "  generate  - Generate RST files from YAML block definitions"
	@echo "  html      - Build HTML documentation"
	@echo "  serve     - Serve documentation on http://localhost:8000"
	@echo "  pdf       - Build PDF documentation"
	@echo ""
	@echo "Pass 'QUICK=1' to ignore mapping files (faster to compile)"

setup:
	rm -rf .venv
	python3 -m venv .venv
	echo "*" >> .venv/.gitignore
	source .venv/bin/activate
	pip install .

clean:
	rm -rf build
	rm -rf source/scripts

generate_scripts:
	.venv/bin/python3 ./src/main.py scripts

generate_mapping:
	.venv/bin/python3 ./src/_old/mapping/generateRoomsDocs.py
	.venv/bin/python3 ./src/_old/mapping/generateRoomsDistributionDocs.py
	.venv/bin/python3 ./src/_old/mapping/generateItemPickerContainerPropertiesDocs.py
	.venv/bin/python3 ./src/_old/mapping/generateProceduralDistributionsDocs.py
	.venv/bin/python3 ./src/_old/mapping/generateTilePropertiesDocs.py

generate_java:
	.venv/bin/python3 ./src/_old/java/generateColorsDocs.py
	.venv/bin/python3 ./src/_old/java/generateItemTagsDocs.py
	.venv/bin/python3 ./src/_old/java/generateActionSoundTimeDocs.py
	.venv/bin/python3 ./src/_old/java/generateMagazineSubjectDocs.py
	.venv/bin/python3 ./src/_old/java/generateMetabolicsDocs.py
	.venv/bin/python3 ./src/_old/java/generateItemBodyLocationDocs.py

generate_translations:
	.venv/bin/python3 ./src/main.py translation

generate_xml:
	.venv/bin/python3 ./src/main.py xml

generate: generate_scripts generate_mapping generate_java generate_translations generate_xml
# 	echo ${QUICK}

html: generate
	source ./.venv/bin/activate
	cd docs
	if [[ "${QUICK}" -eq 1 ]]; then
		export QUICK_BUILD=1
	else
		export QUICK_BUILD=0
	fi
	sphinx-build -b html source build/html

serve: html
	cd docs/build/html
	.venv/bin/python3 -m http.server 8000

pdf: generate
	source ./.venv/bin/activate
	cd docs
	sphinx-build -b latex source build/latex
	cd build/latex && make
