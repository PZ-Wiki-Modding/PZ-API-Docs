"""
Merge different .vscode/settings.json files into a single workspace settings.json file.
"""

import json

from project import PROJECT_ROOT

EXTERNAL_PATH = PROJECT_ROOT / "external"
OUT_PATH = PROJECT_ROOT / "out" / "settings.json"

configs = [
    EXTERNAL_PATH / "pz-xml-data" / "out" / "settings.json",
    EXTERNAL_PATH / "pz-translation-data" / "out" / "settings.json"
]


configs_data = []
for config in configs:
    with open(config, "r") as f:
        configs_data.append(json.load(f))

merged_config = {}
for config_data in configs_data:
    merged_config.update(config_data)

from pprint import pprint
pprint(merged_config)

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_PATH, "w") as f:
    json.dump(merged_config, f, indent=4)