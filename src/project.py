import m2r
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
INDENT = " " * 3
DOC_LINK = r"https://pz-wiki-modding.github.io/PZ-API-Docs" # i hate it


def sanitize_description(description: str) -> str:
    """Sanitize the provided description by converting Markdown to reStructuredText."""
    return m2r.convert(description).strip()


if __name__ == "__main__":
    print(f"Repository root path: {PROJECT_ROOT}")