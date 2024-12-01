#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def insert(self, index, data):
        nodIn = Node(data)
        temp = self.head
        if index >= 0 and index <= self.length:
            if index == 0:
                self.head = nodIn
                nodIn.next = temp
                self.length += 1
                return True
            else:
                beftem = temp
                for _ in range(index):
                    beftem = temp
                    temp = temp.next
                if index == self.length :
                    self.tail.next = nodIn
                    self.tail = nodIn
                else:       
                    beftem.next = nodIn
                    nodIn.next = temp
                self.length += 1
                return True
        else:
            return False
        

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.push(10))  # Success
print(singlyLinkedList.push(15))  # Success
print(singlyLinkedList.push(20))  # Success

print(singlyLinkedList.insert(2, 12))  # True
print(singlyLinkedList.insert(100, 12))  # False
print(singlyLinkedList.length)  # 5
print(singlyLinkedList.head.val)  # 5
print(singlyLinkedList.head.next.val)  # 10
print(singlyLinkedList.head.next.next.val)  # 12
print(singlyLinkedList.head.next.next.next.val)  # 15
print(singlyLinkedList.head.next.next.next.next.val)  # 20

print(singlyLinkedList.insert(5, 25))  # True
print(singlyLinkedList.length)  # 5
print(singlyLinkedList.head.next.next.next.next.next.val)  # 25
print(singlyLinkedList.tail.val)  # 25