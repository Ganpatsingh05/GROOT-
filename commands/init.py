"""
gsc init
Creates .gsc/ directory and metadata files in the CURRENT working directory.
Usage:
  gsc init
"""

import os
import json

USAGE = __doc__

GSC_DIR = ".gsc"
INDEX_FILE = "index.json"
LOG_FILE = "log.json"
COMMITS_DIR = "commits"

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def run(args):
    cwd = os.getcwd()
    gsc_path = os.path.join(cwd, GSC_DIR)
    if os.path.exists(gsc_path):
        print("GSC repository already initialized in", cwd)
        return 0

    os.makedirs(os.path.join(gsc_path, COMMITS_DIR), exist_ok=True)
    write_json(os.path.join(gsc_path, INDEX_FILE), [])
    write_json(os.path.join(gsc_path, LOG_FILE), [])
    print("Initialized empty GSC repository in", gsc_path)
    return 0
