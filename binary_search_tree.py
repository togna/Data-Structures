from enum import Enum

class EdgeType(Enum):
    ROOT = 0
    LEFT = 1
    RIGHT = 2

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = BSTNode(value)
        if self.root == None:
            self.root = new_node
            return
        
        compared_node = self.root
        while compared_node != None:
            if value > compared_node.value:
                if compared_node.right == None:
                    compared_node.right = new_node
                    return
                else:
                    compared_node = compared_node.right
            else:
                if compared_node.left == None:
                    compared_node.left = new_node
                    return
                else:
                    compared_node = compared_node.left

    def search(self, value):
        compared_node = self.root
        while compared_node != None:
            if value == compared_node.value:
                return True
            if value > compared_node.value:
                compared_node = compared_node.right
            else:
                compared_node = compared_node.left
        return False

    def replace_node(self, parent, edge_type, old_child, new_child):
        if edge_type == EdgeType.ROOT:
            self.root = new_child
        elif edge_type == EdgeType.LEFT:
            parent.left = new_child
        else:
            parent.right = new_child
        if new_child:
            new_child.right = old_child.right
            new_child.left = old_child.left

    def leftmost_child(self, parent, node):
        while True:
            if node.left == None:
                return parent, node
            parent = node
            node = node.left


    def delete(self, value):
        if self.root == None:
            raise Exception("Tree is empty")

        parent = self
        node = self.root
        parent_edge = EdgeType.ROOT
        while node != None:
            if value == node.value:
                if node.right == None and node.left == None:
                    self.replace_node(parent, parent_edge, node, None)
                elif node.right == None and node.left != None:
                    self.replace_node(parent, parent_edge, node, node.left)
                elif node.left == None:
                    self.replace_node(parent, parent_edge, node, node.right)
                else:
                    leftmost_parent, leftmost = self.leftmost_child(node, node.right)
                    leftmost_parent.left = leftmost.right
                    self.replace_node(parent, parent_edge, node, leftmost)
                return
            
            parent = node
            if value > node.value:
                node = node.right
                parent_edge = EdgeType.RIGHT
            else:
                node = node.left
                parent_edge = EdgeType.LEFT

        raise Exception("Value not found in tree")

    
