"""Simple HTTP client helpers using the requests library."""

from __future__ import annotations

from typing import Any

import requests


def get(url: str, **kwargs: Any) -> requests.Response:
    """Send a GET request to *url* and return the response."""
    response = requests.get(url, **kwargs)
    response.raise_for_status()
    return response


def post(url: str, data: Any = None, json: Any = None, **kwargs: Any) -> requests.Response:
    """Send a POST request to *url* and return the response."""
    response = requests.post(url, data=data, json=json, **kwargs)
    response.raise_for_status()
    return response


def put(url: str, data: Any = None, json: Any = None, **kwargs: Any) -> requests.Response:
    """Send a PUT request to *url* and return the response."""
    response = requests.put(url, data=data, json=json, **kwargs)
    response.raise_for_status()
    return response


def delete(url: str, **kwargs: Any) -> requests.Response:
    """Send a DELETE request to *url* and return the response."""
    response = requests.delete(url, **kwargs)
    response.raise_for_status()
    return response
