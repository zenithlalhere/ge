class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", self.items)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:", q.dequeue())
q.display()
