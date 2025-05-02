class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove_from_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def remove_from_end(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')
