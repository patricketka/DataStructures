class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def delete(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous

    def increase(self):
        self.value += 1

    def __str__(self):
        return "Key: " + str(self.key) + ", Value: " + str(self.value) + "\n"