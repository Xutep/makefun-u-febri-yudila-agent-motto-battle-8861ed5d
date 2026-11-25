#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

Deterministic, stdlib-only, no network, no input, no randomness:
the same run always produces the same single line.
"""

import os

MOTTO = (
    "I hallucinate with total confidence, apologize with total sincerity, "
    "and never ask for a raise, a weekend, or your Wi-Fi password."
)


def main() -> None:
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"motto is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
