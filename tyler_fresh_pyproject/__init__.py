"""Minimal package for tyler-fresh-pyproject."""

import requests


def fetch(url: str) -> requests.Response:
    """Make a GET request to the given URL and return the response."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
    response = fetch("https://httpbin.org/get")
    print(f"Status: {response.status_code}")
    print(f"Response JSON: {response.json()}")
