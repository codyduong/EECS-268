"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Linked Queue

Modified for lab06 adding a __len__ dunder method
Also added a custom function to speed up arbitrary instantiation
"""

from typing import Any, TypeVar, Union
from .Node import Node
Self = TypeVar("Self", bound="LinkedQueue")

class LinkedQueue:
  T = TypeVar("T")
  _front: Union[Node[Any], None] = None
  # _back:  Union[Node[Any], None] = None

  def __init__(self) -> None:
    self._length: int = 0

  def enqueue(self: Self, entry: T) -> None:
    temp_node = self._front
    next_node = self._front
    while (next_node is not None):
      temp_node = next_node
      next_node = next_node.next
    if (temp_node is not None):
      temp_node.link_next(Node(entry))
    else:
      self._front = Node(entry)
    self._length += 1
      
  def dequeue(self: Self) -> T:
    temp_current_node = self._front
    if (temp_current_node is not None):
      self._front = temp_current_node.next
      self._length -= 1
      return temp_current_node.value
    else:
      return RuntimeError("Could not dequeue")

  def peek_front(self: Self) -> T:
    if (self._front is not None):
      return self._front.value
    else:
      return RuntimeError("Could not peek at queue")

  def is_empty(self) -> bool:
    return self._front is None

  def __len__(self) -> int:
    return self._length

  def arbitrary_fill(self: Self, i: int) -> Self:
    """
    Needed some faster way to instantiate a queue of arbitrary length... 
    Otherwise I would be waiting until the heat death of the universe
    """
    if (self._front is not None):
      raise ValueError("This function can only be used on an empty queue")

    end_node: Node[str] = Node('end')
    temp_node: Node[str] = end_node
    for _ in range(i):
      """
      Link from the end of the queue to the front, because it will be faster
      
      This is just a stack LOL
      """
      temp_node.link_prev(Node('foo'))
      temp_node = temp_node.prev
    """Set the current node to the last node in the stack, as the new front"""
    self._front = temp_node
    # self._back = end_node
    self._length = i
    return self
