# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## Making HTTP Requests

The package exposes simple helpers for the four most common HTTP methods:

```python
from tyler_fresh_pyproject import get, post, put, delete

# GET
response = get("https://httpbin.org/get")
print(response.json())

# POST
response = post("https://httpbin.org/post", json={"key": "value"})
print(response.json())

# PUT
response = put("https://httpbin.org/put", json={"key": "updated"})
print(response.json())

# DELETE
response = delete("https://httpbin.org/delete")
print(response.status_code)
```

All helpers call `raise_for_status()` automatically, so any 4xx/5xx response
raises a `requests.HTTPError`.
