from .node import Node

class Stack():
  current_node = None

  def __init__(self, entry=None):
    self.current_node = entry

  def push(self, entry):
    old_node = self.current_node
    new_node = Node(entry)
    new_node.link_next(old_node)
    self.current_node = new_node
      
  def pop(self):
    temp_current_node = self.current_node
    if temp_current_node is not None:
      self.current_node = temp_current_node.next
      return temp_current_node.curr
    else:
      return RuntimeError("Could not pop")

  def peek(self):
    if self.current_node is not None:
      return self.current_node.curr
    else:
      return RuntimeError("Could not peek at stack")

  def is_empty(self):
    return self.current_node is None
