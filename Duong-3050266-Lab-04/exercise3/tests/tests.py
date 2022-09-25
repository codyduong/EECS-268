"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-25
Lab: lab04
Last modified: 2022-09-25
Purpose: Test fibonacci functionality
"""

from io import StringIO
import json
import unittest
from unittest.mock import patch
from exercise3.exercise3 import Fibonacci, FibonacciPrompter


class TestFibonacci(unittest.TestCase):
    def __init__(self, *argv):
        super().__init__(*argv)
        with open("exercise3/tests/fibonacci.json", encoding="utf8") as f:
            self.sequence = json.load(f)[:496]

    def test_fibonacci(self):
        fib = Fibonacci()
        generated = [fib.number_at(d) for d in range(0, 496)]
        self.assertListEqual(self.sequence[:496], generated)

    def test_in(self):
        fib = Fibonacci()
        sequence = self.sequence
        generated = [fib.in_sequence(d) for d in sequence[:496]]
        self.assertTrue(all(generated))

    def test_not_in(self):
        fib = Fibonacci()
        sequence = self.sequence
        generated = [not fib.in_sequence(d * 4096) for d in sequence[:496]]
        self.assertFalse(all(generated))

    def test_prompter_verify_in(self):
        for v in self.sequence[:496]:
            with patch("builtins.input", return_value=f"-v {v}"):
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    FibonacciPrompter().prompt()
                    self.assertEqual(
                        mock_print.getvalue().rstrip(), f"{v} is in the sequence"
                    )

    def test_prompter_verify_out(self):
        for v in self.sequence[1:496]:
            with patch("builtins.input", return_value=f"-v {v*4096}"):
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    FibonacciPrompter().prompt()
                    self.assertEqual(
                        mock_print.getvalue().rstrip(),
                        f"{v*4096} is not in the sequence",
                    )

    def test_prompter_n(self):
        prompter = FibonacciPrompter()
        for n in range(490):
            with patch("builtins.input", return_value=f"-i {n}"):
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    prompter.prompt()
                    self.assertEqual(
                        mock_print.getvalue().rstrip(), f"{self.sequence[n]}"
                    )

    def test_prompter_bad(self):
        BAD_COMMAND_AND_RESULT = [
            [
                "a",
                "Error encountered, program terminated gracefully:\nNot enough flags received: 2, received: 1",
            ],
            [
                "a 1",
                "Error encountered, program terminated gracefully:\nUnsupported mode received, expected one of: dict_keys(['-i', '-v']), received: a",
            ],
            [
                "-v -v",
                "Error encountered, program terminated gracefully:\ninvalid literal for int() with base 10: '-v'",
            ],
            [
                "-v 1024.5",
                "Error encountered, program terminated gracefully:\ninvalid literal for int() with base 10: '1024.5'",
            ],
            # [
            #     "-v 1024.5",
            #     "Error encountered, program terminated gracefully:\nUnsupported value type recieved, expected type of: <class 'int'>, received: <class 'float'>",
            # ],
            [
                "-i 5000",
                "Error encountered, program terminated gracefully:\nmaximum recursion depth exceeded",
            ],
        ]

        prompter = FibonacciPrompter()
        for (command, result) in BAD_COMMAND_AND_RESULT:
            with patch("builtins.input", return_value=f"{command}"):
                with patch("sys.stdout", new=StringIO()) as mock_print:
                    prompter.prompt()
                    self.assertEqual(mock_print.getvalue().rstrip(), result)
