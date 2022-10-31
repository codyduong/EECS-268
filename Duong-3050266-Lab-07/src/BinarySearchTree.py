"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-30
Lab: lab07
Last modified: 2022-10-30
Purpose: Binary Search Tree Node
"""


from typing import Generic, List, TypeVar, Any, Union
from src.BinarySearchTreeNode import BinarySearchTreeNode, BinarySearchTreeNodeSubnode

BinarySearchTreeValue = TypeVar("BinarySearchTreeValue", bound="Any")


class BinarySearchTree(Generic[BinarySearchTreeValue]):
    def __init__(self) -> None:
        self._root_node: Union[
            BinarySearchTreeNode[BinarySearchTreeValue],
            None,
        ] = None
        # self._current_node: Union[
        #     BinarySearchTreeNode[BinarySearchTreeValue],
        #     None,
        # ] = None

    def _recursive_add(
        self,
        current_node: BinarySearchTreeNode[Any],
        new_node: BinarySearchTreeNode[Any],
    ) -> None:
        if current_node.value is None:
            current_node = new_node
        elif new_node < current_node:
            if current_node.left:
                self._recursive_add(current_node.left, new_node)
            else:
                current_node.left = new_node  # type: ignore
        elif new_node > current_node:
            if current_node.right:
                self._recursive_add(current_node.right, new_node)
            else:
                current_node.right = new_node  # type: ignore
        elif new_node == current_node:
            raise ValueError(
                f"Duplicate value of: {new_node.value} was attempted to add to the BST, duplicate values are not allowed!"
            )
        else:
            raise RuntimeError(
                "An unknown exception occured while attempting to recursively add a node to the BST"
            )

    def add(self, value: BinarySearchTreeValue) -> None:
        root_node: BinarySearchTreeNode[
            BinarySearchTreeValue @ BinarySearchTree[BinarySearchTreeValue]
        ] | None = self._root_node
        new_node: BinarySearchTreeNode[
            BinarySearchTreeValue @ BinarySearchTree[BinarySearchTreeValue]
        ] = BinarySearchTreeNode(value)
        if root_node is None:
            self._root_node = new_node
        else:
            return self._recursive_add(root_node, new_node)

    def preorder(
        self,
        node: Union[
            None,
            BinarySearchTreeNodeSubnode,
        ] = None,
        order: List[BinarySearchTreeValue] = [],
    ) -> List[BinarySearchTreeValue]:
        """
        Return the preorder of the BST
        """
        root_node: BinarySearchTreeNode[
            BinarySearchTreeValue @ BinarySearchTree[BinarySearchTreeValue]
        ] | None = (node or self._root_node)
        if root_node:
            order.append(root_node.value)  # type: ignore

            if root_node.left:
                self.preorder(root_node.left, order)

            if root_node.right:
                self.preorder(root_node.right, order)

        return order

    def inorder(
        self,
        node: Union[
            None,
            BinarySearchTreeNodeSubnode,
        ] = None,
        order: List[BinarySearchTreeValue] = [],
    ) -> List[BinarySearchTreeValue]:
        """
        Return the inorder of the BST
        """
        root_node: BinarySearchTreeNode[
            BinarySearchTreeValue @ BinarySearchTree[BinarySearchTreeValue]
        ] | None = (node or self._root_node)
        if root_node:
            if root_node.left:
                self.inorder(root_node.left)

            order.append(root_node.value)  # type: ignore

            if root_node.right:
                self.inorder(root_node.right)

        return order

    def postorder(
        self,
        node: Union[
            None,
            BinarySearchTreeNodeSubnode,
        ] = None,
        order: List[BinarySearchTreeValue] = [],
    ) -> List[BinarySearchTreeValue]:
        """
        Return the postorder of the BST
        """
        root_node: BinarySearchTreeNode[
            BinarySearchTreeValue @ BinarySearchTree[BinarySearchTreeValue]
        ] | None = (node or self._root_node)
        if root_node:

            if root_node.left:
                self.postorder(root_node.left)

            if root_node.right:
                self.postorder(root_node.right)

            order.append(root_node.value)  # type: ignore

        return order

    def search(
        self,
        value: Any,  # indexed access types where?
        *keys: str,
        current_node: Union[BinarySearchTreeNode[Any], None] = None,
    ) -> Union[BinarySearchTreeNode[BinarySearchTreeValue], None]:
        """
        This search function will return a whole node based on a subkey path.

        :value: any value to search for
        :key: property to access on node, delimited by .
        :example:
            pokedex.search(132, "id") # -> ditto

        """
        current_node = current_node or self._root_node

        if current_node is None:
            return None

        current_value: BinarySearchTreeNode[BinarySearchTreeValue] = current_node.value
        if current_value is None:
            return None

        for k in keys:
            # Of course this is unsafe
            current_value = getattr(current_value, k)  # type: ignore

        if value == current_value:
            return current_node
        elif value < current_value:
            return self.search(value, *keys, current_node=current_node.left)
        elif value > current_value:
            return self.search(value, *keys, current_node=current_node.right)
