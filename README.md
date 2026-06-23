# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## Making HTTP Requests

The package exposes a `make_request` helper built on Python's standard-library
`urllib.request` — no extra dependencies required.

```python
from tyler_fresh_pyproject import make_request

# Simple GET request
body = make_request("https://httpbin.org/get")
print(body)

# POST request with a JSON payload
import json
payload = json.dumps({"key": "value"}).encode("utf-8")
body = make_request("https://httpbin.org/post", method="POST", data=payload)
print(body)
```
