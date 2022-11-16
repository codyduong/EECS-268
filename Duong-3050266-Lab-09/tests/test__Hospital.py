"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-16
Lab: lab09
Last modified: 2022-11-16
Description: Test Hospital Class
"""

from io import StringIO, TextIOWrapper
from typing import Any
import unittest
from unittest.mock import patch

from .testutil import text_number_tuple
from src.Hospital import Hospital


class TestHospital(unittest.TestCase):
    maxDiff: None = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)
        self.tests: list[tuple[str, TextIOWrapper]] = [
            text_number_tuple(i) for i in range(1, 4)
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            with patch("sys.stdout", new=StringIO()) as mock_print:
                Hospital().run(input)
                self.assertEqual(
                    mock_print.getvalue().rstrip(),
                    "".join(output.readlines()),
                )
                output.close()

    def tearDown(self) -> None:
        for (_, output) in self.tests:
            output.close()

        return super().tearDown()
