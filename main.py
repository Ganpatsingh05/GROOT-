#!/usr/bin/env python3
"""
GROOT - Main dispatcher
Usage: groot <command> [args...]
This script delegates each command to a separate module in the `commands/` folder.
"""

import sys
import os

# commands folder name
COMMANDS_PKG = "commands"

def available_commands():
    commands_dir = os.path.join(os.path.dirname(__file__), COMMANDS_PKG)
    if not os.path.isdir(commands_dir):
        return []
    names = []
    for fname in os.listdir(commands_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            names.append(fname[:-3])
    return sorted(names)

def print_help():
    print("GROOT - Git-Inspired Repository & Object Organizer Tool")
    print("Usage: groot <command> [options]")
    print("Available commands:")
    for c in available_commands():
        print("  -", c)
    print("\nRun `groot help <command>` for command details.")

def run_command(cmd_name, args):
    try:
        module_name = f"{COMMANDS_PKG}.{cmd_name}"
        module = __import__(module_name, fromlist=["*"])
    except ImportError:
        print(f"Unknown command: {cmd_name}")
        print_help()
        return 2
    if hasattr(module, "run"):
        try:
            return module.run(args)
        except Exception as e:
            print("Error while running command:", e)
            return 1
    else:
        print(f"Command module '{cmd_name}' has no run(args) function.")
        return 1

def main():
    if len(sys.argv) <= 1:
        # Simple message when just 'groot' is typed
        print("GROOT - Git-Inspired Repository & Object Organizer Tool")
        print("\nUsage: groot <command> [options]")
        print("\nType 'groot help' to see all available commands.")
        return 0

    cmd = sys.argv[1].lower()
    args = sys.argv[2:]

    return run_command(cmd, args)


if __name__ == "__main__":
    sys.exit(main())
