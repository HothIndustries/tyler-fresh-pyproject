import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

from tyler_fresh_pyproject import main, make_request


class RequestsFeatureTests(unittest.TestCase):
    def test_make_request_returns_response_body(self) -> None:
        mock_response = MagicMock()
        mock_response.read.return_value = b"ok"
        mock_response.__enter__.return_value = mock_response

        with patch("tyler_fresh_pyproject.urlopen", return_value=mock_response) as mock_urlopen:
            result = make_request("https://example.com")

        self.assertEqual(result, "ok")
        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.full_url, "https://example.com")

    def test_main_prints_hello_without_args(self) -> None:
        with patch("tyler_fresh_pyproject.sys.argv", ["tyler-fresh"]):
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                main()

        self.assertEqual(stdout.getvalue().strip(), "Hello from tyler-fresh-pyproject!")

    def test_main_uses_request_when_url_is_provided(self) -> None:
        with patch("tyler_fresh_pyproject.sys.argv", ["tyler-fresh", "https://example.com"]), patch(
            "tyler_fresh_pyproject.make_request",
            return_value="response body",
        ):
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                main()

        self.assertEqual(stdout.getvalue().strip(), "response body")


if __name__ == "__main__":
    unittest.main()
