class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_from_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        self.head = self.head.next

    def remove_from_position(self, pos):
        if self.head is None:
            raise Exception("List is empty")
        if pos == 0:
            self.remove_from_beginning()
            return
        current = self.head
        for _ in range(pos - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        current.next = current.next.next if current.next else None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
