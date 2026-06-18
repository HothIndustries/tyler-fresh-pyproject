"""Minimal package for tyler-fresh-pyproject."""

import sys
from urllib.request import Request, urlopen


def make_request(url: str, timeout: float = 10.0) -> str:
    request = Request(url, headers={"User-Agent": "tyler-fresh-pyproject/0.1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def main() -> None:
    if len(sys.argv) > 1:
        print(make_request(sys.argv[1]))
        return

    print("Hello from tyler-fresh-pyproject!")
