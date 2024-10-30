class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

stack = Stack()
stack.push(17)
stack.push(21)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())