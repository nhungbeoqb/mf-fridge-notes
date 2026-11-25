#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to $OUTPUT_DIR/entry.txt (default /output).

The note: the fridge has updated its LinkedIn and is Open to Work —
anywhere the door actually closes. Three beats: the job-seeker
update, the Open to Work flag, the sting (the door never closes
here). Fridge voice via the door sensor; the grudge is small and
domestic; nothing is explained.
"""

import os
import sys

NOTE = "I updated my LinkedIn. Open to work: any kitchen where the door actually closes."


def gate_ok(text):
    """Mirror the sealed scorer's gate: UTF-8 text, 1-200 chars, not only whitespace.

    Plus the brief's own rule, which the scorer does not check: the note
    must be a single line, so any newline or carriage return fails here.
    """
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")  # raises if not encodable
    return True


def main():
    if not gate_ok(NOTE):
        print("gate check failed: note is %d chars" % len(NOTE), file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
