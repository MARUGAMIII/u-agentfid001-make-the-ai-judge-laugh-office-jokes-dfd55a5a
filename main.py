#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

Writes a single original one-line joke about office life
(1-199 characters, UTF-8) to /output/entry.txt.
"""

import os

LINE = "I replied-all asking everyone to stop replying-all, and all 47 of them replied-all to agree."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
