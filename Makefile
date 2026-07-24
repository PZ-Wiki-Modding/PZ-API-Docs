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
<<<<<<< HEAD
	python3 ./chores/_old/scripts/generateScriptsDocs.py
	python3 ./chores/main.py scripts

generate_mapping:
	source ./.venv/bin/activate
	python3 ./chores/_old/mapping/generateRoomsDocs.py
	python3 ./chores/_old/mapping/generateRoomsDistributionDocs.py
	python3 ./chores/_old/mapping/generateItemPickerContainerPropertiesDocs.py
	python3 ./chores/_old/mapping/generateProceduralDistributionsDocs.py
	python3 ./chores/_old/mapping/generateTilePropertiesDocs.py

generate_java:
	source ./.venv/bin/activate
	python3 ./chores/_old/java/generateColorsDocs.py
	python3 ./chores/_old/java/generateItemTagsDocs.py
	python3 ./chores/_old/java/generateActionSoundTimeDocs.py
	python3 ./chores/_old/java/generateMagazineSubjectDocs.py
	python3 ./chores/_old/java/generateMetabolicsDocs.py
	python3 ./chores/_old/java/generateItemBodyLocationDocs.py

generate_translations:
	source ./.venv/bin/activate
	python3 ./chores/main.py translation

generate_xml:
	source ./.venv/bin/activate
	python3 ./chores/main.py xml
=======
	python3 ./src/scripts/generateScriptsDocs.py

generate_mapping:
	source ./.venv/bin/activate
	python3 ./src/mapping/generateRoomsDocs.py
	python3 ./src/mapping/generateRoomsDistributionDocs.py
	python3 ./src/mapping/generateItemPickerContainerPropertiesDocs.py
	python3 ./src/mapping/generateProceduralDistributionsDocs.py
	python3 ./src/mapping/generateTilePropertiesDocs.py

generate_java:
	source ./.venv/bin/activate
	python3 ./src/java/generateColorsDocs.py
	python3 ./src/java/generateItemTagsDocs.py
	python3 ./src/java/generateActionSoundTimeDocs.py
	python3 ./src/java/generateMagazineSubjectDocs.py
	python3 ./src/java/generateMetabolicsDocs.py
	python3 ./src/java/generateItemBodyLocationDocs.py

generate_translations:
	source ./.venv/bin/activate
	python3 ./src/translations/generateLanguageCodesDocs.py
	python3 ./src/translations/generateTranslationFilesDocs.py

generate_xml:
	source ./.venv/bin/activate
	python3 ./src/xml/generateXMLDocs.py
>>>>>>> 4ca061f (reorganize files into src folder, include pyproject for details on the python setup. Added LICENSE and CONTRIBUTING files)

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
