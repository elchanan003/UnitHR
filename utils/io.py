import json
from pathlib import Path


base = Path(__file__).resolve().parent.parent
json_path = base / 'soldiers.json'


def get_all_soldiers(json_path):
    with open(json_path, 'r', encoding='utf8') as f:
        soldiers = json.load(f)

        return soldiers

def save_soldiers(data, json_path):
    with open(json_path, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4)

