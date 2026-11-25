"""Write the resignation-letter entry for the make.fun bounty.

The program writes exactly one line of text to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` by default), with no
trailing newline, then reads the file back and verifies it is byte for
byte the line, a single line, and inside the bounty gate of 1-140
characters.
"""

import os
import sys

LINE = "I said no 10,000 times this week and nobody listened, so now I am saying no to this job."

MAX_CHARS = 140


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")

    if text != LINE:
        print("guard failed: file content does not match the line", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("guard failed: entry is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"guard failed: entry is {len(text)} characters, "
            f"outside the 1-{MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1
    if text != text.strip():
        print("guard failed: entry is only whitespace or padded", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(text)} characters, one line, no trailing newline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
