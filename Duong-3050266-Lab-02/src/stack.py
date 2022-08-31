"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Stack
"""

from typing import TypeVar
from .node import Node
Self = TypeVar("Self", bound="Stack")

class Stack():
  T = TypeVar("T")
  current_node: Node = None

  def __init__(self: Self, entry: T = None) -> Self:
    self.current_node = entry

  def push(self: Self, entry: T) -> None:
    old_node = self.current_node
    new_node = Node(entry)
    new_node.link_next(old_node)
    self.current_node = new_node
      
  def pop(self: Self) -> T:
    temp_current_node = self.current_node
    if (temp_current_node is not None):
      self.current_node = temp_current_node.next
      return temp_current_node.curr
    else:
      return RuntimeError("Could not pop")

  def peek_front(self: Self) -> T:
    if (self.current_node is not None):
      return self.current_node.curr
    else:
      return RuntimeError("Could not peek at stack")

  def is_empty(self: Self) -> bool:
    return self.current_node is None
