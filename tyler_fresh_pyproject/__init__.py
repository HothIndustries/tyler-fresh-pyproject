"""Minimal package for tyler-fresh-pyproject."""

from typing import Any, Optional
import requests


def make_request(
    url: str,
    method: str = "GET",
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
    timeout: int = 10,
) -> requests.Response:
    """Make an HTTP request and return the response.

    Args:
        url: The URL to request.
        method: HTTP method (GET, POST, PUT, DELETE, etc.).
        params: Query parameters to include in the request.
        data: Data to send in the request body (for POST/PUT).
        headers: HTTP headers to include in the request.
        timeout: Request timeout in seconds.

    Returns:
        The HTTP response object.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    response = requests.request(
        method=method.upper(),
        url=url,
        params=params,
        json=data,
        headers=headers,
        timeout=timeout,
    )
    response.raise_for_status()
    return response


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
