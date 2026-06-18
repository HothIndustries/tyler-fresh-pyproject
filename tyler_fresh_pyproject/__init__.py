"""Minimal package for tyler-fresh-pyproject."""

from __future__ import annotations

import sys
from urllib.parse import urlparse
from urllib.request import urlopen


def request_url(url: str) -> str:
    parsed_url = urlparse(url)
    if parsed_url.scheme not in {"http", "https"}:
        raise ValueError("Only http:// and https:// URLs are supported.")

    with urlopen(url, timeout=10) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main() -> None:
    if len(sys.argv) <= 1:
        print("Hello from tyler-fresh-pyproject!")
        return

    print(request_url(sys.argv[1]))
