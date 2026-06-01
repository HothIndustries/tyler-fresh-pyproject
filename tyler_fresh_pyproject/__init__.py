"""Minimal package for tyler-fresh-pyproject."""

from typing import Optional, Sequence
from urllib.request import urlopen


def make_request(url: str, timeout: float = 10.0) -> str:
    """Fetch text content from a URL."""
    with urlopen(url, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = list(argv) if argv is not None else []
    if not args:
        print("Hello from tyler-fresh-pyproject!")
        return
    print(make_request(args[0]))
