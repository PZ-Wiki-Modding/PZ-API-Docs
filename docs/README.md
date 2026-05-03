# API Reference Documentation

This directory contains the Sphinx documentation for the Project Zomboid Scripts API reference.

## Structure

- `source/` - Source files for Sphinx documentation
  - `conf.py` - Sphinx configuration
  - `index.rst` - Main documentation index
  - `blocks/` - Auto-generated block documentation
  - `_static/` - Static assets (CSS, images, etc.)
  - `_templates/` - Custom Sphinx templates

- `build/` - Generated HTML documentation (created during build)

## Setup

The documentation requires Sphinx and related dependencies. These are already listed in the project's `requirements.txt`:

```bash
pip install -r ../requirements.txt
```

## Generating Documentation

### Quick Start

To generate and build the documentation in one step:

```bash
make html
```

### Step by Step

1. **Generate block documentation from YAML:**
   ```bash
   python ../scripts/generate_docs.py
   ```
   This creates RST files in `source/blocks/` from the YAML definitions in `../data/blocks/`

2. **Build HTML documentation:**
   ```bash
   sphinx-build -b html source build/html
   ```

### Using the Makefile

Available targets:

- `make generate` - Generate RST files from YAML block definitions
- `make html` - Generate and build HTML documentation
- `make clean` - Remove generated files and build output
- `make serve` - Build documentation and serve it locally

## Viewing Documentation

### Option 1: Direct File Access
Open `build/html/index.html` in your web browser.

### Option 2: Local Server
```bash
make serve
```
Then visit `http://localhost:8000` in your browser.

## Documentation Features

### Automated Generation
The `scripts/generate_docs.py` script automatically generates documentation from the YAML block definitions. This ensures the documentation is always in sync with the actual block definitions.

### Modular Structure
Each block type gets its own RST file with:
- Block description
- Parent/child block relationships
- Parameter documentation
- Default values and constraints

### Interactive HTML Output
The generated HTML includes:
- Full-text search
- Navigation sidebar
- Cross-references between blocks
- Syntax highlighting

## Adding/Updating Block Documentation

1. Update the YAML block definition in `../data/blocks/`
2. Run `make generate` to regenerate the RST files
3. Run `make html` to rebuild the HTML

## Building Other Formats

### PDF
```bash
sphinx-build -b latex source build/latex
cd build/latex
make
```

### Man Pages
```bash
sphinx-build -b man source build/man
```

### Plain Text
```bash
sphinx-build -b text source build/text
```

## Configuration

All Sphinx settings are in `source/conf.py`. Key options:

- **Theme:** `sphinx_rtd_theme` (Read the Docs theme)
- **Project:** Project Zomboid Scripts API Reference
- **Extensions:**
  - `sphinx.ext.autodoc` - Automatic documentation from docstrings
  - `sphinx.ext.viewcode` - Links to source code

## Contributing

When modifying documentation, ensure:

1. YAML block definitions are properly formatted
2. Parameter descriptions are clear and concise
3. The documentation builds without errors: `make clean && make html`
4. All warnings are resolved or documented

## Troubleshooting

### Sphinx not found
```bash
pip install sphinx sphinx-rtd-theme
```

### Build fails with import errors
```bash
pip install -r ../requirements.txt
```

### Old files in build
```bash
make clean
```

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/)
- [Project Zomboid Wiki - Scripts](https://pzwiki.net/wiki/Scripts)
