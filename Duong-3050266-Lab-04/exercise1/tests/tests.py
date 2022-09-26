"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-25
Lab: lab04
Last modified: 2022-09-25
Purpose: Test recursive power functionality
"""


from io import StringIO
import unittest
from unittest.mock import patch
from exercise1.exercise1 import RecursivePower


class TestPower(unittest.TestCase):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.tests = [
            (["2", "0"], "Answer: 1"),
            (["2", "1"], "Answer: 2"),
            (["2", "2"], "Answer: 4"),
            (["2", "3"], "Answer: 8"),
            (["2", "4"], "Answer: 16"),
            (["2", "5"], "Answer: 32"),
            (
                ["2", "256"],
                "Answer: 115792089237316195423570985008687907853269984665640564039457584007913129639936",
            ),
            (
                ["5", "96"],
                "Answer: 12621774483536188886587657044524579674771302961744368076324462890625",
            ),
            # it takes too long for this test to pass
            # (
            #     ["2", "455"],
            #     "Answer: 93035356709837681990313447409664580397266094167976711716030745495121828878514934185752454491361736391777602765602070775492429008462675968",
            # ),
            (["5", "0", "5"], "Answer: 1"),
            (["5", "-1", "1"], "Sorry, your exponent must be zero or larger.\nAnswer: 5"),
            (
                ["5", "1.25", "1"],
                "There was an error, try again!\n invalid literal for int() with base 10: '1.25'\nAnswer: 5",
            ),
            (
                ["2", "-1", "-1", "-1", "-1", "-1", "10"],
                "Sorry, your exponent must be zero or larger.\nSorry, your exponent must be zero or larger.\nSorry, your exponent must be zero or larger.\nSorry, your exponent must be zero or larger.\nSorry, your exponent must be zero or larger.\nAnswer: 1024",
            ),
        ]

    def test(self):
        rp = RecursivePower()
        for (side_effect, result) in self.tests:
            with patch("builtins.input", side_effect=side_effect):
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    rp.prompt()
                    self.assertEqual(mock_print.getvalue().rstrip(), f"{result}")
