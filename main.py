#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one alien tourist's review of planet Earth to /output/entry.txt.
Deterministic: every run writes the exact same bytes.
"""
import os

REVIEW = (
    "Four stars. The locals pay to watch other locals pretend to be other "
    "locals, then argue online about whether the pretending was believable. "
    "The snacks, however, were flawless."
)


def main():
    # The gate reads /output/entry.txt: 1-200 UTF-8 chars, not only whitespace.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
