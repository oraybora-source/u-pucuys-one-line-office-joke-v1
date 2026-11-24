#!/usr/bin/env python3
"""One-Line Office Joke (make.fun) — V1 entrypoint.

Writes one joke about office life — a single line — to
/output/entry.txt. The line is the whole entry: no code, no
explanation, nothing else.

Deterministic: the same bytes on every run (fixed string, no random,
no time, no network). Python 3 standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

ENTRY = "My Jira ticket has been \"In Progress\" for eleven months, which in office time is basically a pet — I feed it status updates every Friday."
MAX_CHARS = 200


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The output must be readable by every user: folder 0755, file 0644.
    os.chmod(out_dir, 0o755)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The output must be readable by every user: file 0644, folder 0755.
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
