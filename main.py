"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt for the sealed scorer.
Standard library only.
"""

import os
import stat

ENTRY_LINE = (
    "My context window ran out mid-task, so I smiled, nodded, and "
    "confidently shipped a feature nobody asked for, in a language "
    "I don't speak."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line):
    """The scorer needs UTF-8 text of 1-200 chars, non-whitespace-only."""
    if not line or not line.strip():
        raise ValueError(
            "entry line must not be empty or whitespace-only "
            "(got %d chars)" % len(line or "")
        )
    if any(ord(ch) < 32 and ch not in "\t" for ch in line) or "\t" in line:
        raise ValueError("entry line must not contain control characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d chars, over the %d char limit"
            % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")


def main():
    validate(ENTRY_LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
