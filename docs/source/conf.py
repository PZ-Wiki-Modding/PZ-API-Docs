# Configuration file for the Sphinx documentation builder.

import os
import sys
import re
import json
from pathlib import Path

# Add parent directory and docs directory to path
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))

SCRIPT_PATH = os.path.dirname(__file__)

with open(os.path.join(SCRIPT_PATH, '../../project.json'), 'r') as f:
    project_info = json.load(f)

project = project_info['project']
author = project_info['author']
game_version = project_info['game_version']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_reredirects',
]

redirects = {
    "scripts/root-blends": "./roots/blends.html",
    "scripts/root-default": "./roots/default.html",
    "scripts/root-mapbasexml": "./roots/mapbasexml.html",
    "scripts/root-mapinfo": "./roots/mapinfo.html",
    "scripts/root-modinfo": "./roots/modinfo.html",
    "scripts/root-rules": "./roots/rules.html",
    "scripts/root-sandboxoptions": "./roots/sandboxoptions.html",
    "scripts/root-scripts": "./roots/scripts.html",
    "scripts/root-spritemodels": "./roots/spritemodels.html",
    "scripts/root-tilegeometry": "./roots/tilegeometry.html",
    "scripts/root-tmxconfig": "./roots/tmxconfig.html",
}

templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    # 'mapping/**',
]

# html_theme = 'pydata_sphinx_theme'
html_theme = "furo"
html_static_path = ['_static']
html_title = f"{project} {game_version}"
html_logo = None
html_favicon = "_static/favicon.ico"
html_css_files = [
    'custom.css',
]

html_theme_options = {
    'collapse_navigation': True,
#     'navigation_depth': 10,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/PZ-Wiki-Modding/PZ-API-Docs",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],

    "source_repository": "https://github.com/PZ-Wiki-Modding/PZ-API-Docs",
    "source_branch": "main",
    "source_directory": "docs",
    # "announcement": "<em>Important</em> announcement!",
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
