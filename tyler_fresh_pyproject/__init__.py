"""Minimal package for tyler-fresh-pyproject."""

import urllib.request
import urllib.error
from typing import Optional


def make_request(url: str, method: str = "GET", data: Optional[bytes] = None) -> str:
    """Make an HTTP request and return the response body as a string.

    Args:
        url: The URL to request.
        method: HTTP method (e.g. "GET", "POST"). Defaults to "GET".
        data: Optional bytes payload for POST/PUT requests.

    Returns:
        The response body decoded as UTF-8.

    Raises:
        urllib.error.URLError: If the request fails.
    """
    req = urllib.request.Request(url, data=data, method=method)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
    print("Use make_request(url) to perform HTTP requests.")
