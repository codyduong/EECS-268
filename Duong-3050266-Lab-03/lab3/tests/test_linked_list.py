import unittest

from lab3.src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def __init__(self, *argv):
        super().__init__(*argv)
        self._empty_list = LinkedList()

    def assertException(self, fn, args, error):
        try:
            fn(*args)
        except Exception as e:
            self.assertTrue(e, error)

    def test_empty(self):
        list = self._empty_list
        self.assertEqual(len(list), 0)
        self.assertEqual(list.length(), 0)

    def test_insert_on_empty(self):
        self._empty_list.insert(True, 0)
        self.assertEqual(self._empty_list.get_entry(0), True)
        self.assertEqual(self._empty_list._tail.value, True)
        self.assertEqual(self._empty_list._head.value, True)

    def test_complete(self):
        list = LinkedList(*range(10))
        list.insert(False, 3)
        list.insert(False, 9)
        self.assertEqual(list.get_entry(4), False)
        self.assertEqual(list.get_entry(10), False)
        list.remove(9)
        self.assertEqual(list.get_entry(0), 0)
        self.assertEqual(list.get_entry(4), False)
        self.assertEqual(list.get_entry(11), 9)
        self.assertEqual(list._tail.value, 9)
        self.assertEqual(list._head.value, 0)
        self.assertEqual(list[0], 0)
        self.assertEqual(list[4], False)

    def test_insert_over_index_bounds(self):
        self.assertException(self._empty_list.insert, [None, 1], IndexError)

    def test_insert_under_index_bounds(self):
        self.assertException(self._empty_list.insert, [None, -1], IndexError)

    def test_remove_over_index_bounds(self):
        self.assertException(self._empty_list.insert, [None, 1], IndexError)

    def test_remove_under_index_bounds(self):
        self.assertException(self._empty_list.insert, [None, -1], IndexError)

    def test_error_get_entry(self):
        self.assertException(self._empty_list.get_entry, [0], RuntimeError)

    def test_error_set_entry(self):
        self.assertException(self._empty_list.set_entry, [0, None], RuntimeError)
