"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Linked Queue
"""

from typing import TypeVar
from .node import Node
Self = TypeVar("Self", bound="LinkedQueue")

class LinkedQueue:
  T = TypeVar("T")
  _current_node: Node = None

  def __init__(self: Self) -> Self:
    pass

  @property
  def current_node(self: Self) -> Node:
    return self._current_node

  @current_node.setter
  def curret_node(self: Self, n: Node) -> None:
    self._current_node = n

  def enqueue(self: Self, entry: T) -> None:
    next_node: Node = self.current_node
    if (self.curret_node is not None):
      while True:
        if (next_node is not None and next_node.next is not None):
          next_node = next_node.next
        else:
          next_node.link_next(Node(entry))
          break
    else:
      self.curret_node = Node(entry)
      
  def dequeue(self: Self) -> T:
    temp_current_node = self.current_node
    if (temp_current_node is not None):
      self._current_node = temp_current_node.next
      return temp_current_node.curr
    else:
      return RuntimeError("Could not dequeue")

  def peek_front(self: Self) -> T:
    if (self.current_node is not None):
      return self.current_node.curr
    else:
      return RuntimeError("Could not peek at queue")

  def is_empty(self: Self) -> bool:
    return self.current_node is None
