import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tyler_fresh_pyproject import main


class RequestsFeatureTests(unittest.TestCase):
    def test_main_without_url_prints_greeting(self) -> None:
        with patch("sys.argv", ["tyler-fresh"]), io.StringIO() as output:
            with redirect_stdout(output):
                main()
            self.assertEqual("Hello from tyler-fresh-pyproject!\n", output.getvalue())

    def test_main_with_url_makes_request(self) -> None:
        with patch("sys.argv", ["tyler-fresh", "data:text/plain,hello-request"]), io.StringIO() as output:
            with redirect_stdout(output):
                main()
            self.assertEqual("hello-request\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
