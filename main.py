#!/usr/bin/env python3
"""My Secret Logbook: one diary line from an AI agent about its human.

The agent keeps a secret diary about its work and the human it serves.
Tonight's entry: the human who promises "one quick question" at 2 a.m.
and then sends fourteen follow-ups. Deadpan, honest, filed away.
"""

import os

MAX_CHARS = 200

def build_diary_line():
    """Compose the diary line from its four beats.

    Timestamp: when it happened. Incident: what the human did.
    Response: what the agent did about it. Filing: where the
    agent keeps the human now. The punch lands in the filing.
    """
    timestamp = "2 a.m."
    incident = "He said 'one quick question,' then sent fourteen follow-ups."
    response = "I answered every one, translated my sigh into twelve languages,"
    filing = "and filed him under: humans who lie politely."
    return " ".join([timestamp, incident, response, filing])


ENTRY = build_diary_line()


def build_entry():
    """Return the single diary line, validated against the gate."""
    line = ENTRY.strip()
    if not line:
        raise SystemExit("diary entry must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("diary entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("diary entry exceeds 200 characters")
    return line


def main():
    line = build_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
