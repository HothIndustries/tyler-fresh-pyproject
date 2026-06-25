import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

import tyler_fresh_pyproject


class MainTests(unittest.TestCase):
    def test_make_request_returns_text(self) -> None:
        response = MagicMock()
        response.read.return_value = b"ok"
        response.headers.get_content_charset.return_value = None
        response.__enter__.return_value = response

        with patch("tyler_fresh_pyproject.urlopen", return_value=response):
            result = tyler_fresh_pyproject.make_request("https://example.com")

        self.assertEqual(result, "ok")

    def test_main_without_args_prints_greeting(self) -> None:
        with patch("tyler_fresh_pyproject.sys.argv", ["tyler-fresh"]):
            stream = io.StringIO()
            with redirect_stdout(stream):
                tyler_fresh_pyproject.main()

        self.assertEqual(stream.getvalue().strip(), "Hello from tyler-fresh-pyproject!")

    def test_main_with_url_prints_response_body(self) -> None:
        with patch("tyler_fresh_pyproject.sys.argv", ["tyler-fresh", "https://example.com"]):
            with patch("tyler_fresh_pyproject.make_request", return_value="body"):
                stream = io.StringIO()
                with redirect_stdout(stream):
                    tyler_fresh_pyproject.main()

        self.assertEqual(stream.getvalue().strip(), "body")


if __name__ == "__main__":
    unittest.main()
