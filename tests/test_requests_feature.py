"""Tests for the HTTP request feature in tyler_fresh_pyproject."""

import unittest
from unittest.mock import MagicMock, patch
import urllib.error

from tyler_fresh_pyproject import make_request


class TestMakeRequest(unittest.TestCase):
    """Unit tests for make_request()."""

    @patch("urllib.request.urlopen")
    def test_successful_get_request(self, mock_urlopen: MagicMock) -> None:
        """make_request returns the response body on a successful request."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"Hello, world!"
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = make_request("https://example.com")

        self.assertEqual(result, "Hello, world!")
        mock_urlopen.assert_called_once_with("https://example.com", timeout=10)

    @patch("urllib.request.urlopen")
    def test_custom_timeout(self, mock_urlopen: MagicMock) -> None:
        """make_request passes the timeout argument to urlopen."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"data"
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        make_request("https://example.com", timeout=30)

        mock_urlopen.assert_called_once_with("https://example.com", timeout=30)

    def test_empty_url_raises_value_error(self) -> None:
        """make_request raises ValueError when url is empty."""
        with self.assertRaises(ValueError):
            make_request("")

    def test_none_url_raises_value_error(self) -> None:
        """make_request raises ValueError when url is None."""
        with self.assertRaises(ValueError):
            make_request(None)  # type: ignore[arg-type]

    @patch("urllib.request.urlopen")
    def test_url_error_raises_runtime_error(self, mock_urlopen: MagicMock) -> None:
        """make_request raises RuntimeError when a URLError occurs."""
        mock_urlopen.side_effect = urllib.error.URLError("connection refused")

        with self.assertRaises(RuntimeError) as ctx:
            make_request("https://unreachable.example.com")

        self.assertIn("connection refused", str(ctx.exception))

    @patch("urllib.request.urlopen")
    def test_response_decoded_as_utf8(self, mock_urlopen: MagicMock) -> None:
        """make_request decodes the response body as UTF-8."""
        mock_response = MagicMock()
        mock_response.read.return_value = "こんにちは".encode("utf-8")
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = make_request("https://example.com")

        self.assertEqual(result, "こんにちは")


if __name__ == "__main__":
    unittest.main()
