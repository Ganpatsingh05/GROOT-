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
        print(f"Error: path does not exist: {target}")
        print(f"Current directory: {cwd}")
        return 1

    index = load_index(index_path)
    # store relative path (as user typed)
    # rel = os.path.relpath(full_target, cwd)
    rel = os.path.normpath(os.path.relpath(full_target, cwd))
    
    # Prevent staging current directory "."
    if rel == "." or os.path.samefile(full_target, cwd):
        print("Error: Cannot stage the current directory '.'")
        print("Tip: To stage all files, use: groot add <filename> for each file")
        return 1
    
    # Prevent staging .groot directory
    if ".groot" in rel.split(os.sep):
        print("Error: Cannot stage .groot directory or its contents")
        return 1
    
    # Check if it's a file or directory
    is_dir = os.path.isdir(full_target)
    file_type = "directory" if is_dir else "file"
    
    if rel in index:
        print(f"✓ Already staged: {rel} ({file_type})")
        return 0
    
    index.append(rel)
    save_index(index_path, index)
    
    # Enhanced output
    print(f"✓ Staged {file_type}: {rel}")
    if not is_dir:
        size = os.path.getsize(full_target)
        size_str = f"{size} bytes" if size < 1024 else f"{size/1024:.1f} KB"
        print(f"  Size: {size_str}")
    print(f"  Total files staged: {len(index)}")
    return 0
