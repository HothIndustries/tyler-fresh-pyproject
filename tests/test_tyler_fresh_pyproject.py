import io
import unittest
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import Mock, patch

import tyler_fresh_pyproject


class TylerFreshPyprojectTests(unittest.TestCase):
    def test_main_without_arguments_prints_greeting(self) -> None:
        output = io.StringIO()

        with patch("sys.argv", ["tyler-fresh"]), redirect_stdout(output):
            tyler_fresh_pyproject.main()

        self.assertEqual(output.getvalue().strip(), "Hello from tyler-fresh-pyproject!")

    def test_make_request_decodes_response(self) -> None:
        response = Mock()
        response.headers = SimpleNamespace(get_content_charset=lambda: "utf-8")
        response.read.return_value = b"example response"
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)

        with patch("tyler_fresh_pyproject.urlopen", return_value=response) as mock_urlopen:
            result = tyler_fresh_pyproject.make_request("https://example.com")

        self.assertEqual(result, "example response")
        mock_urlopen.assert_called_once_with("https://example.com", timeout=10.0)


if __name__ == "__main__":
    unittest.main()
