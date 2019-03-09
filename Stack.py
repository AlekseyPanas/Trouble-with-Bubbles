class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def yank(self, item):
        if item in self.stack:
            self.stack.remove(item)

    def get(self):
        return self.stack