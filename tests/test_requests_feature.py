import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

import tyler_fresh_pyproject


class RequestsFeatureTests(unittest.TestCase):
    def test_main_without_args_keeps_greeting(self) -> None:
        with io.StringIO() as buffer, redirect_stdout(buffer):
            tyler_fresh_pyproject.main([])
            self.assertEqual("Hello from tyler-fresh-pyproject!\n", buffer.getvalue())

    def test_main_with_url_prints_response(self) -> None:
        with patch("tyler_fresh_pyproject.make_request", return_value="ok") as mock_request:
            with io.StringIO() as buffer, redirect_stdout(buffer):
                tyler_fresh_pyproject.main(["https://example.com"])
                self.assertEqual("ok\n", buffer.getvalue())
        mock_request.assert_called_once_with("https://example.com")

    def test_make_request_reads_and_decodes_response(self) -> None:
        mock_response = MagicMock()
        mock_response.read.return_value = b"hello world"
        mock_response.headers.get_content_charset.return_value = "utf-8"
        context_manager = MagicMock()
        context_manager.__enter__.return_value = mock_response
        context_manager.__exit__.return_value = None

        with patch("tyler_fresh_pyproject.urlopen", return_value=context_manager) as mock_urlopen:
            result = tyler_fresh_pyproject.make_request("https://example.com")

        self.assertEqual("hello world", result)
        mock_urlopen.assert_called_once_with("https://example.com", timeout=10.0)


if __name__ == "__main__":
    unittest.main()
