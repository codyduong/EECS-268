import unittest
from unittest.mock import patch

from exercise1.src.blob import Blob


class TestBlobPromptFile(unittest.TestCase):
    maxDiff = None

    def __init__(self, *argv):
        super().__init__(*argv)

        def text_str(str: str) -> str:
            return f"exercise1/tests/mocks/input{str}.txt"

        self.tests = [
            (
                text_str(1),
                [
                    [
                        ["#", "#", "S", "#"],
                        ["#", "P", "S", "#"],
                        ["#", "#", "S", "#"],
                        ["S", "P", "P", "#"],
                    ],
                    [0, 2],
                ],
            ),
        ]

    def test_inputs(self):
        for (input, output) in self.tests:
            with patch("builtins.input", return_value=input):
                # self.assertListEqual(Blob.prompt_file(), output)
                print(Blob.prompt_file())
                print(output)
