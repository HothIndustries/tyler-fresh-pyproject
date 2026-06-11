"""Minimal package for tyler-fresh-pyproject."""

import requests


def make_request(url: str, method: str = "GET", **kwargs) -> requests.Response:
    """Make an HTTP request and return the response.

    Args:
        url: The URL to request.
        method: HTTP method (GET, POST, PUT, DELETE, etc.). Defaults to "GET".
        **kwargs: Additional keyword arguments passed to ``requests.request``.

    Returns:
        The :class:`requests.Response` object.
    """
    response = requests.request(method, url, **kwargs)
    response.raise_for_status()
    return response


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
    try:
        response = make_request("https://httpbin.org/get")
        print(f"Status: {response.status_code}")
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.RequestException as exc:
        print(f"Request failed: {exc}")
