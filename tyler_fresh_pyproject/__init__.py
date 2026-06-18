"""Minimal package for tyler-fresh-pyproject."""

import requests


def make_request(url: str, method: str = "GET", **kwargs) -> requests.Response:
    """Make an HTTP request to the given URL.

    Args:
        url: The URL to send the request to.
        method: HTTP method (GET, POST, PUT, DELETE, etc.). Defaults to GET.
        **kwargs: Additional keyword arguments passed to requests.request().

    Returns:
        A requests.Response object.
    """
    response = requests.request(method, url, **kwargs)
    response.raise_for_status()
    return response


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
