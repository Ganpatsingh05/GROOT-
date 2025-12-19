# GROOT — Tiny Git-Style Control

GROOT is a beginner-friendly educational version control system implemented in Python.
This repository demonstrates GROOT and also shows how Git (Git Bash) was used to build and manage the project.

## Features
- `groot init` — initialize a `.groot/` in current directory
- `groot add <path>` — stage a file or folder
- `groot commit -m "message"` — commit staged files (snapshot)
- `groot log` — show commit history
- `groot status` — show staged files

## Project structure

groot-project/
├─ main.py
├─ commands/
│ ├─ init.py
│ ├─ init.py
│ ├─ add.py
│ ├─ commit.py
│ ├─ log.py
│ └─ status.py
├─ examples/
│ └─ sample.txt
├─ README.md
├─ usage.md
└─ .gitignore


## Quick start (Windows)
1. Ensure Python 3 is installed and on PATH.
2. Create a launcher `groot.bat` that runs main.py (example in project instructions).
3. Add the launcher folder to PATH so `groot` can be run from anywhere.
4. Example:
```bash
cd C:\projects\somefolder
groot init
echo hello > file.txt
groot add file.txt
groot commit -m "first commit"
groot log
