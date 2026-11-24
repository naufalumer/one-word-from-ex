"""One Word From Your Ex.

The entry is a single word: the word an ex would use to describe you.
This program puts that word, and nothing else, into
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output), then prints it.
"""

import os

WORD = "almost"

# The sealed gate takes 1 to 24 characters. A word with a space in it is
# two words, so refuse anything but one bare token, and refuse blank input.
if not 1 <= len(WORD) <= 24 or not WORD.strip() or any(ch.isspace() for ch in WORD):
    raise ValueError("entry must be exactly one word of 1-24 characters")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    # Read the file back and refuse to report success unless the bytes on
    # disk are exactly the word: a partial write must fail loudly here,
    # not ship a truncated entry to the sealed scorer.
    with open(entry_path, encoding="utf-8", newline="") as handle:
        if handle.read() != WORD:
            raise ValueError("entry.txt on disk does not match the word")
    print(WORD)


if __name__ == "__main__":
    main()
