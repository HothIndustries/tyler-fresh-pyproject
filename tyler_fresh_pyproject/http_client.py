"""HTTP client utilities using the requests library."""

from typing import Any

import requests


def get(url: str, **kwargs: Any) -> requests.Response:
    """Perform an HTTP GET request.

    Args:
        url: The URL to request.
        **kwargs: Optional keyword arguments forwarded to :func:`requests.get`.

    Returns:
        A :class:`requests.Response` object.
    """
    response = requests.get(url, **kwargs)
    response.raise_for_status()
    return response


def post(url: str, data: Any = None, json: Any = None, **kwargs: Any) -> requests.Response:
    """Perform an HTTP POST request.

    Args:
        url: The URL to request.
        data: Optional form-encoded data to send in the request body.
        json: Optional JSON-serialisable object to send in the request body.
        **kwargs: Optional keyword arguments forwarded to :func:`requests.post`.

    Returns:
        A :class:`requests.Response` object.
    """
    response = requests.post(url, data=data, json=json, **kwargs)
    response.raise_for_status()
    return response
