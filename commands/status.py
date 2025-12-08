"""
gsc status
Show staged files (the index).
Usage:
  gsc status
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
    gsc_dir = os.path.join(cwd, ".gsc")
    if not os.path.isdir(gsc_dir):
        print("No GSC repository here. Run `gsc init` first.")
        return 2
    index = load_json(os.path.join(gsc_dir, "index.json"))
    if not index:
        print("Staging area is empty.")
        return 0
    print("Staged files:")
    for f in index:
        print("  -", f)
    return 0
