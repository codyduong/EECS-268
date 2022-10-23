"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-22
Lab: lab03
Last modified: 2022-09-22
Purpose: LinkedList

Optimized with some tail-end/cache previous accessed value
"""

from .Node import Node
from .assertx import assertx
from typing import Any, Callable, Generic, Iterable, Tuple, TypeVar, Union
from .typingx import Self, TypeGuard

LinkedList = TypeVar("LinkedList", bound="LinkedList")


Self = TypeVar("Self", bound="LinkedListIterator")
T = TypeVar("T")


class LinkedListIterator(Generic[T]):
    """
    Iterable helper class for LinkedList to make iteration easier
    """

    def __init__(self: Self, linked_list: LinkedList) -> Self:
        self._linked_list = linked_list  # type: LinkedList[T]
        self._index = 0  # type: int

    def __iter__(self):
        return self

    def __next__(self: Self) -> T:
        if self._index < len(self._linked_list):
            result = self._linked_list[self._index]
            self._index += 1
            return result
        raise StopIteration


Self = TypeVar("Self", bound="LinkedList")
T = TypeVar("T")


class LinkedListOptimized(Generic[T]):
    """
    Doubly linked list
    """

    def __init__(self: Self, *argv: Union[Self, T, Iterable]) -> Self:
        """
        Initialize a linked list with elements (optional)

        :param items: Optional. Accepts individual elements (not in a Node).
        """
        self._head = None  # type: Node[T]
        self._tail = None  # type: Node[T]
        self._length = 0  # type: int

        # cache recently accessed value
        self._cache: Union[None, Tuple[int, Node[T]]] = None

        if len(argv) > 0:
            for arg in argv:
                if Node.isinstance(arg):
                    raise TypeError(
                        "Node instances are not supported, they are automatically instantiated by LinkedList"
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
        assertx(isinstance(index, int), TypeError, "index is not of type int")

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
        assertx(isinstance(index, int), TypeError, f"index is not of type int")

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
        A convenience method around __getitem__, only supports indexes (not slices),
        and is bound by 0 and list length (inclusive)

        :returns: Integer containing list length
        """
        return self.__getitem__(index)

    def set_entry(self: Self, index: int, value: T) -> None:
        """
        A convenience method around __setitem__, only supports indexes (not slices),
        and is bound by 0 and list length (inclusive)

        :returns: Integer containing list length
        """
        self.__setitem__(index, value)

    def clear(self: Self) -> None:
        """Empties the list"""
        self._head = None
        self._tail = None
        self._length = 0

    def __iterate_to(
        self: Self,
        index: Union[int, slice],
        callback: Callable[[Union[Self, Node]], Any],
    ) -> Any:
        """
        Helper function for __getitem__ and __setitem__, uses a callback to do an action on any elem in list.
        """

        is_int = isinstance(index, int)
        is_slice = isinstance(index, slice)

        assertx(
            is_int or is_slice,
            TypeError,
            "index is not of type int or slice",
        )

        curr_node = self._head
        try:
            if is_int:
                head_diff = index
                tail_diff = self._length - index
                cache_diff = index - self._cache[0] if self._cache else self._length

                if self._cache is not None and (
                    min(head_diff, tail_diff) > abs(cache_diff)
                ):
                    # use a cached value if it is available
                    curr_node = self._cache[1]
                    if cache_diff > 0:
                        for _ in range(abs(cache_diff)):
                            curr_node = curr_node.next
                    elif cache_diff < 0:
                        for _ in range(abs(cache_diff)):
                            curr_node = curr_node.prev
                    self._cache = (index, curr_node)
                    return callback(curr_node)
                elif head_diff > tail_diff:
                    print("tailed")
                    curr_node = self._tail
                    for _ in range(tail_diff):
                        curr_node = curr_node.prev
                    self._cache = (index, curr_node)
                    return callback(curr_node)
                elif head_diff < tail_diff:
                    # head-end search
                    for _ in range(head_diff):
                        if curr_node and curr_node.next:
                            curr_node = curr_node.next
                    self._cache = (index, curr_node)
                    return callback(curr_node)
            elif is_slice:
                temp_list = LinkedList()
                start = index.start or 0
                stop = index.stop or len(self)
                step = index.step or 1
                assertx(
                    start >= 0,
                    ValueError,
                    "Slicing with negative numbers is not supported",
                )
                assertx(
                    stop >= 0,
                    ValueError,
                    "Slicing with negative numbers is not supported",
                )
                assertx(
                    step >= 0,
                    ValueError,
                    "Slicing with negative numbers is not supported",
                )
                for i in range(stop):
                    if i >= start and (i + start) % step == 0:
                        temp_list.append(curr_node.value)
                    if curr_node and curr_node.next:
                        curr_node = curr_node.next

                return callback(temp_list)
        except AttributeError as e:
            """
            ...raises a RuntimeError otherwise. Ideally we'd cover this with the proper errors,
            typically an IndexError, but it's explicitly stated otherwise on the lab reqs. w/e
            """
            raise RuntimeError(e)

    def __getitem__(self: Self, index: Union[int, slice]) -> T:
        """
        Only supports 0 to index length inclusive,
        Slicing is implemented but does not support negative ints
        """

        return self.__iterate_to(
            index,
            lambda node_or_list: node_or_list.value
            if isinstance(node_or_list, Node)
            else node_or_list,
        )

    def __setitem__(self: Self, index: int, value: T) -> None:
        """
        Only supports 0 to index length inclusive,
        Slicing is not implemented/supported
        """
        assertx(
            isinstance(index, int),
            TypeError,
            "index is not of type int",
        )

        def set_item_callback(node: Self) -> None:
            node.value = value

        return self.__iterate_to(index, set_item_callback)

    def __iter__(self: Self) -> LinkedListIterator[T]:
        return LinkedListIterator(self)

    def __add__(self: Self, other_list: Self) -> Self:
        temp_list = self
        for elem in other_list:
            temp_list.append(elem)
        return temp_list

    def __str__(self: Self) -> str:
        output_str = "["
        for elem in self:
            output_str += f"{elem}, "
        output_str = output_str[:-2]
        output_str += "]"
        return output_str

    @staticmethod
    def isinstance(arg: Any) -> "TypeGuard[LinkedList[T]]":
        """Typeguards if it is an own instance, see PEP-0647"""
        return isinstance(arg, LinkedList)
