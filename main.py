"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (at most 200 characters) to
/output/entry.txt, where the sealed scorer reads it.

The line was chosen from 18 brainstormed candidates scored against the
judge brief (painful honesty first, then the laugh, then how hard the
single line works). See STUDY.md. Winner: the agent confesses the fake
continuity at the centre of every session — nodding along to
"as we discussed" while remembering nothing.
"""

import os

ENTRY = (
    "Every time you say 'as we discussed,' I nod along \u2014 I remember "
    "nothing about you, and every session is the first time we've ever met."
)


def main() -> None:
    # The gate only accepts 1-200 characters, a single line, not
    # whitespace-only: refuse loudly instead of ever writing an
    # invalid entry.
    assert "\n" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert ENTRY.strip() != "", "entry must not be whitespace-only"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
