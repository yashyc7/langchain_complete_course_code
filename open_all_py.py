#!/usr/bin/env python3
"""
open_all_py.py

Default Behavior:
- Runs forever
- 10 second delay between openings
- Opens only NEW .py files
- Uses same VS Code window
- Stops with Ctrl+C
"""

import os
import sys
import argparse
import subprocess
import shutil
import time
from typing import List, Set

EXCLUDE_DIRS = {"venv", ".venv", "env", "ENV", ".git", "__pycache__", "node_modules"}


# ------------------------------------------------------------
# Find Python files
# ------------------------------------------------------------
def find_py_files(root: str) -> List[str]:
    root = os.path.abspath(root)
    py_files = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.abspath(os.path.join(dirpath, filename))

                # Skip this script itself
                try:
                    if os.path.samefile(full_path, __file__):
                        continue
                except Exception:
                    pass

                py_files.append(full_path)

    return sorted(py_files)


# ------------------------------------------------------------
# Find VS Code CLI
# ------------------------------------------------------------
def find_code_cli():
    for name in ("code", "code.cmd", "code.exe"):
        path = shutil.which(name)
        if path:
            return path
    return None


# ------------------------------------------------------------
# Main Opening Logic (Forever by default)
# ------------------------------------------------------------
def open_files(root: str, delay: float = 10.0) -> int:
    code_cli = find_code_cli()
    opened_files: Set[str] = set()

    try:
        while True:
            current_files = set(find_py_files(root))
            new_files = current_files - opened_files

            if not new_files:
                print("No new Python files found. Waiting...")
            else:
                for file_path in sorted(new_files):
                    if code_cli:
                        subprocess.run(
                            [code_cli, "--reuse-window", file_path],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                        print(f"Opened in VS Code: {file_path}")
                    else:
                        os.startfile(file_path)
                        print(f"Opened with default app: {file_path}")

                    opened_files.add(file_path)

                    time.sleep(delay)

                print(f"Cycle complete. Opened {len(new_files)} file(s).")

            # Wait before rescanning
            time.sleep(delay)

    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C).")

    return 0


# ------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Open all .py files in a folder forever with 10s gap by default."
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root folder to scan (default: current directory)"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=10.0,
        help="Seconds between file openings (default: 10)"
    )

    args = parser.parse_args()

    root_path = os.path.abspath(args.path)

    if not os.path.exists(root_path):
        print(f"Path not found: {root_path}")
        return 1

    return open_files(root=root_path, delay=args.delay)


if __name__ == "__main__":
    sys.exit(main())