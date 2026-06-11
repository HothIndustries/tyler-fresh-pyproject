# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+
- `requests`

## Run

```bash
python -m tyler_fresh_pyproject
```

## HTTP Requests

The `fetch(url)` function makes a GET request and returns the response:

```python
from tyler_fresh_pyproject import fetch

response = fetch("https://httpbin.org/get")
print(response.status_code)
print(response.json())
```
