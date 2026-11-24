#!/usr/bin/env python3
"""Charm the Commuter: one-line forecast for a city that isn't.

Writes a single broadcast-style forecast line to /output/entry.txt.
The invented city is Drizzlewick: light rain, umbrellas up, and ducks
have taken over the bus lane -- a small joke for a bored commuter
standing at a rainy bus stop.
"""

import os

FORECAST = (
    "Good morning, Drizzlewick: light rain, 14 degrees, umbrellas up "
    "-- the ducks have taken over the bus lane again."
)


def validate(line: str) -> str:
    """Return the forecast line, or raise if it fails the 1-140 gate."""
    checked = line.strip()
    if not checked:
        raise ValueError("forecast must not be only whitespace")
    if not 1 <= len(checked) <= 140:
        raise ValueError(f"forecast is {len(checked)} chars, must be 1-140")
    return checked


def write_entry(line: str, path: str = "/output/entry.txt") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> None:
    write_entry(validate(FORECAST))


if __name__ == "__main__":
    main()
