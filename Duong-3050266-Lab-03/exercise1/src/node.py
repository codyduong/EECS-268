"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab03
Last modified: 2022-09-22
Purpose: Node
"""

from typing import Any, Generic, TypeVar
from .typingx import Self, TypeGuard

Self = TypeVar("Self", bound="Node")

T = TypeVar("T")


class Node(Generic[T]):
    """
    This node implementation with the ability to link and unlink previous/next nodes
    """

    def __init__(self: Self, value: T, prev: Self = None, next: Self = None) -> Self:
        """
        :param value: The value of the node
        :param prev: Optional. Set the previous node
        :param next: Optional. Set the next node
        """
        self._value = value
        self.link_prev(prev)
        self.link_next(next)

    @property
    def value(self: Self) -> T:
        return self._value

    @property
    def prev(self: Self) -> Self:
        return self._prev

    @property
    def next(self: Self) -> Self:
        return self._next

    @value.setter
    def value(self: Self, value: T) -> T:
        self._value = value

    def link_prev(self: Self, prev_node: Self) -> None:
        """
        Links the previous pointer towards another Node, and also sets that Node's forwards pointer to this Node

        :param prev_node: Node instance
        """
        self._prev = prev_node
        if prev_node and prev_node.next is None:
            prev_node.link_next(self)

    def link_next(self: Self, next_node: Self) -> None:
        """
        Links the forwards pointer towards another Node, and also sets that Node's previous pointer to this Node

        :param prev_node: Node instance
        """
        self._next = next_node
        if next_node and next_node.prev is None:
            next_node.link_prev(self)

    def unlink_prev(self: Self) -> None:
        """
        Unlinks the forwards pointer towards another Node, and also sets that Node's previous pointer to this None

        :param prev_node: Node instance
        """
        if self._prev and self._prev.next:
            self._prev.unlink_next()
        self._prev = None

    def unlink_next(self: Self) -> None:
        """
        Unlinks the previous pointer towards another Node, and also sets that Node's forwards pointer to this None

        :param prev_node: Node instance
        """
        if self._next and self._next.prev:
            self._next.unlink_prev()
        self._next = None

    def __str__(self: Self) -> str:
        return str(self._value)

    @staticmethod
    def isinstance(arg: Any) -> "TypeGuard[Node[T]]":
        """Typeguards if it is an own instance, see PEP-0647"""
        return isinstance(arg, Node)
