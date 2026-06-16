"""Minimal package for tyler-fresh-pyproject."""

import json
import urllib.request
from typing import Any, Optional


def get(url: str, headers: Optional[dict] = None) -> dict:
    """Make a GET request and return the parsed JSON response."""
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())


def post(url: str, data: Any, headers: Optional[dict] = None) -> dict:
    """Make a POST request with JSON body and return the parsed JSON response."""
    body = json.dumps(data).encode()
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=body, headers=req_headers, method="POST")
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
    result = get("https://httpbin.org/get")
    print("GET response:", json.dumps(result, indent=2))
