from node import Node
from Color import Color

COUNT = [5]


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = Color.black
        self.root = self.nil
        self.nodes = 0

    # Theta(lg n) -> lg n to find spot where node should be inserted and then pointer reassignment
    def insert(self, number):
        self.nodes += 1
        new_node = Node(number)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == self.nil:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = Color.red
        self.insert_fixup(new_node)

    # O(lg n) since at worst you move from bottom up to root (height of tree when is O(lg n))
    def insert_fixup(self, z):
        while z.parent.color == Color.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                # Case 1
                if y.color == Color.red:
                    z.parent.color = Color.black
                    y.color = Color.black
                    z.parent.parent.color = Color.red
                    z = z.parent.parent
                # Case 2
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                # Case 3
                else:
                    z.parent.color = Color.black
                    z.parent.parent.color = Color.red
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                # Case 1
                if y.color == Color.red:
                    z.parent.color = Color.black
                    y.color = Color.black
                    z.parent.parent.color = Color.red
                    z = z.parent.parent
                # Case 2
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                # Case 3
                else:
                    z.parent.color = Color.black
                    z.parent.parent.color = Color.red
                    self.left_rotate(z.parent.parent)
        self.root.color = Color.black

    # Constant
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Constant
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            y.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    # Theta(lg n)
    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    # Theta(lg n)
    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    # Theta(lg n)
    def search(self, x, k):
        if k == x.key:
            return True
        if x == self.nil:
            return False
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    # Theta(lg n)
    def find_node(self, x, k):
        if k == x.key:
            return x
        if x == self.nil:
            return None
        if k < x.key:
            return self.find_node(x.left, k)
        else:
            return self.find_node(x.right, k)

    #Theta(lg n)
    def successor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    #Theta(lg n)
    def predecessor(self, x):
        if x.left != self.nil:
            return self.maximum(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    # constant
    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Theta (lg n)
    def delete(self, number):
        z = self.find_node(self.root, number)
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            if y_original_color == Color.black:
                self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.nil and x.color == Color.black:
            if x == x.parent.left:
                w = x.parent.right
                # Case 1
                if w.color == Color.red:
                    w.color = Color.black
                    x.parent.color = Color.red
                    self.left_rotate(x.parent)
                    w = x.parent.right
                # Case 2
                if w.left.color == Color.black and w.right.color == Color.black:
                    w.color = Color.red
                    x = x.parent
                # Case 3
                elif w.right.color == Color.black:
                    w.left.color = Color.black
                    w.color = Color.red
                    self.right_rotate(w)
                    w = x.parent.right
                # Case 4
                else:
                    w.color = x.parent.color
                    x.parent.color = Color.black
                    w.right.color = Color.black
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                # Case 1
                if w.color == Color.red:
                    w.color = Color.black
                    x.parent.color = Color.red
                    self.right_rotate(x.parent)
                    w = x.parent.left
                # Case 2
                if w.right.color == Color.black and w.left.color == Color.black:
                    w.color = Color.red
                    x = x.parent
                # Case 3
                elif w.left.color == Color.black:
                    w.right.color = Color.black
                    w.color = Color.red
                    self.left_rotate(w)
                    w = x.parent.left
                # Case 4
                else:
                    w.color = x.parent.color
                    x.parent.color = Color.black
                    w.left.color = Color.black
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = Color.black

    def print_nodes(self, x):
        if x.left != self.nil:
            self.print_node_helper(x.left)
        print(x.key)
        if x.right != self.nil:
            self.print_node_helper(x.right)

    def print_node_helper(self, x):
        if x.left != self.nil:
            self.print_node_helper(x.left)
        print(x.key)
        if x.right != self.nil:
            self.print_node_helper(x.right)

    def height(self, node):
        if node == self.nil:
            return -1
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
