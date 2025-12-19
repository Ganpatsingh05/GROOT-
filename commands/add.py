"""
groot add <path>
Adds a file or folder path to the staging area (index.json).
Usage:
  groot add filename.txt
  groot add folder_name/
"""

import os
import json

USAGE = __doc__

def load_index(index_path):
    if not os.path.exists(index_path):
        return []
    with open(index_path, "r", encoding="utf-8-sig") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_index(index_path, data):
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def run(args):
    if not args:
        print("Usage: groot add <path>")
        return 2
    target = args[0]
    cwd = os.getcwd()
    groot_dir = os.path.join(cwd, ".groot")
    index_path = os.path.join(groot_dir, "index.json")
    if not os.path.isdir(groot_dir):
        print("No GROOT repository here. Run `groot init` first.")
        return 2

    full_target = os.path.join(cwd, target)
    if not os.path.exists(full_target):
        print("Error: path does not exist:", target)
        return 1

    index = load_index(index_path)
    # store relative path (as user typed)
    # rel = os.path.relpath(full_target, cwd)
    rel = os.path.normpath(os.path.relpath(full_target, cwd))
    if rel in index:
        print("Already staged:", rel)
        return 0
    index.append(rel)
    save_index(index_path, index)
    print("Staged:", rel)
    return 0
