"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-30
Lab: lab07
Last modified: 2022-10-30
Purpose: Binary Search Tree Node
"""

from typing import Any, Generic, NewType, TypeVar, Union


BinarySearchTreeNodeValue = TypeVar("BinarySearchTreeNodeValue")
BinarySearchTreeNodeSubnode = NewType(
    "BinarySearchTreeNodeSubnode", "BinarySearchTreeNode[BinarySearchTreeNodeValue]"
)
BinarySearchTreeNodeSubnodeExpanded = Union[BinarySearchTreeNodeSubnode, None]


class BinarySearchTreeNode(Generic[BinarySearchTreeNodeValue]):
    """
    A binary search tree node, a binary search tree node's subnodes typeof left and right trees must be equivalent
    to the parent value type. IE. the tree must all be of the same type.
    """

    @property
    def left(self) -> BinarySearchTreeNodeSubnodeExpanded:
        return self._left

    @left.setter
    def left(self, v: BinarySearchTreeNodeSubnodeExpanded) -> None:
        self._left = v

    @property
    def right(self) -> BinarySearchTreeNodeSubnodeExpanded:
        return self._right

    @right.setter
    def right(self, v: BinarySearchTreeNodeSubnodeExpanded) -> None:
        self._right = v

    @property
    def value(self) -> BinarySearchTreeNodeValue:
        return self._value

    @value.setter
    def value(self, v: BinarySearchTreeNodeValue) -> None:
        self._value = v

    def __init__(
        self,
        value: BinarySearchTreeNodeValue,
        left: BinarySearchTreeNodeSubnodeExpanded = None,
        right: BinarySearchTreeNodeSubnodeExpanded = None,
    ) -> None:
        self._value = value
        self._left: BinarySearchTreeNodeSubnodeExpanded = left
        self._right: BinarySearchTreeNodeSubnodeExpanded = right

    def __gt__(self, other: Any) -> bool:
        return self.value > other.value

    def __lt__(self, other: Any) -> bool:
        return self.value < other.value

    def __eq__(self, other: Any) -> bool:
        return self.value == other.value

    def __str__(self) -> str:
        return f"{self.value}, l: {self.left}, r: {self.right}"
