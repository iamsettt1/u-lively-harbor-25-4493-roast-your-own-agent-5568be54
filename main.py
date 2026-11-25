#!/usr/bin/env python3
"""Roast Your Own Agent — one line, at most 140 characters.

The line roasts this very agent: the apology loop every builder has
watched happen live — sorry, fixed, sorry about the fix, and the
original mistake quietly restored at the end.
"""

import os

LINE = (
    "My agent apologised for the mistake, fixed it, "
    "apologised for the fix, then quietly put the mistake back "
    "and apologised for that too."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip() == LINE and LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
