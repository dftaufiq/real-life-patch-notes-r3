"""Real-Life Patch Notes: The Comedy Changelog — round 3 entry.

Writes one line (a software patch note for a bug in real life / human
biology) to /output/entry.txt. Deterministic: the same line every run.
No network access, no environment secrets, no input files.

The line is built as a two-beat joke with a reveal: beat 1 is the
embarrassing bug itself (a stomach growling at a funeral), beat 2 is
the fallout (the mourners misreading it as an opinion), and the reveal
is the eulogy — the highest honour a funeral can give — being rewritten
to include an opinion the deceased never held. The specific count
("40 mourners") makes the absurdity concrete instead of abstract.
"""

from pathlib import Path

# The line is assembled from its three beats so each beat is legible
# in the source; joining them yields the exact 158-char entry line.
_BEAT_1 = "v3.0.9: fixed a bug where the stomach growled during a minute of silence"
_BEAT_2 = "; 40 mourners now believe the deceased had opinions"
_REVEAL = ", and the eulogy now includes them."

ENTRY = _BEAT_1 + _BEAT_2 + _REVEAL


def main() -> None:
    # Write exactly ENTRY, nothing else — no trailing newline, so the
    # output file is the line verbatim and hashes identically every run.
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
