"""Minimal package for tyler-fresh-pyproject."""

import requests


def make_request(url: str, method: str = "GET", **kwargs) -> requests.Response:
    """Make an HTTP request and return the response.

    Args:
        url: The URL to request.
        method: HTTP method (GET, POST, PUT, DELETE, etc.). Defaults to GET.
        **kwargs: Additional keyword arguments forwarded to ``requests.request``.

    Returns:
        A :class:`requests.Response` object.

    Raises:
        requests.HTTPError: If the server returned an error status code and
            ``raise_for_status`` is called on the response.
        requests.ConnectionError: If a network problem occurred.
        requests.Timeout: If the request timed out.
    """
    response = requests.request(method.upper(), url, **kwargs)
    return response


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
