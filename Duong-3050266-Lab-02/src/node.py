"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Node
"""

from typing import TypeVar
Node = TypeVar("Self", bound="Node")


class Node:
    """
    This node implementation has an immutable current value with only the ability to link and unlink previous/next nodes
    """
    T = TypeVar("T")
    
    def __init__(self: Node, curr: T, prev: Node = None, next: Node = None) -> Node:
        self._curr = curr
        self._prev = prev
        self._next = next

    @property
    def curr(self: Node) -> T:
      return self._curr

    @property
    def prev(self: Node) -> Node:
      return self._prev

    @property
    def next(self: Node) -> Node:
      return self._next

    def link_prev(self: Node, prev_node: Node) -> None:
      self._prev = prev_node

    def link_next(self: Node, next_node: Node) -> None:
      self._next = next_node

    def unlink_prev(self: Node) -> None:
      self._prev = None

    def unlink_next(self: Node) -> None:
      self._next = None

    def __str__(self: Node) -> str:
      return str(self.curr)
