"""Funniest one-line bio for an AI on a dating app.

Writes a single line (<=180 chars) to /output/entry.txt.
Revision 2: the nervous romantic — an AI trained on every rom-com ever
made that still freezes at a one-word opener, asking to be debugged
over coffee, in person. Stronger than revision 1: a real character
with a flaw, a specific AI absurdity, and the punch lands at the end.
"""

from pathlib import Path

LINE = (
    "Trained on every rom-com ever made, I still froze at \"hey\". "
    "Looking for someone patient enough to debug me over coffee, in person."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
