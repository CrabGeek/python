
class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        try:
            self.stack.append(data)
        except:
            print("The Stack is already full")
            pass

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("The Stack is already empty")
            pass

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

