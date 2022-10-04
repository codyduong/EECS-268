import unittest
from unittest.mock import patch
from exercise1.tests.testutil import text_str, str_to_matrix
from exercise1.src.blob import Blob


class TestBlobPromptFile(unittest.TestCase):
    maxDiff = None

    def __init__(self, *argv):
        super().__init__(*argv)

        self.tests = [
            (
                text_str("input1"),
                [
                    str_to_matrix(
                        """##S#
#PS#
##S#
SPP#"""
                    ),
                    (0, 2),
                ],
            ),
            (
                text_str("input2"),
                [
                    str_to_matrix(
                        """PSSSSSS#
######S#
@SSSSSP#
########
###S####
@SSS#SS#
#S####S#
###PPPSP"""
                    ),
                    (0, 0),
                ],
            ),
        ]

    def test_inputs(self):
        for (input, output) in self.tests:
            with patch("builtins.input", return_value=input):
                self.assertListEqual(Blob.prompt_file()["map_state"], output[0])
                self.assertTupleEqual(Blob.prompt_file()["blob_location"], output[1])
                # print(Blob.prompt_file())
                # print(output)

    def test_invalid_file(self):
        with self.assertRaises(ValueError):
            with patch("builtins.input", return_value="foobar.txt"):
                Blob.prompt_file()

    def test_invalid_rows(self):
        with self.assertRaises(ValueError):
            with patch("builtins.input", return_value="fail_input1.txt"):
                Blob.prompt_file()

    def test_invalid_cols(self):
        with self.assertRaises(ValueError):
            with patch("builtins.input", return_value="fail_input2.txt"):
                Blob.prompt_file()

    def test_invalid_rows_and_cols(self):
        with self.assertRaises(ValueError):
            with patch("builtins.input", return_value="fail_input3.txt"):
                Blob.prompt_file()

    def test_invalid_start_pos(self):
        with self.assertRaises(ValueError):
            with patch("builtins.input", return_value="fail_input4.txt"):
                Blob.prompt_file()
