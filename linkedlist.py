# based on implementation at https://realpython.com/linked-lists-python/

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
            node.next = None

    def __len__(self):
        node = self.head
        counter = 0
        while node != None:
            counter += 1
            node = node.next
        return counter

    def __str__(self):
        '''prints in format head -> ... -> tail -> None'''
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def is_empty(self):
        return self.head == None

    def add_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def add_back(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            for node in self:
                pass
            node.next = new_node

    def add_after(self, target_val, val_to_add):
        if self.head == None:
            raise Exception("List is empty")

        new_node = Node(val_to_add)

        for node in self:
            if node.value == target_val:
                new_node.next = node.next
                node.next = new_node
                return
            
        raise Exception("Node with value '%s' not found" % target_val)

    def add_before(self, target_val, val_to_add):
        if self.head == None:
            raise Exception("List is empty")

        new_node = Node(val_to_add)

        if self.head.value == target_val:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.head
        for node in self:
            if node.value == target_val:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
            
        raise Exception("Node with value '%s' not found" % target_val)

    def remove_node(self, target_val):
            if self.head == None:
                raise Exception("List is empty")

            if self.head.value == target_val:
                self.head = self.head.next
                return
            
            prior_node = self.head
            node = self.head.next

            while node != None:
                if node.value == target_val:
                    prior_node.next = node.next
                    return
                prior_node = node
                node = node.next

            raise Exception("Node with value '%s' not found" % target_val)

    def __getitem__(self, target_index):
        if self.head == None:
            raise Exception("List is empty")
        
        for index, node in enumerate(self):
            if index == target_index:
                return node.value

        raise Exception("Node at index '%s' not found" % target_index)

    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        
        reversed_list = LinkedList()

        for node in self:
            reversed_list.add_front(node.value)

        self.head = reversed_list.head
