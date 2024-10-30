class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

queue = Queue()
queue.push(21)
queue.push(17)
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())
