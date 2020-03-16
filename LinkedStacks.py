from ListList import *


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        return self.stack.add_head(data)

    def pop(self):
        return self.stack.rem_front()

    def peek(self):
        return self.stack.display()[-1]

    def head(self):
        return self.stack.show()
