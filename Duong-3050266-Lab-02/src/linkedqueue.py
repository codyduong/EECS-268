from .node import Node

# queue is already used
class LinkedQueue:
  _current_node = None

  def __init__(self):
    pass

  @property
  def current_node(self):
    return self._current_node

  @current_node.setter
  def current_node(self, n):
    self._current_node = n

  def enqueue(self, entry):
    next_node = self.current_node
    if self.current_node is not None:
      while True:
        if next_node is not None and next_node.next is not None:
          next_node = next_node.next
        else:
          next_node.link_next(Node(entry))
          break
    else:
      self.current_node = Node(entry)
      
  def dequeue(self):
    temp_current_node = self.current_node
    if temp_current_node is not None:
      self._current_node = temp_current_node.next
      return temp_current_node.curr
    else:
      return RuntimeError("Could not dequeue")

  def peek_front(self):
    if self.current_node is not None:
      return self.current_node.curr
    else:
      return RuntimeError("Could not peek at queue")

  def is_empty(self):
    return self.current_node is None
