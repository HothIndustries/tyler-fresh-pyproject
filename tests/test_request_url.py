import unittest
from unittest.mock import MagicMock, patch

from tyler_fresh_pyproject import request_url


class RequestUrlTests(unittest.TestCase):
    def test_rejects_non_http_scheme(self) -> None:
        with self.assertRaises(ValueError):
            request_url("file:///tmp/local.txt")

    @patch("tyler_fresh_pyproject.urlopen")
    def test_returns_decoded_body_for_http_url(self, mock_urlopen: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.__enter__.return_value = mock_response
        mock_response.headers.get_content_charset.return_value = "utf-8"
        mock_response.read.return_value = b"ok"
        mock_urlopen.return_value = mock_response

        self.assertEqual(request_url("https://example.com"), "ok")


if __name__ == "__main__":
    unittest.main()
