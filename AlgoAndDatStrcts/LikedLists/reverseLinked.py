class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
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
    
    def reverse(self):
        # TODO
        valor = self.length
        for i in range((valor -1 ), -1, -1):
            self.append(self.get(i).value)
            print("dude")
        self.head = self.get(valor)
        return True

a = LinkedList()
for i in range(1, 6, 1):
    a.append(i)

print(a)
print(a.get(1).value)
print(a.length)
print(a.get(1).value)

a.reverse()
print(a)

# print((a.get(3).next.value))
