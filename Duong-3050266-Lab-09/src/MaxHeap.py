"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-14
Lab: lab09
Last modified: 2022-11-14
Description: Max heap implementation
"""

from typing import Generic, TypeVar
from .Comparable import Comparable


T = TypeVar("T", bound=Comparable)


class MaxHeap(Generic[T]):
    """Maxheap implementation"""

    def __init__(self, *values: T | list[T]) -> None:
        self._list: list[T] = []
        for value in values:
            if isinstance(value, list):
                for v in value:  # type: ignore
                    self.insert(v)  # type: ignore
            else:
                self.insert(value)

    @property
    def heap(self) -> list[T]:
        return self._list

    def parent(self, i: int) -> T:
        """
        Returns the parent of i

        :param i: int
        :return T:
        """
        return self._list[i // 2]

    @staticmethod
    def left(i: int) -> int:
        return i * 2 + 1

    def left_child(self, i: int) -> T:
        """
        Returns the left child of i

        :param i: int
        :return T:
        """
        return self._list[MaxHeap.left(i)]

    @staticmethod
    def right(i: int) -> int:
        return i * 2 + 2

    def right_child(self, i: int) -> T:
        """
        Returns the right child of i

        :param i: int
        :return T: typeof values in MaxHeap
        """
        return self._list[MaxHeap.right(i)]

    def _iheapify(self, i: int) -> None:
        """
        "heapifies" the heap to follow heap rules

        Follows a bottom-up heapify, assuming the starting i is the out-of-order element

        :param i: location of out-of-order value
        :return None:
        """
        parent: int = (i - 1) // 2

        heap = self._list

        # print(heap, i, parent)
        if parent >= 0:
            if heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                self._iheapify(parent)

    def insert(self, value: T) -> None:
        """
        Insert a value into the heap

        :param value: any
        :return None:
        """
        self._list.append(value)
        # print("insert", value)
        self._iheapify(len(self._list) - 1)

    def _dheapify(self, i: int) -> None:
        """
        "heapifies" the heap to follow heap rules

        Follows a top down heapify, assumes the other subtree is already heap-correct

        :param i: largest node to start at
        :return None:
        """
        largest: int = i
        left: int = MaxHeap.left(i)
        right: int = MaxHeap.right(i)

        if left < len(self._list) and self._list[largest] < self._list[left]:
            largest = left

        if right < len(self._list) and self._list[largest] < self._list[right]:
            largest = right

        if largest != i:
            # swap the two positions
            self._list[i], self._list[largest] = self._list[largest], self._list[i]

            self._dheapify(largest)

    def pop(self) -> T | None:
        """
        Pop the root of the heap

        :return T | None: Returns the value of the popped root if successful, None if there is none
        """
        self._list[0], self._list[-1] = self._list[-1], self._list[0]
        popped_root: T | None = self._list.pop() if len(self._list) > 0 else None
        self._dheapify(0)
        return popped_root

    def __len__(self) -> int:
        return len(self._list)

    def peek(self) -> T | None:
        """Returns the top of the heap without removing it"""
        return self._list[0]
