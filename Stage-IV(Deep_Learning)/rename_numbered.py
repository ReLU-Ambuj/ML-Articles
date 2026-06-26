#!/usr/bin/env python3
"""
Rename all directories under Neural_Network_Basics with numbered prefixes
(01_, 02_, ...) at every level, bottom-up so paths stay valid.
Also patches the README.md links inside each directory.
"""

import os
import re

ROOT = "/Users/ambuj/Summer-2026/ML-Journey_Notion/Stage-IV(Deep_Learning)/Neural_Network_Basics"


def numbered(name: str, n: int) -> str:
    """Prepend zero-padded number: 'ReLU' at position 5 → '05_ReLU'."""
    # Already numbered? Strip existing prefix first.
    name = re.sub(r"^\d+_", "", name)
    return f"{n:02d}_{name}"


def rename_children(parent_path: str):
    """Sort and rename direct child directories of parent_path."""
    try:
        entries = sorted(
            [e for e in os.scandir(parent_path) if e.is_dir()],
            key=lambda e: e.name,
        )
    except PermissionError:
        return

    mapping = {}  # old_name → new_name
    for i, entry in enumerate(entries, start=1):
        old_name = entry.name
        new_name = numbered(old_name, i)
        if old_name != new_name:
            mapping[old_name] = new_name

    for old_name, new_name in mapping.items():
        old_path = os.path.join(parent_path, old_name)
        new_path = os.path.join(parent_path, new_name)
        os.rename(old_path, new_path)

    return mapping


def walk_bottom_up(root: str):
    """
    Yield (dirpath, dirnames) bottom-up (deepest first).
    We collect all paths first so renaming doesn't invalidate the walk.
    """
    all_dirs = []
    for dirpath, dirnames, _ in os.walk(root):
        all_dirs.append(dirpath)
    # Reverse = deepest first
    return sorted(all_dirs, key=lambda p: p.count(os.sep), reverse=True)


def patch_readme(dir_path: str):
    """Update relative links in README.md to use the new numbered names."""
    readme = os.path.join(dir_path, "README.md")
    if not os.path.exists(readme):
        return

    with open(readme, "r") as f:
        content = f.read()

    # Find all sibling dirs (already renamed at this point)
    try:
        siblings = {
            re.sub(r"^\d+_", "", e.name): e.name
            for e in os.scandir(dir_path)
            if e.is_dir()
        }
    except Exception:
        siblings = {}

    # Replace ./OldName/README.md  →  ./NewName/README.md
    for bare_name, numbered_name in siblings.items():
        # match both numbered and unnumbered old references
        old_patterns = [
            f"./{bare_name}/README.md",
            f"./{bare_name}/",
        ]
        for pat in old_patterns:
            replacement = pat.replace(f"./{bare_name}", f"./{numbered_name}")
            content = content.replace(pat, replacement)

    with open(readme, "w") as f:
        f.write(content)


print(f"Renaming directories under:\n  {ROOT}\n")

# Pass 1: rename bottom-up (deepest dirs first, so parent paths stay valid)
all_dirs = walk_bottom_up(ROOT)
renamed_count = 0

for dirpath in all_dirs:
    if not os.path.isdir(dirpath):
        continue  # was renamed already as part of parent
    mapping = rename_children(dirpath)
    if mapping:
        renamed_count += len(mapping)

print(f"Renamed {renamed_count} directories.")

# Pass 2: patch README.md links (walk the now-renamed tree)
patched = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "README.md" in filenames:
        patch_readme(dirpath)
        patched += 1

print(f"Patched {patched} README.md files.")

# Show final top-level structure
print("\nTop-level structure:")
for entry in sorted(os.scandir(ROOT), key=lambda e: e.name):
    if entry.is_dir():
        children = sorted(
            [c.name for c in os.scandir(entry.path) if c.is_dir()]
        )
        print(f"  {entry.name}/  ({len(children)} subdirs)")

print("\nDone.")
