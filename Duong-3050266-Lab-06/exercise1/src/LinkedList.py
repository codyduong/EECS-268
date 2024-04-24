from .Node import Node

class LinkedListIterator:
    """
    Iterable helper class for LinkedList to make iteration easier
    """

    def __init__(self, linked_list):
        self._linked_list = linked_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._linked_list):
            result = self._linked_list[self._index]
            self._index += 1
            return result
        raise StopIteration

class LinkedList:
    """
    Doubly linked list
    """

    def __init__(self, *argv):
        """
        Initialize a linked list with elements (optional)

        :param items: Optional. Accepts individual elements (not in a Node).
        """
        self._head = None
        self._tail = None
        self._length = 0

        if len(argv) > 0:
            for arg in argv:
                if Node.isinstance(arg):
                    raise TypeError(
                        "Node instances are not supported, they are automatically instantiated by LinkedList"
                    )
                else:
                    self.append(arg)

    def __set_head_tail(self):
        """Private helper method to set the TAIL to HEAD or HEAD to TAIL if length is only 1"""
        if len(self) == 1:
            self._tail = self._tail or self._head
            self._head = self._head or self._tail

    def length(self):
        """
        A convenience method around __len__, recommended to use len(...) instead

        :returns: Integer of list length
        """
        return self.__len__()

    def __len__(self):
        """
        :returns: Integer of list length
        """
        return self._length

    def append(self, value):
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

    def insert(self, value, index=0):
        """
        Insert an element at an index, by default is at HEAD

        :param value: value to insert
        :param index: to insert element at, by default inserts at HEAD
        """

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

    def pop(self, index=None):
        """
        Remove an element at an index, by default is at TAIL

        :param index: index to insert element at, by default removes at TAIL
        :return: The value of the element that was popped
        """

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

    def remove(self, index=0):
        """
        Remove an element at an index, by default is at HEAD

        :param index: index to insert element at, by default removes at HEAD
        :return: The value of the element that was popped
        """
        return self.pop(index)

    def clear(self):
        """Empties the list"""
        self._head = None
        self._tail = None
        self._length = 0
        
    def get_entry(self, index):
        """
        A convenience method around __getitem__, only supports indexes (not slices),
        and is bound by 0 and list length (inclusive)

        :returns: Integer containing list length
        """
        return self.__getitem__(index)

    def set_entry(self, index, value):
        """
        A convenience method around __setitem__, only supports indexes (not slices),
        and is bound by 0 and list length (inclusive)

        :returns: Integer containing list length
        """
        self.__setitem__(index, value)

    def __iterate_to(
        self,
        index,
        callback,
    ):
        """
        Helper function for __getitem__ and __setitem__, uses a callback to do an action on any elem in list.
        """

        is_int = isinstance(index, int)
        is_slice = isinstance(index, slice)

        curr_node = self._head
        try:
            if is_int:
                for _ in range(index):
                    if curr_node and curr_node.next:
                        curr_node = curr_node.next
                return callback(curr_node)

            elif is_slice:
                temp_list = LinkedList()
                start = index.start or 0
                stop = index.stop or len(self)
                step = index.step or 1
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

    def __getitem__(self, index):
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

    def __setitem__(self, index, value):
        """
        Only supports 0 to index length inclusive,
        Slicing is not implemented/supported
        """
        def set_item_callback(node):
            node.value = value

        return self.__iterate_to(index, set_item_callback)

    def __iter__(self):
        return LinkedListIterator(self)

    def __add__(self, other_list):
        temp_list = self
        for elem in other_list:
            temp_list.append(elem)
        return temp_list

    def __str__(self):
        output_str = "["
        for elem in self:
            output_str += f"{elem}, "
        output_str = output_str[:-2]
        output_str += "]"
        return output_str

    @staticmethod
    def isinstance(arg):
        return isinstance(arg, LinkedList)
