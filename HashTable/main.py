import math
import re
import string
from HashTable import HashTable

FILE_NAME = "test.txt"
exclude = set(string.punctuation)

def read_file():
    document = open(FILE_NAME, 'r', encoding="utf8")
    words = document.read()
    document.close()
    words = re.sub(r'[^\w\s]', '', words).lower()
    return words.split()

def write_file(input):
    text_file = open("Output.txt", 'w')
    text_file.write(input.__str__())

def main():

    words = read_file()
    # exponent = math.floor(math.log2(len(words)))
    # size = 2**exponent
    hash_table = HashTable(100000)

    for word in words:
        if hash_table.find(word) is not None:
            hash_table.increase(word)
        else:
            hash_table.insert(word, 1)
    write_file(hash_table)


main()