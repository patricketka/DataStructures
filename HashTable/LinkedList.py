import math
import string

from Node import Node


class LinkedList:
    def __init__(self, new_node):
        self.head = new_node
        self.nil = Node(math.inf, math.inf)
        self.head.next = self.nil
        self.size = 1

    def add_node(self, new_node):
        new_node.next = self.head
        self.head = new_node
        new_node.next.previous = new_node
        self.size += 1

    def search(self, key):
        node = self.head
        while node != self.nil:
            if node.key == key:
                return node
            node = node.next
        return None

    def delete(self, node):
        if node.previous is None:
            self.head = node.next
        node.delete()
        self.size -= 1

    def increase(self, key):
        node = self.head
        while node.key != key:
            if node.key == key:
                return node
            node = node.next
        node.increase()

    def __str__(self):
        print_object = ""
        node = self.head
        while node != self.nil:
            print_object += node.__str__()
            node = node.next
        return print_object
