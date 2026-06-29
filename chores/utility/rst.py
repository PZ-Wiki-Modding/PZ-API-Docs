
# RST headers
class headers(str):
    SECTION: 'headers'          # h1
    SUBSECTION: 'headers'       # h2
    SUBSUBSECTION: 'headers'    # h3
    PARAGRAPH: 'headers'       # h4
    
    def __new__(cls, value):
        return str.__new__(cls, value)

    def next(self):
        """Return the next header level."""
        if self == headers.SECTION:
            return headers.SUBSECTION
        elif self == headers.SUBSECTION:
            return headers.SUBSUBSECTION
        elif self == headers.SUBSUBSECTION:
            return headers.PARAGRAPH
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
headers.SECTION = headers("=")
headers.SUBSECTION = headers("-")
headers.SUBSUBSECTION = headers("^")
headers.PARAGRAPH = headers('"')



if __name__ == "__main__":
    # Example usage
    current_header = headers.SECTION
    print(f"Current header: {current_header}")
    next_header = current_header.next()
    print(f"Next header: {next_header}")