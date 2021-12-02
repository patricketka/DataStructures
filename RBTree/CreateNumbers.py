import math
from random import randint


def create_numbers_simple(count):
    try:
        numbers = open('randomNumbers.txt', 'w')
    except IOError:
        print("Error unable to create")
    else:
        for i in range(count):
            numbers.write(i.__str__() + ", ")
        numbers.close()


def create_numbers(count):
    try:
        numbers = open('randomNumbers.txt', 'w')
    except IOError:
        print("Error unable to create")
    else:
        number_set = set()
        for i in range(count):
            x = randint(1, 1000000)
            number_set.add(x)
        for number in number_set:
            temp = number.__str__() + ", "
            numbers.write(temp)
        numbers.close()


def get_numbers():
    try:
        numbers = open('randomNumbers.txt', 'r')
    except IOError:
        print("Error unable to create")
    else:
        number_chain = numbers.read()
        number_list = number_chain.split(", ")
        numbers.close()

    return number_list
