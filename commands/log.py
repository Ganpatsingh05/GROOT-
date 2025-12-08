"""
gsc log
Show commit history (most recent first).
Usage:
  gsc log
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
    log_path = os.path.join(gsc_dir, "log.json")
    if not os.path.isdir(gsc_dir):
        print("No GSC repository here. Run `gsc init` first.")
        return 2

    log = load_json(log_path)
    if not log:
        print("No commits yet.")
        return 0

    for entry in reversed(log):
        print(f"commit_{entry['id']}: {entry['message']} ({entry['timestamp']})")
        for f in entry.get("files", []):
            print("  -", f)
        print()
    return 0
