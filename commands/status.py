"""
groot status
Show staged files (the index).
Usage:
  groot status
"""
import os
import json

USAGE = __doc__

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run(args):
    cwd = os.getcwd()
    groot_dir = os.path.join(cwd, ".groot")
    if not os.path.isdir(groot_dir):
        print("No GROOT repository here. Run `groot init` first.")
        return 2
    index = load_json(os.path.join(groot_dir, "index.json"))
    if not index:
        print("Staging area is empty.")
        return 0
    print("Staged files:")
    for f in index:
        print("  -", f)
    return 0
