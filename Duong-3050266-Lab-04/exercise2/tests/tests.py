"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-25
Lab: lab04
Last modified: 2022-09-25
Purpose: Test outbreak functionality
"""

import json
import unittest
from exercise2.exercise2 import get_sick_number


class TestOutbreak(unittest.TestCase):
    def test(self):
        with open("exercise2/tests/sequence.json", encoding="utf8") as f:
            sequence = json.load(f)
            outbreak_sequence = [
                get_sick_number(d) for d in range(1, len(sequence) + 1)
            ]
            self.assertListEqual(sequence, outbreak_sequence)
