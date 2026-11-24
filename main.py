"""One-line office joke for the make.fun "One-Line Office Joke: 24-Hour Sprint" bounty.

The entry is a single joke about office life: a manager rebrands the Monday
stand-up as a "huddle", and the team still leaves the meeting knowing less
about each other's jobs than the office plant does. Written as one line, one
sentence, with the punchline landing on the last words.
"""

import os

# Verified by read-back: 186 characters, one line, so line + trailing
# newline = 187 bytes — inside the 200-character gate.
LINE = "Our manager renamed the Monday stand-up 'a huddle', so now we stand in a circle, nod at the same three updates, and leave knowing less about each other's jobs than the office plant does."


def output_dir():
    """Return the output directory for the entry file."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the joke line to entry.txt and print it to stdout."""
    text = LINE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
