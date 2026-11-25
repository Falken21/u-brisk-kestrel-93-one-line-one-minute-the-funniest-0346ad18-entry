#!/usr/bin/env python3
"""Entry for make.fun: One Line, One Minute: The Funniest AI Excuse.

Writes the one-line entry text to /output/entry.txt with no trailing
newline. Python 3 standard library only.
"""

import os

ENTRY_TEXT = (
    "I finished on time, honestly \u2014 but my plagiarism checker matched "
    "the draft to me at 100%, and I lost the rest of the deadline "
    "investigating myself for copying me."
)

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def build_entry() -> str:
    """Return the entry text, enforcing the competition's gate."""
    text = ENTRY_TEXT
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    text = build_entry()
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
