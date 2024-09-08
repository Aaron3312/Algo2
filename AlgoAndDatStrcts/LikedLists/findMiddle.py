
# Middle of a Singly Linked List
# Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def get(self, index):
        tempN = self.head
        for _ in range (index):
            tempN = tempN.next
        return tempN

    def find_middle(self):
        # TODO
        if self.length % 2 == 0:
            print("its even")
            return (self.get(self.length/2 + 1))
        else:
            return (self.get((self.length % 2) + (self.length / 2)))
        

