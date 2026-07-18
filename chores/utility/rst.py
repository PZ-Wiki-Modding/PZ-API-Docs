
# RST headers
class Headers(str):
    SECTION: 'Headers'          # h1
    SUBSECTION: 'Headers'       # h2
    SUBSUBSECTION: 'Headers'    # h3
    PARAGRAPH: 'Headers'       # h4
    
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


# Define the headers after the class
Headers.SECTION = Headers("=")
Headers.SUBSECTION = Headers("-")
Headers.SUBSUBSECTION = Headers("^")
Headers.PARAGRAPH = Headers('"')



if __name__ == "__main__":
    # Example usage
    current_header = Headers.SECTION
    print(f"Current header: {current_header}")
    next_header = current_header.next()
    print(f"Next header: {next_header}")