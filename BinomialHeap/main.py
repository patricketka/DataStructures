from BinomialHeap import BinomialHeap

n = 10


def main():
    H = BinomialHeap()
    for i in range(n):
        H.insert(i)
    H.print()


main()
