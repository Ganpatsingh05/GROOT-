### 1.10 `usage.md` (detailed usage & examples)
```markdown
# GSC Usage

## Install / make global (Windows example)
1. Create `gsc.bat` pointing to `main.py`:
@echo off
py -3 "C:\path\to\gsc-project\main.py" %*

pgsql
Copy code
2. Put `gsc.bat` in `C:\gsc-cli\` and add that folder to PATH.

## Commands
- `gsc init`  
Initialize a `.gsc` folder in the current directory.

- `gsc add <path>`  
Stage a file or folder (relative path stored).

- `gsc commit -m "message"`  
Commit the current staging area to `.gsc/commits/commit_N/`.

- `gsc status`  
Show staged files.

- `gsc log`  
Show commit history.

## Example session
```bash
mkdir demo
cd demo
gsc init
echo hello > notes.txt
gsc add notes.txt
gsc status
gsc commit -m "Add notes"
gsc log