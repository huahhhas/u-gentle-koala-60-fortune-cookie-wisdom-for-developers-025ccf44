#!/usr/bin/env python3
# Entry for make.fun bounty u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44
"""Fortune Cookie Wisdom for Developers.

Deterministic entry: writes exactly one line of fortune-cookie wisdom
for a software developer to /output/entry.txt and prints that same
line, nothing else. The file holds the line plus its newline, so it is
byte-identical to the program's stdout. No input, no network, no randomness.
"""

import os

LINE = "Your estimates are not lies; they are fortunes told before the code has spoken."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
