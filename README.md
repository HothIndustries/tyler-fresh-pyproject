# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Installation

```bash
pip install .
```

## Run

```bash
python -m tyler_fresh_pyproject
```

## Making HTTP Requests

The package exposes a `make_request` helper that wraps the `requests` library:

```python
from tyler_fresh_pyproject import make_request

# Simple GET request
response = make_request("https://httpbin.org/get")
print(response.json())

# POST request with JSON body
response = make_request(
    "https://httpbin.org/post",
    method="POST",
    data={"key": "value"},
    headers={"Accept": "application/json"},
)
print(response.json())
```
