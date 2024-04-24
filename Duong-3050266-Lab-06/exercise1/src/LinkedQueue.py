from .Node import Node

# queue is already used
class LinkedQueue:
  _front = None
  # _back = None

  def __init__(self):
    self._length: int = 0

  def enqueue(self, entry):
    temp_node = self._front
    next_node = self._front
    while (next_node is not None):
      temp_node = next_node
      next_node = next_node.next
    else:
      self._front = Node(entry)
    self._length += 1
      
  def dequeue(self):
    temp_current_node = self._front
    if (temp_current_node is not None):
      self._front = temp_current_node.next
      self._length -= 1
      return temp_current_node.value
    else:
      return RuntimeError("Could not dequeue")

  def peek_front(self):
    if self.current_node is not None:
      return self.current_node.curr
    else:
      return RuntimeError("Could not peek at queue")

  def is_empty(self):
    return self.current_node is None

  def __len__(self):
    return self._length

  def arbitrary_fill(self, i):
    if (self._front is not None):
      raise ValueError("This function can only be used on an empty queue")

    end_node: Node[str] = Node('end')
    temp_node: Node[str] = end_node
    for _ in range(i):
      """
      This is just a stack LOL
      """
      temp_node.link_prev(Node('foo'))
      temp_node = temp_node.prev
    """Set the current node to the last node in the stack, as the new front"""
    self._front = temp_node
    # self._back = end_node
    self._length = i
    return self