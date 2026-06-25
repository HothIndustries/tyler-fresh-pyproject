"""Minimal package for tyler-fresh-pyproject."""

from __future__ import annotations

import sys
from urllib.request import urlopen


def make_request(url: str, timeout: float = 10.0) -> str:
    with urlopen(url, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Hello from tyler-fresh-pyproject!")
        return

    print(make_request(args[0]))
