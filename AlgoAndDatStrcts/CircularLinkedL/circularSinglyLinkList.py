class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        # TODO
        temp = self.head
        regresa = ""
        while temp is not None:
            if temp == self.tail:
                regresa += str(temp.value)
            else:
                regresa += str(temp.value) + " -> "
            temp = temp.next
            if temp == self.head:
                return regresa
        
    
    def append(self, value):
        # TODO
        new_node = Node(value)
        temp = self.head
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            while temp.next != None:
                if temp.next == self.head:
                    break
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # TODO
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
            self.tail.next = self.head
        self.length += 1
            



a = CSLinkedList()
a.append(2)
a.append(3)
a.prepend(32)
a.append(3)
a.append(3)


print(a)