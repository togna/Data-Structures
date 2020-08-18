import unittest
from linkedlist import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    # __init__ tests
    def test_init_empty_list(self):
        test_list = LinkedList()
        self.assertEqual(test_list.head, None)

    def test_init_one_ele_list(self):
        test_list = LinkedList(["one"])
        self.assertEqual(test_list.head.value, "one")

    def test_init_two_ele_list(self):
        test_list = LinkedList([1, 2])
        self.assertEqual(test_list.head.next.value, 2)

    # __str__ tests
    def test_str_empty_list(self):
        test_list = LinkedList()
        self.assertEqual(test_list.__str__(), "None")

    def test_str_one_ele_list(self):
        test_list = LinkedList([1])
        self.assertEqual(test_list.__str__(), "1 -> None")

    def test_str_two_ele_list(self):
        test_list = LinkedList(["one", "two"])
        self.assertEqual(test_list.__str__(), "one -> two -> None")

    # __iter__ test
    def test_iter_empty_list(self):
        test_list = LinkedList()
        count = 0
        for ele in test_list:
            count += 1
        self.assertEqual(count, 0)

    def test_iter_one_ele_list(self):
        test_list = LinkedList([1])
        result = ""
        for ele in test_list:
            result += str(ele.value)
        self.assertEqual(result, "1")

    def test_iter_two_ele_list(self):
        test_list = LinkedList(["uno", "dos"])
        result = ""
        for ele in test_list:
            result += str(ele.value)
        self.assertEqual(result, "unodos")


if __name__ == "__main__":
    unittest.main()