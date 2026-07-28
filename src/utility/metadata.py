from typing import Any, Callable, TypedDict, NotRequired, TypeVar, Generic

from project import INDENT
from documentation import DocObject, DocObjectT

class Rule(TypedDict):
    """Type definition for a metadata rule."""
    # the key to access in the data dictionary
    access_key: NotRequired[str]
    
    # default fallback value. if not provided, then mandatory key
    default: NotRequired[str | None]

    # first arg needs to be Generic[DocObjectT]
    formatter: NotRequired[Callable[[Any, str, Any], str]]  # optional formatter function to format the value


class Metadata(Generic[DocObjectT]):
    def __init__(self, rule_set: dict[str, Rule]):
        self.rule_set = rule_set

    def generate(self, obj: DocObjectT, data: dict[str, Any]) -> str:
        """Generate metadata string based on the provided data and rule set."""
        out = ""
        i = 0
        for key, rule in self.rule_set.items():
            # check if exists in data
            access_key = rule.get("access_key", key)
            if access_key in data:
                value = data[access_key]
                # use formatter if provided in ruleset
                if "formatter" in rule:
                    value = rule["formatter"](obj, key, value)

            # use default if provided in ruleset
            elif "default" in rule:
                value = rule["default"]
                
                # skip if default is None, means we just hide it
                if value is None:
                    continue

            # unexpected behavior: key is mandatory
            else:
                raise ValueError(f"Missing required metadata key: {key}")
            
            out += self.format_metadata(key, value) + "\n"
            i += 1

        if i == 0:
            return ""

        return out.rstrip()  # remove trailing newline
    
    @staticmethod
    def format_metadata(key: str, value: str | None) -> str:
        """Helper method to format a single metadata key-value pair."""
        value = str(value)
        value = f"\n{INDENT}".join(value.split('\n'))
        return f".. attribute:: {key}\n\n{INDENT}{value}\n"
