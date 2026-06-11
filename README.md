# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## HTTP Requests

The package exposes a `make_request` helper that performs an HTTP GET request
using Python's built-in `urllib` module (no third-party dependencies required).

```python
from tyler_fresh_pyproject import make_request

# Fetch a URL and get the response body as a string
body = make_request("https://example.com")
print(body)

# Custom timeout (seconds)
body = make_request("https://example.com", timeout=30)
```

Errors are surfaced as:
- `ValueError` – when the URL is empty or `None`.
- `RuntimeError` – when the request itself fails (e.g. network error).

## Tests

```bash
python -m unittest discover -s tests -v
```
