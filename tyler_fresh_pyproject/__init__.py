"""Minimal package for tyler-fresh-pyproject."""

from tyler_fresh_pyproject.http_client import delete, get, post, put

__all__ = ["delete", "get", "main", "post", "put"]


def main() -> None:
    print("Hello from tyler-fresh-pyproject!")
