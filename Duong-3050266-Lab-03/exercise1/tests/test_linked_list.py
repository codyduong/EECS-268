import unittest

from exercise1.src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def __init__(self, *argv):
        super().__init__(*argv)
        self._empty_list = LinkedList()

    def assertException(self, fn, args, error):
        try:
            fn(*args)
        except Exception as e:
            # print(e)
            self.assertIsInstance(e, error)

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
        self.assertEqual(len(list), 12)
        self.assertEqual(list.get_entry(4), False)
        self.assertEqual(list.get_entry(10), False)
        list.remove(9)
        self.assertEqual(len(list), 11)
        self.assertEqual(list.get_entry(0), 0)
        self.assertEqual(list.get_entry(4), False)
        self.assertEqual(list.get_entry(11), 9)
        self.assertEqual(list._tail.value, 9)
        self.assertEqual(list._head.value, 0)
        self.assertEqual(list[0], 0)
        self.assertEqual(list[4], False)
        list[4] = True
        self.assertEqual(list[4], True)
        list.set_entry(4, False)
        self.assertEqual(list[4], False)
        list.clear()
        self.assertEqual(len(list), 0)

    def test_iteratable(self):
        list = LinkedList(*range(10))
        list_iter = iter(list)
        self.assertListEqual([elem for elem in list_iter], [*range(10)])

    def test_slice(self):
        list = LinkedList(*range(10))
        list_sliced1 = list[0:5:2]
        self.assertListEqual([elem for elem in list_sliced1], [0, 2, 4])
        list_sliced2 = list[:9]
        self.assertListEqual([elem for elem in list_sliced2], [*range(9)])

    def test_add(self):
        list1 = LinkedList(*range(10))
        list2 = LinkedList(*range(10))
        self.assertListEqual([elem for elem in list1 + list2], [*range(10)] + [*range(10)])

    def test_conditional(self):
        list1 = LinkedList(*range(10))
        self.assertTrue(1 in list1)
        self.assertTrue(10 not in list1)

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

    def test_insert_invalid_type(self):
        self.assertException(self._empty_list.insert, ["10", None], TypeError)
