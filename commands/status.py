"""
groot status
Show staged files (the index).
Usage:
  groot status
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
    groot_dir = os.path.join(cwd, ".groot")
    if not os.path.isdir(groot_dir):
        print("No GROOT repository here. Run `groot init` first.")
        return 2
    
    index = load_json(os.path.join(groot_dir, "index.json"))
    log = load_json(os.path.join(groot_dir, "log.json"))
    
    # Header
    print("=" * 60)
    print("GROOT Repository Status")
    print("=" * 60)
    
    # Show last commit info if available
    if log:
        last_commit = log[-1]
        print(f"\nLast Commit:")
        print(f"  ID: commit_{last_commit['id']}")
        print(f"  Message: {last_commit['message']}")
        print(f"  Date: {last_commit['timestamp']}")
        print(f"  Files: {len(last_commit.get('files', []))}")
    else:
        print("\nNo commits yet")
    
    print("\n" + "-" * 60)
    
    # Show staged files
    if not index:
        print("\nStaged files: None")
        print("\n✓ Staging area is clean")
    else:
        print(f"\nStaged files ({len(index)}):")
        for f in index:
            full_path = os.path.join(cwd, f)
            if os.path.exists(full_path):
                if os.path.isdir(full_path):
                    print(f"  📁 {f}")
                else:
                    size = os.path.getsize(full_path)
                    size_str = f"{size} bytes" if size < 1024 else f"{size/1024:.1f} KB"
                    print(f"  📄 {f} ({size_str})")
            else:
                print(f"  ⚠️  {f} (missing)")
        
        print(f"\n✓ Ready to commit {len(index)} file(s)")
        print("  Run: groot commit -m \"your message\"")
    
    print("=" * 60)
    return 0
