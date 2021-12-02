class Node:
    def __init__(self, key, levels):
        self.key = key
        self.height = levels
        self.next = [None] * (levels + 1)
        self.previous = [None] * (levels + 1)
