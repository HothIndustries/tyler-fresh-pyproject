"""Minimal package for tyler-fresh-pyproject."""

import urllib.request
import urllib.error
from typing import Optional


def make_request(url: str, timeout: int = 10) -> Optional[str]:
    """Make an HTTP GET request to the given URL and return the response body.

    Args:
        url: The URL to send the GET request to.
        timeout: Request timeout in seconds (default: 10).

    Returns:
        The response body as a string, or None if the request failed.

    Raises:
        ValueError: If the URL is empty or None.
    """
    if not url:
        raise ValueError("URL must not be empty.")
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Request to {url!r} failed: {exc.reason}") from exc


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
