# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+
- [requests](https://pypi.org/project/requests/) ≥ 2.28

## Run

```bash
python -m tyler_fresh_pyproject
```

## Making HTTP Requests

The package exposes simple `get` and `post` helpers built on top of the
[requests](https://pypi.org/project/requests/) library.

```python
from tyler_fresh_pyproject import get, post

# GET request
response = get("https://httpbin.org/get")
print(response.json())

# POST request with JSON body
response = post("https://httpbin.org/post", json={"key": "value"})
print(response.json())
```

Both helpers call `response.raise_for_status()` automatically, so any HTTP
error (4xx / 5xx) will raise a `requests.HTTPError`.
