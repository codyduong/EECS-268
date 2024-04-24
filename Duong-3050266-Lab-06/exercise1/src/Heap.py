class MaxHeap:
    """Maxheap implementation"""

    def __init__(self, *values):
        self._list = []
        for value in values:
            if isinstance(value, list):
                for v in value:
                    self.insert(v)
            else:
                self.insert(value)

    @property
    def heap(self):
        return self._list

    def parent(self, i):
        """
        Returns the parent of i

        :param i: int
        :return T:
        """
        return self._list[i // 2]

    @staticmethod
    def left(i):
        return i * 2 + 1

    def left_child(self, i):
        """
        Returns the left child of i

        :param i: int
        :return T:
        """
        return self._list[MaxHeap.left(i)]

    @staticmethod
    def right(i):
        return i * 2 + 2

    def right_child(self, i):
        """
        Returns the right child of i

        :param i: int
        :return T: typeof values in MaxHeap
        """
        return self._list[MaxHeap.right(i)]

    def _iheapify(self, i):
        """
        "heapifies" the heap to follow heap rules

        Follows a bottom-up heapify, assuming the starting i is the out-of-order element

        :param i: location of out-of-order value
        :return None:
        """
        parent = (i - 1) // 2

        heap = self._list

        # print(heap, i, parent)
        if parent >= 0:
            if heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                self._iheapify(parent)

    def insert(self, value):
        """
        Insert a value into the heap

        :param value: any
        :return None:
        """
        self._list.append(value)
        # print("insert", value)
        self._iheapify(len(self._list) - 1)

    def _dheapify(self, i):
        """
        "heapifies" the heap to follow heap rules

        Follows a top down heapify, assumes the other subtree is already heap-correct

        :param i: largest node to start at
        :return None:
        """
        largest = i
        left = MaxHeap.left(i)
        right = MaxHeap.right(i)

        if left < len(self._list) and self._list[largest] < self._list[left]:
            largest = left

        if right < len(self._list) and self._list[largest] < self._list[right]:
            largest = right

        if largest != i:
            # swap the two positions
            self._list[i], self._list[largest] = self._list[largest], self._list[i]

            self._dheapify(largest)

    def pop(self):
        """
        Pop the root of the heap

        :return T | None: Returns the value of the popped root if successful, None if there is none
        """
        self._list[0], self._list[-1] = self._list[-1], self._list[0]
        popped_root = self._list.pop() if len(self._list) > 0 else None
        self._dheapify(0)
        return popped_root

    def __len__(self):
        return len(self._list)

    def peek(self):
        """Returns the top of the heap without removing it"""
        return self._list[0]
