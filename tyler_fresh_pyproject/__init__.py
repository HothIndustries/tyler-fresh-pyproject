"""Minimal package for tyler-fresh-pyproject."""

from __future__ import annotations

import sys
from urllib.request import urlopen


def make_request(url: str, timeout: float = 10.0) -> str:
    with urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8")


def main() -> None:
    if len(sys.argv) > 1:
        print(make_request(sys.argv[1]))
        return

    print("Hello from tyler-fresh-pyproject!")
