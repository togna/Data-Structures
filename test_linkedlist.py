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

    # is_empty tests
    def test_isempty_empty_list(self):
        test_list = LinkedList()
        self.assertEqual(test_list.is_empty(), True)

    def test_isempty_non_empty_list(self):
        test_list = LinkedList([1])
        self.assertEqual(test_list.is_empty(), False)

    # add_front tests
    def test_add_front_empty_list(self):
        test_list = LinkedList()
        test_list.add_front(1)
        self.assertEqual(test_list.head.value, 1)

    def test_add_front_one_ele_list(self):
        test_list = LinkedList()
        test_list.add_front("one")
        test_list.add_front("two")
        self.assertEqual(test_list.head.value, "two")

    def test_add_front_two_ele_list(self):
        test_list = LinkedList()
        test_list.add_front("uno")
        test_list.add_front("dos")
        test_list.add_front("tres")
        self.assertEqual(test_list.head.value, "tres")

    # add_back tests
    def test_add_back_empty_list(self):
        test_list = LinkedList()
        test_list.add_back(1)
        self.assertEqual(test_list.head.value, 1)

    def test_add_back_one_ele_list(self):
        test_list = LinkedList()
        test_list.add_back("one")
        test_list.add_back(2)
        self.assertEqual(test_list.head.next.value, 2)

    def test_add_back_two_ele_list(self):
        test_list = LinkedList()
        test_list.add_back("one")
        test_list.add_back(2)
        test_list.add_back("tres")
        self.assertEqual(test_list.head.next.next.value, "tres")

    # add_after tests
    def test_add_after_empty_list(self):
        test_list = LinkedList()
        with self.assertRaises(Exception):
            test_list.add_after(1, 2)

    def test_add_after_one_ele(self):
        test_list = LinkedList([1])
        test_list.add_after(1, 2)
        self.assertEqual(test_list.head.next.value, 2)

    def test_add_after_first_ele(self):
        test_list = LinkedList([1, 2])
        test_list.add_after(1, 3)
        self.assertEqual(test_list.head.next.value, 3)

    def test_add_after_last_ele(self):
        test_list = LinkedList([1, 2])
        test_list.add_after(2, 3)
        self.assertEqual(test_list.head.next.next.value, 3)

    def test_add_after_missing_ele(self):
        test_list = LinkedList([1, 2, 3])
        with self.assertRaises(Exception):
            test_list.add_after(4, 5)

    # add_before tests
    def test_add_before_empty_list(self):
        test_list = LinkedList()
        with self.assertRaises(Exception):
            test_list.add_before(1, 2)

    def test_add_before_one_ele(self):
        test_list = LinkedList([1])
        test_list.add_before(1, 2)
        self.assertEqual(test_list.head.value, 2)

    def test_add_before_mid_list(self):
        test_list = LinkedList([1, 2])
        test_list.add_before(2, 3)
        self.assertEqual(test_list.head.next.value, 3)

    def test_add_before_last_ele(self):
        test_list = LinkedList([1, 2, 3])
        test_list.add_before(3, 4)
        self.assertEqual(test_list.head.next.next.value, 4)

    def test_add_before_missing_ele(self):
        test_list = LinkedList([1, 2, 3])
        with self.assertRaises(Exception):
            test_list.add_before(4, 5)

    # remove_node tests
    def test_rm_node_empty_list(self):
        test_list = LinkedList()
        with self.assertRaises(Exception):
            test_list.remove_node(1)

    def test_rm_non_existant_node(self):
        test_list = LinkedList([1, 2, 3])
        with self.assertRaises(Exception):
            test_list.remove_node(4)

    def test_rm_node_one_ele(self):
        test_list = LinkedList(["one"])
        test_list.remove_node("one")
        self.assertEqual(test_list.head, None)

    def test_rm_middle_node(self):
        test_list = LinkedList(["uno", "dos", "tres"])
        test_list.remove_node("dos")
        self.assertEqual(test_list.head.next.value, "tres")

    def test_rm_last_node(self):
        test_list = LinkedList(["one", "two", "three"])
        test_list.remove_node("three")
        self.assertEqual(test_list.head.next.next, None)

    # __getitem__ tests
    def test_getitem_empty_list(self):
        test_list = LinkedList()
        with self.assertRaises(Exception):
            test_list[0]
    
    def test_getitem_out_of_bounds(self):
        test_list = LinkedList([1, 2, 3])
        with self.assertRaises(Exception):
            test_list[3]

    def test_getitem_first(self):
        test_list = LinkedList(["one"])
        self.assertEqual(test_list[0], "one")

    def test_getitem_middle(self):
        test_list = LinkedList(["uno", "dos", "tres"])
        self.assertEqual(test_list[1], "dos")

    def test_getitem_last(self):
        test_list = LinkedList([1, 2, 3])
        self.assertEqual(test_list[2], 3)

    # reverse tests
    def test_reverse_empty_list(self):
        test_list = LinkedList()
        test_list.reverse()
        self.assertTrue(test_list.is_empty())

    def test_reverse_single_item(self):
        test_list = LinkedList(["uno"])
        test_list.reverse()
        self.assertEqual(test_list.head.value, "uno")

    def test_reverse_two_items(self):
        test_list = LinkedList([1, 2])
        test_list.reverse()
        flag = True
        value = 2
        for node in test_list:
            if node.value != value:
                flag = False
                break
            value -= 1
        self.assertTrue(flag)

    def test_reverse_three_items(self):
        test_list = LinkedList([1, 2, 3])
        test_list.reverse()
        flag = True
        value = 3
        for node in test_list:
            if node.value != value:
                flag = False
                break
            value -= 1
        self.assertTrue(flag)


if __name__ == "__main__":
    unittest.main()