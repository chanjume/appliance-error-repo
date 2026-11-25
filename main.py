#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line (67 characters, within the 1-200 gate) to /output/entry.txt:
a washing machine reporting, in its own flat voice, the most honest fault
it knows - the sock that never comes back - with a deadpan twist.
"""
import os

ENTRY = "Cycle complete. One sock is missing. It filed for divorce and left."


def main() -> None:
    # Gate check before writing: 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
