from random import randint
from Node import Node
import math


class SkipList:
    def __init__(self):
        self.height = 0
        self.elements = 0
        self.max_levels = 1
        self.start = Node(-math.inf, self.max_levels)

    def check_max_levels(self):
        if math.floor(math.log2(self.elements)) > self.max_levels:
            previous_levels = self.max_levels
            self.max_levels = math.floor(math.log2(self.elements))
            new_pointer_array = Node(-math.inf, self.max_levels)
            for i in range(previous_levels + 1):
                new_pointer_array.next[i] = self.start.next[i]
            self.start = new_pointer_array

    ## Theta(lg n) -> lg n to find the insert spot, and then constant to reassign pointers in at most lg n levels
    def insert(self, new_key):
        self.elements += 1
        self.check_max_levels()
        end_of_lists = [self.start] * (self.max_levels + 1)
        for i in range(self.height, -1, -1):
            while end_of_lists[i].next[i] is not None and end_of_lists[i].next[i].key < new_key:
                end_of_lists[i] = end_of_lists[i].next[i]
        height_of_new_key = self.decide_levels()
        if height_of_new_key > self.height:
            for i in range(self.height + 1, height_of_new_key + 1):
                end_of_lists[i] = self.start
            self.height = height_of_new_key
        new_node = Node(new_key, height_of_new_key)
        for i in range(0, height_of_new_key + 1):
            if end_of_lists[i].next[i] is not None:
                end_of_lists[i].next[i].previous[i] = new_node
            new_node.next[i] = end_of_lists[i].next[i]
            end_of_lists[i].next[i] = new_node
            new_node.previous[i] = end_of_lists[i]

    # Theta(lg n) -> lg n to find node and then constant to reassign pointers at most in lg n levels
    def delete(self, key_to_find):
        level = self.height
        itr = self.start
        node_found = False
        while level >= 0:
            while itr.next[level] is not None and itr.next[level].key <= key_to_find:
                itr = itr.next[level]
            if itr.key == key_to_find:
                node_found = True
                level = -1
            level -= 1
        if node_found:
            for i in range(itr.height, -1, -1):
                if itr.previous[i].key == -math.inf:
                    self.start.next[i] = itr.next[i]
                    if itr.next[i] is not None:
                        itr.next[i].previous[i] = self.start
                else:
                    itr.previous[i].next[i] = itr.next[i]
                    if itr.next[i] is not None:
                        itr.next[i].previous[i] = itr.previous[i]
                if self.start.next[i] is None:
                    self.height -= 1

    # Theta(lg n) -> lg n to find node at most
    def lookup(self, key_to_find):
        level = self.height
        itr = self.start
        node_found = False
        while level >= 0:
            while itr.next[level] is not None and itr.next[level].key <= key_to_find:
                itr = itr.next[level]
            if itr.key == key_to_find:
                node_found = True
            level -= 1
        return node_found

    def decide_levels(self):
        heads = randint(0, 1)
        count = 0
        while heads and count < self.max_levels:
            count += 1
            heads = randint(0, 1)
        return count

    def __str__(self):
        formatted_string = ""
        itr = self.start
        for i in range(self.height, -1, -1):
            formatted_string += "Level " + str(i) + ": "
            while itr.next[i] is not None:
                itr = itr.next[i]
                formatted_string += str(itr.key) + " "
            formatted_string += "\n"
            itr = self.start

        return formatted_string
