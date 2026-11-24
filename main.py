"""Real-Life Patch Notes: The Comedy Changelog — round 3 entry.

Writes one line (a software patch note for a bug in real life / human
biology) to /output/entry.txt. Deterministic: the same line every run.
No network access, no environment secrets, no input files.
"""

from pathlib import Path

ENTRY = (
    "v3.0.9: fixed a bug where the stomach growled during a minute of "
    "silence; 40 mourners now believe the deceased had opinions, and the "
    "eulogy now includes them."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
