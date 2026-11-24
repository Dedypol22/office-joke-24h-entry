"""One-line office joke entry for the make.fun bounty
"One-Line Office Joke: 24-Hour Sprint".

The joke: a boss who brags that his door is always open, while the door
is guarded by three escalating barriers — a keypad, a booking form and a
three-day waiting list. The setup promises access; the punchline, landing
on the last words, takes it all away.
"""

import os

JOKE = (
    "My boss says his door is always open, but there's a keypad on it, "
    "a booking form, and a three-day waiting list."
)


def output_dir():
    """Return the directory entry.txt should be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the joke to entry.txt and print it to stdout."""
    text = JOKE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
