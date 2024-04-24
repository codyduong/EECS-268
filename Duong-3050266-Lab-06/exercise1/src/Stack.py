from .Node import Node

class Stack():
  current_node = None

  def __init__(self, entry=None):
    self.current_node = entry
    self._length: int = 1 if entry else 0

  def push(self, entry):
    old_node = self.current_node
    new_node = Node(entry)
    new_node.link_next(old_node)
    self.current_node = new_node
    self._length += 1
    return self
      
  def pop(self):
    temp_current_node = self.current_node
    if temp_current_node is not None:
      self.current_node = temp_current_node.next
      self._length -= 1
      return temp_current_node.value
    else:
      raise RuntimeError("Could not pop")

  def peek(self):
    if self.current_node is not None:
      return self.current_node.value
    else:
      raise RuntimeError("Could not peek at stack")

  def is_empty(self):
    return self.current_node is None

  def __len__(self):
    """
    :returns: Integer of stack length
    """
    return self._length