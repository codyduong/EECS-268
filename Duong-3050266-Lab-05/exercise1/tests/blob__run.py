from io import StringIO
import unittest
from unittest.mock import patch
from exercise1.tests.testutil import text_str, str_to_matrix
from exercise1.src.blob import Blob


class TestBlobRun(unittest.TestCase):
    maxDiff = None

    def __init__(self, *argv):
        super().__init__(*argv)

        self.tests = [
            (text_str(f"input{i}"), text_str(f"output{i}")) for i in range(2, 3)
        ]

    def test_run(self):
        for (input, output) in self.tests:
            with patch("builtins.input", return_value=input):
                blob = Blob(**Blob.prompt_file())
                # blob.run()
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    blob.run()
                    with open(output) as f:
                        self.assertEqual(f.read(), mock_print.getvalue().strip())
