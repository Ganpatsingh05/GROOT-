"""
groot init
Creates .groot/ directory and metadata files in the CURRENT working directory.
Usage:
  groot init
"""

import os
import json

USAGE = __doc__

GROOT_DIR = ".groot"
INDEX_FILE = "index.json"
LOG_FILE = "log.json"
COMMITS_DIR = "commits"

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def run(args):
    cwd = os.getcwd()
    groot_path = os.path.join(cwd, GROOT_DIR)
    if os.path.exists(groot_path):
        print("GROOT repository already initialized in", cwd)
        return 0

    try:
        os.makedirs(os.path.join(groot_path, COMMITS_DIR), exist_ok=True)
        write_json(os.path.join(groot_path, INDEX_FILE), [])
        write_json(os.path.join(groot_path, LOG_FILE), [])
    except PermissionError:
        print("Error: cannot create .groot in this folder (permission denied). Try running the command in a writable directory.")
        return 1

    print("Initialized empty GROOT repository at:", groot_path)
    print("You can now run: groot add <file>  and  groot commit -m \"message\"")")
    return 0
