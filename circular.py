class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert(self, data):
        new_node = CNode(data)
        if self.tail is None:
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, key):
        if self.tail is None:
            raise Exception("List is empty")

        current = self.tail.next
        prev = self.tail
        while True:
            if current.data == key:
                if current == self.tail and current.next == self.tail:
                    self.tail = None  # only one node
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                return
            prev = current
            current = current.next
            if current == self.tail.next:
                break
        raise ValueError("Element not found")

    def search(self, key):
        if self.tail is None:
            return None
        current = self.tail.next
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.tail.next:
                break
        return None

    def display(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail.next
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.tail.next:
                break
        print("(back to head)")
