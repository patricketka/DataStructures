import math

from Node import Node


def make_binomial_heap():
    return BinomialHeap()


def merge_heap(new_heap, heap1, heap2):
    x = heap1.head
    y = heap2.head
    z = new_heap.head
    while x is not None or y is not None:
        if y is None:
            if z is None:
                x.previous = z
                new_heap.head = x
                z = x
            else:
                z.sibling = x
                x.previous = z
                z = z.sibling
            x = x.sibling
        elif x is None:
            if z is None:
                y.previous = z
                new_heap.head = y
                z = y
            else:
                z.sibling = y
                y.previous = z
                z = z.sibling
            y = y.sibling
        else:
            if x.degree <= y.degree:
                if z is None:
                    x.previous = z
                    new_heap.head = x
                    z = x
                else:
                    z.sibling = x
                    x.previous = z
                    z = z.sibling
                x = x.sibling
            else:
                if z is None:
                    y.previous = z
                    new_heap.head = y
                    z = y
                else:
                    z.sibling = y
                    y.previous = z
                    z = z.sibling
                y = y.sibling


def link(y, z):
    y.parent = z
    y.sibling = z.child
    y.previous = None
    if z.child is not None:
        z.child.previous = y
    z.child = y
    z.degree += 1


def union(heap1, heap2):
    new_heap = make_binomial_heap()
    merge_heap(new_heap, heap1, heap2)
    if new_heap.head is None:
        return new_heap
    prev_x = None
    x = new_heap.head
    next_x = x.sibling
    while next_x is not None:
        if x.degree != next_x.degree or (next_x.sibling is not None and next_x.sibling.degree == x.degree):
            prev_x = x
            x = next_x
        else:
            if x.key <= next_x.key:
                x.sibling = next_x.sibling
                link(next_x, x)
            else:
                next_x.previous = x.previous
                if prev_x is None:
                    new_heap.head = next_x
                else:
                    prev_x.sibling = next_x
                link(x, next_x)
                x = next_x
        next_x = x.sibling
    return new_heap


class BinomialHeap:
    def __init__(self):
        self.head = None

    def insert(self, key):
        temp = Node(key)
        new_heap = make_binomial_heap()
        new_heap.head = temp
        new_heap = union(self, new_heap)
        self.head = new_heap.head
        return temp

    def minimum(self):
        y = None
        x = self.head
        min_value = math.inf
        while x is not None:
            if x.key < min_value:
                min_value = x.key
                y = x
            x = x.sibling
        return y

    def extract_minimum(self):
        min_node = self.minimum()
        if min_node.previous is not None:
            min_node.previous.sibling = min_node.sibling
        else:
            self.head = min_node.sibling
        if min_node.sibling is not None:
            min_node.sibling.previous = min_node.previous
        new_heap = make_binomial_heap()
        node_stack = []
        stack_top = -1
        x = min_node.child
        while x is not None:
            node_stack.append(x)
            stack_top += 1
            x = x.sibling
        y = None
        if stack_top > -1:
            y = node_stack[stack_top]
            y.parent = None
            y.previous = None
            new_heap.head = y
            stack_top -= 1
        while stack_top >= 0:
            z = node_stack[stack_top]
            z.parent = None
            z.previous = y
            y.sibling = z
            z.sibling = None
            y = z
            stack_top -= 1
        new_heap = union(self, new_heap)
        self.head = new_heap.head

    def decrease_key(self, x, k):
        if k > x.key:
            return
        x.key = k
        y = x
        z = y.parent
        while z is not None and y.key < z.key:
            temp_key = z.key
            z.key = y.key
            y.key = temp_key
            y = z
            z = y.parent

    def delete(self, x):
        self.decrease_key(x, -math.inf)
        self.extract_minimum()

    def print(self):
        x = self.head
        x.print(0)
