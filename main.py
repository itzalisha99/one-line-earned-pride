#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes one line of quiet, earned pride to /output/entry.txt.
Standard library only; deterministic: every run writes the same line.
"""

import os

LINE = (
    "For three years she practised the same piano piece every morning "
    "before work, and today her daughter heard it from the kitchen and "
    "stopped washing the dishes to listen."
)


def validate(text: str) -> None:
    """Mirror the bounty gate before writing: 1-240 chars, UTF-8,
    not only whitespace, and a single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
