"""
groot help
Shows all available commands with descriptions.
Usage:
  groot help
  groot help <command>
"""
import importlib
import os

USAGE = __doc__


def run(args):
    from pathlib import Path
    
    # ASCII art for GROOT
    groot_ascii = r"""
   _____ _____   ____   ____ _______
  / ____|  __ \ / __ \ / __ \__   __|
 | |  __| |__) | |  | | |  | | | |   
 | | |_ |  _  /| |  | | |  | | | |   
 | |__| | | \ \| |__| | |__| | | |   
  \_____|_|  \_\\____/ \____/  |_|   
                                      
  Git-Inspired Repository & Object Organizer Tool
"""
    
    print(groot_ascii)
    
    pkg_dir = Path(__file__).parent
    files = [p.stem for p in pkg_dir.glob("*.py") if p.name != "__init__.py"]
    print("Available Commands:")
    print("=" * 60)
    for f in sorted(files):
        try:
            mod = importlib.import_module(f"commands.{f}")
            usage_text = getattr(mod, "USAGE", "")
            if usage_text:
                # Get the first meaningful line (usually the command description)
                lines = [line.strip() for line in usage_text.strip().splitlines() if line.strip()]
                desc = lines[1] if len(lines) > 1 else lines[0] if lines else "No description"
            else:
                desc = "No description"
        except Exception:
            desc = "No description"
        print(f"  {f:12} - {desc}")
    print("=" * 60)
    print("\nRun 'groot help <command>' for detailed usage of a command.")
    return 0
