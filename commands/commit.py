"""
gsc commit -m "message"
Create a commit snapshot by copying staged files to a new commits/commit_N folder.
Usage:
  gsc commit -m "your message"
"""

from logging import log
import os
import json
import shutil
from datetime import datetime

USAGE = __doc__

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def copy_item(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)

def run(args):
    # parse message
    if "-m" not in args:
        print("Usage: gsc commit -m \"message\"")
        return 2
    try:
        m_index = args.index("-m") + 1
        message = " ".join(args[m_index:])
    except Exception:
        print("Please provide a message: gsc commit -m \"message\"")
        return 2

    cwd = os.getcwd()
    gsc_dir = os.path.join(cwd, ".gsc")
    if not os.path.isdir(gsc_dir):
        print("No GSC repository here. Run `gsc init` first.")
        return 2

    index_path = os.path.join(gsc_dir, "index.json")
    log_path = os.path.join(gsc_dir, "log.json")
    commits_dir = os.path.join(gsc_dir, "commits")

    staged = load_json(index_path)
    if not staged:
        print("Nothing to commit. Staging area is empty.")
        return 0

    log = load_json(log_path)
    commit_id = len(log) + 1
    commit_folder = os.path.join(commits_dir, f"commit_{commit_id}")
    os.makedirs(commit_folder, exist_ok=True)

    copied = []
    for rel in staged:
        src = os.path.join(cwd, rel)
        if not os.path.exists(src):
            print("Warning: staged item no longer exists, skipping:", rel)
            continue
        dest = os.path.join(commit_folder, rel)
        try:
            copy_item(src, dest)
            copied.append(rel)
        except Exception as e:
            print("Error copying", rel, e)

    # entry = {
    #     "id": commit_id,
    #     "message": message,
    #     "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    #     "files": copied
    # }
    # log.append(entry)
    # save_json(log_path, log)

    # # clear index
    # save_json(index_path, [])

    # print(f"Committed as commit_{commit_id}: {message}")
    # return 0

    entry = {
        "id": commit_id,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "files": copied
    }
    log.append(entry)
    save_json(log_path, log)

    # clear index
    save_json(index_path, [])

    print(f"Committed as commit_{commit_id}: \"{message}\"")
    print(f"Files committed: {len(copied)}")
    if len(copied) < len(staged):
        print("Note: some staged files were missing and skipped during commit.")
    return 0
