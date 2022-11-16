"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-14
Lab: lab09
Last modified: 2022-11-16
Description: Test MaxHeap Class
"""

from typing import Any
import unittest
from src.MaxHeap import MaxHeap


class TestHeap(unittest.TestCase):
    maxDiff: None = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

    def test_heap(self) -> None:
        heap: MaxHeap[int] = MaxHeap(1, 2, 3, 4, 5)
        self.assertListEqual(heap.heap, [5, 4, 2, 1, 3])

    def test_add_heap(self) -> None:
        heap: MaxHeap[int] = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(5)
        # heap.insert(15)
        self.assertListEqual(heap.heap, [5, 1, 2])

    def test_remove_heap(self) -> None:
        heap: MaxHeap[int] = MaxHeap([1, 2, 3], 4, 5, 5)
        self.assertListEqual(heap.heap, [5, 4, 5, 1, 3, 2])
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 4)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 1)
