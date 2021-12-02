import math

from RedBlackTree import RedBlackTree
from node import Node
from CreateNumbers import create_numbers, get_numbers, create_numbers_simple
from math import *

n = 1000


def main():

    T = RedBlackTree()
    create_numbers_simple(n)
    number_list = get_numbers()
    for i in range(len(number_list)-1):
        T.insert(int(number_list[i]))

    continue_loop = True

    while continue_loop:
        selection = int(input("Please make a selection:\n(1) Sort\n(2) Search\n(3) Minimum\n(4) Maximum\n(5) Sucessor\n(6) Predecessor\n(7) Insert\n(8) Delete"
                              "\n(9) Quit\nSelection -> "))
        if selection == 1:
            T.print_nodes(T.root)
        elif selection == 2:
            number = int(input("Please select a number to search for: "))
            if T.search(T.root, number):
                print("{} found in the tree".format(number))
            else:
                print("{} not found in the tree".format(number))
        elif selection == 3:
            print(T.minimum(T.root).key)
        elif selection == 4:
            print(T.maximum(T.root).key)
        elif selection == 5:
            number = int(input("Please select a number to find the successor to: "))
            if T.search(T.root, number):
                node = T.find_node(T.root, number)
                print(T.successor(node).key)
            else:
                print("{} not found in the tree".format(number))
        elif selection == 6:
            number = int(input("Please select a number to find the predecessor to: "))
            if T.search(T.root, number):
                print(T.predecessor(T.find_node(T.root, number)).key)
            else:
                print("{} not found in the tree".format(number))
        elif selection == 7:
            number = int(input("Please select a number to insert: "))
            T.insert(number)
        elif selection == 8:
            number = int(input("Please select a number to delete: "))
            T.delete(number)
        else:
            continue_loop = False
        print("Tree Height: {}".format(T.height(T.root)))
        print("Height upper bound: {}".format(int(2 * math.log2(T.nodes + 1))))
        print("\n")

if __name__ == '__main__':
    main()
