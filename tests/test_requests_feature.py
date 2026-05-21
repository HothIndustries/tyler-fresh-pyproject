import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tyler_fresh_pyproject import main, make_request


class MockResponse:
    def __init__(self, body: bytes) -> None:
        self._body = body

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "MockResponse":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None


class RequestsFeatureTests(unittest.TestCase):
    @patch("tyler_fresh_pyproject.urlopen")
    def test_make_request_returns_decoded_text(self, mocked_urlopen) -> None:
        mocked_urlopen.return_value = MockResponse(b"ok")

        result = make_request("https://example.com")

        self.assertEqual(result, "ok")
        mocked_urlopen.assert_called_once_with("https://example.com", timeout=10.0)

    @patch("tyler_fresh_pyproject.make_request")
    def test_main_prints_response_when_url_arg_is_present(self, mocked_make_request) -> None:
        mocked_make_request.return_value = "response-body"
        output = io.StringIO()

        with redirect_stdout(output):
            main(["https://example.com"])

        self.assertEqual(output.getvalue().strip(), "response-body")
        mocked_make_request.assert_called_once_with("https://example.com")

    def test_main_prints_default_message_without_args(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            main([])

        self.assertEqual(output.getvalue().strip(), "Hello from tyler-fresh-pyproject!")


if __name__ == "__main__":
    unittest.main()
