"""Minimal package for tyler-fresh-pyproject."""

from tyler_fresh_pyproject.http_client import get, post

__all__ = ["get", "post", "main"]


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
