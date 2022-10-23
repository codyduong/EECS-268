"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Stack

Modified for lab06 adding a __len__ dunder method
"""

from typing import TypeVar
from .Node import Node
Self = TypeVar("Self", bound="Stack")

class Stack():
  T = TypeVar("T")
  current_node: Node = None

  def __init__(self: Self, entry: T = None) -> None:
    self._length: int = 1 if entry else 0
    self.current_node = entry

  def push(self: Self, entry: T) -> Self:
    old_node = self.current_node
    new_node = Node(entry)
    new_node.link_next(old_node)
    self.current_node = new_node
    self._length += 1
    return self
      
  def pop(self: Self) -> T:
    temp_current_node = self.current_node
    if (temp_current_node is not None):
      self.current_node = temp_current_node.next
      self._length -= 1
      return temp_current_node.value
    else:
      raise RuntimeError("Could not pop")

  def peek_front(self: Self) -> T:
    if (self.current_node is not None):
      return self.current_node.value
    else:
      return RuntimeError("Could not peek at stack")

  def is_empty(self: Self) -> bool:
    return self.current_node is None

  def __len__(self: Self) -> int:
    """
    :returns: Integer of stack length
    """
    return self._length