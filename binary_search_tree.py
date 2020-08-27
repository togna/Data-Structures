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


    
