"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-22
Lab: lab03
Last modified: 2022-09-22
Purpose: LinkedList
"""

from .node import Node
from typing import Generic, TypeVar, Union
from .typingx import Self, TypeGuard

Self = TypeVar("Self", bound="LinkedList")

T = TypeVar("T")


class LinkedList(Generic[T]):
    """
    Doubly linked list
    """

    def __init__(self, *argv: Union[Self, T]) -> Self:
        """
        Initialize a linked list with elements (optional)

        :param items: Optional. Accepts multiple LinkedList classes or individual elements (not in a Node).
        Fills current LinkedList if provided with either.
        """
        self._head = None  # type: Node[T]
        self._tail = None  # type: Node[T]
        self._length = 0  # type: int

        if len(argv) > 0:
            for arg in argv:
                if LinkedList.isinstance(arg):
                    for i in range(len(arg)):
                        self.append(arg.get_entry(i))
                elif Node.isinstance(arg):
                    raise RuntimeError(
                        "Node elements are not supported, they are automatically instantiated by LinkedList"
                    )
                else:
                    # Conditional typeflow is weak sauce
                    self.append(arg)

    def __set_head_tail(self: Self) -> None:
        """Private helper method to set the TAIL to HEAD or HEAD to TAIL if length is only 1"""
        if len(self) == 1:
            # Probably a bit unidiomatic... w/e
            self._tail = self._tail or self._head
            self._head = self._head or self._tail

    def length(self: Self) -> int:
        """
        A convenience method around __len__, recommended to use len(...) instead

        :returns: Integer of list length
        """
        return self.__len__()

    def __len__(self: Self) -> int:
        """
        :returns: Integer of list length
        """
        return self._length

    def append(self: Self, value: T) -> None:
        """
        Append an element to the TAIL of the LinkedList

        :param value: value to insert
        """
        new_tail = Node(value, self._tail)
        if self._tail:
            self._tail.link_next(new_tail)
        self._tail = new_tail
        self._length += 1
        self.__set_head_tail()

    def insert(self: Self, value: T, index: int = 0) -> None:
        """
        Insert an element at an index, by default is at HEAD

        :param value: value to insert
        :param index: to insert element at, by default inserts at HEAD
        """
        if index > len(self):
            raise IndexError(
                f"Index out of bounds, maximum index surpassed at: {len(self)}"
            )
        elif index < 0:
            raise IndexError()
        elif index == 0:
            new_head = Node(value, next=self._head)
            self._head = new_head
            self._length += 1
        elif index == len(self):
            self.append(value)
        else:
            curr_node = self._head
            for _ in range(index):
                curr_node = curr_node.next
            else:
                curr_node.link_next(Node(value, next=curr_node.next))
                self._length += 1
        self.__set_head_tail()

    def pop(self: Self, index: int = None) -> T:
        """
        Remove an element at an index, by default is at TAIL

        :param index: index to insert element at, by default removes at TAIL
        :return: The value of the element that was popped
        """
        max_len = len(self) - 1
        if index is None:
            index = max_len

        if index > max_len:
            raise IndexError(
                f"Index out of bounds, maximum index surpassed at: {max_len}"
            )
        elif index < 0:
            raise IndexError("Index cannot be negative")
        elif index == 0:
            temp_next = self._head.next
            self._head.unlink_next()
            self._head = temp_next
        elif index == max_len:
            temp_prev = self._tail.prev
            self._tail.unlink_prev()
            self._tail = temp_prev
        self._length -= 1
        self.__set_head_tail()

    def remove(self: Self, index: int = 0) -> T:
        """
        Remove an element at an index, by default is at HEAD

        :param index: index to insert element at, by default removes at HEAD
        :return: The value of the element that was popped
        """
        return self.pop(index)

    def get_entry(self: Self, index: int) -> T:
        """
        A convenience method around __getitem__, only supports indexes (not slices)

        :returns: Integer containing list length
        """
        return self.__getitem__(index)

    def set_entry(self: Self, index: int, value: T) -> None:
        """
        A convenience method around __setitem__, only supports indexes (not slices)

        :returns: Integer containing list length
        """
        self.__setitem__(index, value)

    def clear(self: Self) -> None:
        """Empties the list"""
        self._head = None
        self._tail = None

    def __getitem__(self: Self, index: Union[int, slice]) -> T:
        """Does not support slice object, not required"""
        if isinstance(index, slice):
            raise NotImplementedError(
                "Slice object is not supported. Because I was lazy..."
            )

        curr_node = self._head
        for _ in range(index):
            if curr_node and curr_node.next:
                curr_node = curr_node.next
            else:
                raise RuntimeError()
        try:
            return curr_node.value
        except AttributeError as e:
            raise RuntimeError(f"{e}")

    def __setitem__(self: Self, index: Union[int, slice], value: T) -> None:
        """Does not support slice object, not required"""
        if isinstance(index, slice):
            raise NotImplementedError(
                "Slice object is not supported. Because I was lazy..."
            )

        curr_node = self._head
        for _ in range(index):
            if curr_node and curr_node.next:
                curr_node = curr_node.next
            else:
                raise RuntimeError()
        try:
            curr_node.value = value
        except AttributeError as e:
            raise RuntimeError(f"{e}")

    @staticmethod
    def isinstance(arg) -> "TypeGuard[LinkedList[T]]":
        """Typeguards if it is an own instance, see PEP-0647"""
        return isinstance(arg, LinkedList)
