import unittest
from unittest.mock import patch

from exercise1.src.history import History


class TestHistory(unittest.TestCase):
  @patch('lab3.src.history.history_input', return_value='lab3/tests/input.txt')
  def test_all(self, _):
    history = History()
    history.prompt_file_input()
    
