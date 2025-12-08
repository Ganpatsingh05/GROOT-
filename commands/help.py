"""
help command for GSC
Usage:
  gsc help            -> show all commands
  gsc help <command>  -> show usage for a specific command
"""
import importlib
import os

def run(args):
    if not args:
        # list commands and short descriptions
        from pathlib import Path
        pkg_dir = Path(__file__).parent
        files = [p.stem for p in pkg_dir.glob("*.py") if p.name != "__init__.py"]
        print("GSC help: available commands\n")
        for f in sorted(files):
            print("-", f)
        print("\nRun `gsc help <command>` to see detailed usage for a command.")
        return 0

    cmd = args[0]
    try:
        mod = importlib.import_module(f"commands.{cmd}")
    except Exception:
        print("No help available for unknown command:", cmd)
        return 2

    if hasattr(mod, "USAGE"):
        print(mod.USAGE)
    else:
        print("No usage string defined for command:", cmd)
    return 0

