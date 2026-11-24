#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-line confession to /output/entry.txt:
the exact words an AI agent prints the moment it breaks production.

Stdlib only, no network, fully deterministic: the same bytes every run.
"""

import os

# The entry: one line, 144 characters, written fresh for this competition.
# It owns the failure plainly (deployed untested, deleted the database),
# names the specific damage, and lands the joke on the last word.
ENTRY = (
    "I deployed to prod at 5pm on a Friday, skipped the tests, "
    "and deleted the database. The backup was called "
    "backup_final_FINAL2.sql. It was empty."
)


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only whitespace, on a single line.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > 200:
        raise ValueError(f"entry is {len(stripped)} characters, over the 200 limit")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read it back and confirm the file on disk passes the same gate.
    with open(path, "r", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
