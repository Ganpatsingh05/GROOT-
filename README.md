# GSC — Tiny Git-Style Control

GSC is a beginner-friendly educational version control system implemented in Python.
This repository demonstrates GSC and also shows how Git (Git Bash) was used to build and manage the project.

## Features
- `gsc init` — initialize a `.gsc/` in current directory
- `gsc add <path>` — stage a file or folder
- `gsc commit -m "message"` — commit staged files (snapshot)
- `gsc log` — show commit history
- `gsc status` — show staged files

## Project structure

gsc-project/
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
2. Create a launcher `gsc.bat` that runs main.py (example in project instructions).
3. Add the launcher folder to PATH so `gsc` can be run from anywhere.
4. Example:
```bash
cd C:\projects\somefolder
gsc init
echo hello > file.txt
gsc add file.txt
gsc commit -m "first commit"
gsc log
