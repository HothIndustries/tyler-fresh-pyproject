import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
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
        pass


class RequestsFeatureTests(unittest.TestCase):
    @patch("tyler_fresh_pyproject.urlopen")
    def test_make_request_returns_decoded_text(self, mocked_urlopen) -> None:
        mocked_urlopen.return_value = MockResponse(b"ok")

        result = make_request("https://example.com")

        self.assertEqual(result, "ok")
        mocked_urlopen.assert_called_once_with("https://example.com", timeout=10.0)

    @patch("tyler_fresh_pyproject.urlopen")
    def test_make_request_uses_custom_timeout(self, mocked_urlopen) -> None:
        mocked_urlopen.return_value = MockResponse(b"ok")

        make_request("https://example.com", timeout=2.5)

        mocked_urlopen.assert_called_once_with("https://example.com", timeout=2.5)

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

    @patch("sys.argv", ["prog"])
    def test_main_uses_sys_argv_when_argv_is_none(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue().strip(), "Hello from tyler-fresh-pyproject!")

    def test_make_request_rejects_non_http_schemes(self) -> None:
        with self.assertRaisesRegex(ValueError, "Only http and https URLs are supported."):
            make_request("ftp://example.com")

    def test_make_request_rejects_missing_hostname(self) -> None:
        with self.assertRaisesRegex(ValueError, "A valid URL with a hostname is required."):
            make_request("https:///missing-host")

    def test_make_request_rejects_localhost(self) -> None:
        with self.assertRaisesRegex(
            ValueError, "Requests to local or private network hosts are not allowed."
        ):
            make_request("https://localhost")

    def test_make_request_rejects_private_ip(self) -> None:
        with self.assertRaisesRegex(
            ValueError, "Requests to local or private network hosts are not allowed."
        ):
            make_request("https://10.0.0.1")

    @patch("tyler_fresh_pyproject.make_request")
    def test_main_prints_user_friendly_error_for_failed_request(self, mocked_make_request) -> None:
        mocked_make_request.side_effect = ValueError("Request failed: boom")
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            main(["https://example.com"])

        self.assertEqual(stdout.getvalue().strip(), "")
        self.assertEqual(stderr.getvalue().strip(), "Request failed: boom")


if __name__ == "__main__":
    unittest.main()
