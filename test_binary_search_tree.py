import unittest
from binary_search_tree import BSTNode, BinarySearchTree


class TestBST(unittest.TestCase):

    def setUp(self):
        self.test_tree = BinarySearchTree()

    def tearDown(self):
        del self.test_tree

    def test_init(self):
        self.assertEqual(self.test_tree.root, None)

    def test_insert_root(self):
        self.test_tree.insert(1)
        self.assertEqual(self.test_tree.root.value, 1)

    def test_insert_root_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(0)
        self.assertEqual(self.test_tree.root.left.value, 0)

    def test_insert_root_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(2)
        self.assertEqual(self.test_tree.root.right.value, 2)

    def test_insert_root_right_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(2)
        self.test_tree.insert(3)
        self.assertEqual(self.test_tree.root.right.right.value, 3)

    def test_insert_root_left_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(0)
        self.test_tree.insert(-1)
        self.assertEqual(self.test_tree.root.left.left.value, -1)

    def test_insert_root_right_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(3)
        self.test_tree.insert(2)
        self.assertEqual(self.test_tree.root.right.left.value, 2)

    def test_insert_root_left_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(-1)
        self.test_tree.insert(0)
        self.assertEqual(self.test_tree.root.left.right.value, 0)

    def test_search_empty_tree(self):
        self.assertFalse(self.test_tree.search(1))

    def test_search_missing_value(self):
        self.test_tree.insert(1)
        self.assertFalse(self.test_tree.search(2))

    def test_search_root(self):
        self.test_tree.insert(1)
        self.assertTrue(self.test_tree.search(1))

    def test_search_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(2)
        self.assertTrue(self.test_tree.search(2))

    def test_search_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(0)
        self.assertTrue(self.test_tree.search(0))

    def test_search_right_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(2)
        self.test_tree.insert(3)
        self.assertTrue(self.test_tree.search(3))

    def test_search_right_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(3)
        self.test_tree.insert(2)
        self.assertTrue(self.test_tree.search(2))

    def test_search_left_left(self):
        self.test_tree.insert(1)
        self.test_tree.insert(0)
        self.test_tree.insert(-1)
        self.assertTrue(self.test_tree.search(-1))

    def test_search_left_right(self):
        self.test_tree.insert(1)
        self.test_tree.insert(-1)
        self.test_tree.insert(0)
        self.assertTrue(self.test_tree.search(0))


if __name__ == "__main__":
    unittest.main()