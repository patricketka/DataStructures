class Node:
    def __init__(self, value):
        self.key = value
        self.color = None
        self.left = None
        self.right = None
        self.parent = None

    def change_color(self):
        if self.color == "red":
            self.color = "black"
        else:
            self.color = "red"

    def assign_parent(self, parent_node):
        self.parent = parent_node

    def assign_right_child(self, right_child):
        self.right = right_child

    def assign_left_child(self, left_child):
        self.left = left_child

