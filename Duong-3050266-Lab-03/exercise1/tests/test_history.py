"""
Author: Cody Duong
KUID: 3050266
Date: 202-09-23
Lab: lab03
Last modified: 2022-09-23
Purpose: Test history functionality
"""
from io import StringIO
import unittest
from unittest.mock import patch

from exercise1.src.history import History

class TestHistory(unittest.TestCase):
  maxDiff = None


  @patch('builtins.input', return_value='exercise1/tests/mocks/test0.txt')
  def test0(self, *_):
    with open("exercise1/tests/mocks/test0.out.txt", encoding="utf-8") as f:
        with patch('sys.stdout', new = StringIO()) as mock_print:
            history = History()
            history.prompt_file_input()
            self.assertEqual(mock_print.getvalue().rstrip(), f.read())
            
  @patch('builtins.input', return_value='exercise1/tests/mocks/test1.txt')
  def test1(self, *_):
    with open("exercise1/tests/mocks/test1.out.txt", encoding="utf-8") as f:
        with patch('sys.stdout', new = StringIO()) as mock_print:
            history = History()
            self.assertEqual(history.index, 0)
            history.prompt_file_input()
            self.assertEqual(mock_print.getvalue().rstrip(), f.read())
            self.assertEqual(history.index, 1)
            history.forward()
            history.forward()
            self.assertEqual(history.index, 1)
            history.back()
            history.back()
            history.back()
            history.back()
            self.assertEqual(history.index, 0)

  @patch('builtins.input', return_value='exercise1/tests/mocks/test2.txt')
  def test2(self, *_):
    """This tests incorrect/invalid inputs"""
    with open("exercise1/tests/mocks/test2.out.txt", encoding="utf-8") as f:
        with patch('sys.stdout', new = StringIO()) as mock_print:
            history = History()
            history.prompt_file_input()
            self.assertEqual(mock_print.getvalue().rstrip(), f.read())
