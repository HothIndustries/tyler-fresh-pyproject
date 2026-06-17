# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## Making HTTP Requests

`tyler-fresh-pyproject` exposes a `make_request` helper that wraps the
[`requests`](https://pypi.org/project/requests/) library:

```python
from tyler_fresh_pyproject import make_request

# Simple GET request
response = make_request("https://httpbin.org/get")
print(response.status_code)   # 200
print(response.json())

# POST request with JSON body
response = make_request(
    "https://httpbin.org/post",
    method="POST",
    json={"key": "value"},
)
response.raise_for_status()
print(response.json())
```

Any keyword argument accepted by
[`requests.request`](https://requests.readthedocs.io/en/latest/api/#requests.request)
(e.g. `headers`, `params`, `timeout`, `auth`, …) can be passed as `**kwargs`.
