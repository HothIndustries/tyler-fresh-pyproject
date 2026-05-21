"""Minimal package for tyler-fresh-pyproject."""

from urllib.request import urlopen
import sys


def make_request(url: str, timeout: float = 10.0) -> str:
    with urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8")


def main(argv: list[str] | None = None) -> None:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("Hello from tyler-fresh-pyproject!")
        return

    print(make_request(args[0]))
