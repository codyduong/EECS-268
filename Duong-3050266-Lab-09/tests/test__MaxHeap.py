from typing import Any
import unittest
from src.MaxHeap import MaxHeap


class TestHeap(unittest.TestCase):
    maxDiff: None = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

    def test_heap(self) -> None:
        heap: MaxHeap[int] = MaxHeap(1, 2, 3, 4, 5)
        self.assertListEqual(heap.heap, [5, 3, 4, 1, 2])

    def test_add_heap(self) -> None:
        heap: MaxHeap[int] = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(5)
        # heap.insert(15)
        self.assertListEqual(heap.heap, [5, 1, 2])
