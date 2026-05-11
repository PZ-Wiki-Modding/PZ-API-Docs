# Configuration file for the Sphinx documentation builder.

import os
import sys
import re
import json
from pathlib import Path

# Add parent directory and docs directory to path
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))

with open('../../project.json', 'r') as f:
    project_info = json.load(f)

project = project_info['project']
author = project_info['author']
game_version = project_info['game_version']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = f"{project} {game_version}"
html_logo = None
html_favicon = None
html_css_files = [
    'custom.css',
]

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 10,
    "external_links": [
        {"name": "JavaDocs", "url": "https://demiurgequantified.github.io/ProjectZomboidJavaDocs/"},
        {"name": "LuaDocs", "url": "https://demiurgequantified.github.io/ProjectZomboidLuaDocs/"},
        {"name": "ZedScripts", "url": "https://pzwiki.net/wiki/ZedScripts"},
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/SirDoggyJvla/pz-scripts-data",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        # {
        #     "name": "ZedScripts",
        #     "url": "https://pzwiki.net/wiki/ZedScripts",
        #     "icon": "https://raw.githubusercontent.com/SirDoggyJvla/ZedScripts/refs/heads/main/images/pz-script.png",
        #     "type": "url",
        # },
   ]
}

# LaTeX output options
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}

latex_engine = 'xelatex'

# Output for man pages
man_pages = [
    ('index', 'scripts-api', 'ScriptsDocs',
     ['Scripts-Data Contributors'], 1)
]


def remove_emojis_from_latex(app, exception):
    """Remove emoji characters from LaTeX output files for PDF generation."""
    if app.builder.name != 'latex' or exception is not None:
        return
    
    # Pattern to match emoji and other problematic Unicode characters
    # This includes most emoji ranges
    emoji_pattern = re.compile(
        r'[\U0001F300-\U0001F9FF]|'  # Emojis and symbols
        r'[\u2600-\u27BF]|'  # Miscellaneous Symbols
        r'[\U0001F600-\U0001F64F]',  # Emoticons
        flags=re.UNICODE
    )
    
    latex_dir = Path(app.outdir)
    if not latex_dir.exists():
        return
    
    # Process all .tex files
    for tex_file in latex_dir.glob('*.tex'):
        try:
            content = tex_file.read_text(encoding='utf-8')
            # Remove emoji characters
            cleaned_content = emoji_pattern.sub('', content)
            if cleaned_content != content:
                tex_file.write_text(cleaned_content, encoding='utf-8')
                print(f"Removed emojis from {tex_file.name}")
        except Exception as e:
            print(f"Error processing {tex_file.name}: {e}")


def setup(app):
    """Setup event handlers."""
    # app.add_css_file('custom.css')
    app.connect('build-finished', remove_emojis_from_latex)
