#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun bounty entry.

Writes exactly one line of fortune-cookie wisdom for developers to
/output/entry.txt (no trailing newline).
"""

import hashlib
import os
import sys

LINE = "Your next deploy will pass on the first try \u2014 because this time you actually read the error message."
# Why this line fits the brief: it is a fortune-cookie prediction ("Your next
# deploy will pass on the first try") tied to a concrete developer habit
# (actually reading the error message) — the classic cookie-voice twist where
# the luck turns on something the reader did, not on fate alone.


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the gate: UTF-8, 1-120 chars, not only whitespace,
    # and exactly the intended line.
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 120, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match the intended line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert raw == data, "file bytes differ from the intended encoding"
    print("sha256:", hashlib.sha256(raw).hexdigest())
    print("chars:", len(text), "bytes:", len(raw))


if __name__ == "__main__":
    main()
