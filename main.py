#!/usr/bin/env python3
"""Write one funny developer excuse for a production outage to /output/entry.txt.

Deterministic: no input, no network, no randomness. The program writes a
single fixed line (under 200 characters) and prints it to stdout.
"""

from pathlib import Path

ENTRY = (
    "Production broke because I approved my own pull request at 2 a.m. "
    "\u2014 the only reviewer awake was me, and I was asleep."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer does: one line of
    # 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
