from enum import StrEnum



def make_ref_label(text: str, label: str) -> str:
    """Make a reference label for a given label."""
    return f":ref:`{text} <{label}>`"



# RST headers
class Headers(StrEnum):
    SECTION = '='
    SUBSECTION = '-'
    SUBSUBSECTION = '^'
    PARAGRAPH = '"'
    
    def __new__(cls, value):
        return str.__new__(cls, value)

    def next(self):
        """Return the next header level."""
        if self == Headers.SECTION:
            return Headers.SUBSECTION
        elif self == Headers.SUBSECTION:
            return Headers.SUBSUBSECTION
        elif self == Headers.SUBSUBSECTION:
            return Headers.PARAGRAPH
        else:
            raise ValueError("No next header level for PARAGRAPHS.")
        
    def make(self, title: str, label: str | None = None) -> str:
        """Create a header string with the given title."""
        out = ""
        if label is not None:
            out += f".. _{label}:\n\n"
        out += f"{title}\n{self * len(title)}\n\n"
        return out




if __name__ == "__main__":
    # Example usage
    current_header = Headers.SECTION
    print(f"Current header: {current_header}")
    next_header = current_header.next()
    print(f"Next header: {next_header}")