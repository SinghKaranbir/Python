class Node:
    '''
    Node class for holding node of doubly linked list
    '''

    def __init__(self, pair, next = None, prev = None):
        self.pair = pair
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "[{},{}]".format(self.pair[0], self.pair[1])

class DoublyLinkedList:
    '''
    Doubly Linked List implementation
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def delete(self, node):
        if node is self.head:
            self.head = self.head.next
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            while current:
                if current is node:
                    temp = current.prev
                    current.prev = None
                    temp.next = current.next
                    current.next.prev = temp
                    break

                current = current.next
        self.size -= 1

    def delete_last(self):
        temp = self.tail
        self.delete(self.tail)
        return temp

    def __repr__(self):
        current = self.head
        list_str = ''
        while current:
            list_str += repr(current) + '->'
            current = current.next

        return list_str
