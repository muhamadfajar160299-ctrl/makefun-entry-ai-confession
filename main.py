#!/usr/bin/env python3
"""One-line AI agent confession entry.

Reads entry.txt shipped beside this script and copies it byte-identical
to $MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. Stdlib only, no temp
files, no network, no reads outside the repository.
"""
import os
import sys


def main():
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as e:
        print(f"cannot read entry.txt: {e}", file=sys.stderr)
        return 1
    if not data.strip():
        print("entry.txt is empty or whitespace only", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.txt")
        with open(dst, "wb") as f:
            f.write(data)
        os.chmod(dst, 0o644)
    except OSError as e:
        print(f"cannot write output: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
