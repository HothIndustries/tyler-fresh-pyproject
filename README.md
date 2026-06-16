# tyler-fresh-pyproject

A minimal Python project with HTTP request support.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## HTTP Requests

The package exposes lightweight `get` and `post` helpers built on the Python
standard library (`urllib`) — no extra dependencies required.

```python
from tyler_fresh_pyproject import get, post

# GET request
data = get("https://httpbin.org/get")

# POST request
response = post("https://httpbin.org/post", data={"key": "value"})
```
