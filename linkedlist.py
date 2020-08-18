#!/usr/bin/env python3


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

    def __str__(self):
        '''prints in format head -> ... -> tail -> None'''
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
