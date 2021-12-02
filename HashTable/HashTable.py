from LinkedList import LinkedList
from Node import Node


class HashTable:
    def __init__(self, m):
        self.slots = m
        self.hashes = [None] * m

    def hash_function(self, word):
        ## Djb2 c
        new_hash = 5381
        for i in range(len(word)-1):
            new_hash = ((new_hash << 5) + new_hash) + ord(word[i])

        return new_hash % self.slots

    # Constant time (not considering HF).  Finds slot, if no linked list there yet it will start one with the new key
    def insert(self, key, value):
        node = Node(key, value)
        index = self.hash_function(node.key)
        if self.hashes[index] is not None:
            self.hashes[index].add_node(node)
        else:
            self.hashes[index] = LinkedList(node)

    # Theta(omega). Finds slot where key should be.  If linked list, it searches for key and due to size of hash and
    # collision handling we expect the list to have n/m elements
    def find(self, k):
        index = self.hash_function(k)
        if self.hashes[index] is not None:
            return self.hashes[index].search(k)
        return None

    # Theta(omega). Finds slot where key should be.  If linked list, it searches for key and due to size of hash and
    # collision handling we expect the list to have n/m elements.  Then once node is found it's just a pointer change.
    def delete(self, key):
        index = self.hash_function(key)
        if self.hashes[index] is not None:
            node = self.hashes[index].search(key)
            return self.hashes[index].delete(node)
        return None

    # Theta(omega). Finds slot where key should be.  If linked list, it searches for key and due to size of hash and
    # collision handling we expect the list to have n/m elements. Then constant time to increase count of node.
    def increase(self, key):
        index = self.hash_function(key)
        self.hashes[index].increase(key)

    def __str__(self):
        temp = ""
        for slot in range(self.slots):
            if self.hashes[slot] is not None:
                temp += self.hashes[slot].__str__()

        return temp