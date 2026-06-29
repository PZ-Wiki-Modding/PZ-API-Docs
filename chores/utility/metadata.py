from typing import Any, Callable, TypedDict, NotRequired

from documentation import DocObject


class Rule(TypedDict):
    """Type definition for a metadata rule."""
    # the key to access in the data dictionary
    access_key: NotRequired[str]
    
    # default fallback value. if not provided, then mandatory key
    default: NotRequired[str]

    formatter: NotRequired[Callable[[str, dict, str, Any], str]]  # optional formatter function to format the value


class metadata:
    def __init__(self, rule_set: dict[str, Rule]):
        self.rule_set = rule_set

    def generate(self, object_type: str, object_data: dict[str, Any], data: dict[str, Any]) -> str:
        """Generate metadata string based on the provided data and rule set."""
        out = ""
        for key, rule in self.rule_set.items():
            # check if exists in data
            access_key = rule.get("access_key", key)
            if access_key in data:
                value = data[access_key]
                # use formatter if provided in ruleset
                if "formatter" in rule:
                    value = rule["formatter"](object_type, object_data, key, value)

            # use default if provided in ruleset
            elif "default" in rule:
                value = rule["default"]

            # unexpected behavior: key is mandatory
            else:
                raise ValueError(f"Missing required metadata key: {key}")
            
            out += self.format_metadata(key, value) + "\n"

        return out.strip()
    
    @staticmethod
    def format_metadata(key: str, value: str) -> str:
        """Helper method to format a single metadata key-value pair."""
        return f":{key}: {value}"
