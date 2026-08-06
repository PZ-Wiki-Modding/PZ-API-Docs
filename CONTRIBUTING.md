# Contributing
You are free to contribute to this project by submitting pull requests or reporting issues.

## Structure
The project is structured the following way:
```bash
.github/                      # GitHub related files
└── workflows/
    └── deploy-docs.yml         # build and deploy the docs to the GitHub Pages
docs/                        # the Sphinx documentation source files
└── source/
    └── *.rst                    # the documentation files
    └── conf.py                  # the Sphinx configuration file
```

## Build
First setup the Python environment (`.venv`):
```bash
make setup
```

Then you can build to html:
```bash
make html
```
Or directly build then serve to a local host (http://localhost:8000):
```bash
make serve
```

Output html goes in `docs/build/html`.

## Contact
You can find the creator of this dataset (SimKDT) in the [PZ Modding Community](https://pzwiki.net/wiki/PZ_Modding_Community).