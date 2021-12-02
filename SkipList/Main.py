from random import randint
from SkipList import SkipList


def main():
    S = SkipList()

    continue_loop = True

    while continue_loop:
        selection = int(input("Please make a selection:\n(1) Insert\n(2) Delete\n(3) Lookup\n(4) Quit\nSelection -> "))
        if selection == 1:
            number = int(input("Please select a number to input: "))
            S.insert(number)
        elif selection == 2:
            number = int(input("Please select a number to delete: "))
            S.delete(number)
        elif selection == 3:
            number = int(input("Please select a number to lookup: "))
            if S.lookup(number):
                print("{} found in the skip list".format(number))
            else:
                print("{} not found in the skip list".format(number))
        else:
            continue_loop = False
        print(S)

main()