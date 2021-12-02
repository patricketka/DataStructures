class Node:
    def __init__(self, key):
        self.parent = None
        self.key = key
        self.degree = 0
        self.child = None
        self.sibling = None
        self.previous = None

    def print(self, levels):
        for i in range(levels):
            print("\t", end="")
        print("Key: ", self.key, " Degree: ", self.degree, "\n")
        if self.child is not None:
            self.child.print(levels + 1)
        if self.sibling is not None:
            self.sibling.print(levels)

