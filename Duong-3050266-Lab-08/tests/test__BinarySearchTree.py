from typing import Any
import unittest
from src.BinarySearchTree import BinarySearchTree


class TestBlobPromptFile(unittest.TestCase):
    maxDiff = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

        test_bst1: BinarySearchTree[int] = BinarySearchTree()
        test_bst1.add(50)
        test_bst1.add(25)
        test_bst1.add(75)
        test_bst1.add(12)
        test_bst1.add(37)
        self.test_bst1: BinarySearchTree[int] = test_bst1

    def test_preorder(self) -> None:
        self.assertListEqual(self.test_bst1.preorder(), [50, 25, 12, 37, 75])

    def test_inorder(self) -> None:
        self.assertListEqual(self.test_bst1.inorder(), [12, 25, 37, 50, 75])

    def test_postorder(self) -> None:
        self.assertListEqual(self.test_bst1.postorder(), [12, 37, 25, 75, 50])
