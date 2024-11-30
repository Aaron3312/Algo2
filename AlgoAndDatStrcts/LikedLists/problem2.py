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
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range (index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1 
        return True
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    def get(self, index):
        current = self.head
        for _ in range(index ):
            current = current.next
        return current
    
    def set(self, index, value):
        current = self.head
        if index < 0 or index > self.length:
            return False
        else:

            for _ in range(index):
                current = current.next
            current.value = value
            return True
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value

    def pop(self):
        popped_node = self.tail
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        rets = temp.next
        temp.next = None
        return rets.value
    
    def remove(self, index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        next_node = popped_node.next
        prev_node.next = next_node
        return popped_node.value
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = None

def thingOfWork(LinkedList1, LinkedList2):
    #print(LinkedList1.length)
    listBasure = []
    for i in range(LinkedList1.length -1, -1, -1):
        #print(i)
        #print(List1.get(i).value)
        listBasure.append(List1.get(i).value)
    #print(listBasure)
    for i in range(LinkedList2.length):
        listBasure[i] = listBasure[i] + List2.get(i).value
    #print(listBasure)
    listaSalida = LinkedList()
    for i in range(LinkedList1.length):
        listaSalida.prepend(listBasure[i])
    return listaSalida

List1 = LinkedList()
List2 = LinkedList()

List1.append(0)
List1.append(2)
List1.append(3)
List1.append(3)


List2.append(4)
List2.append(5)
List2.append(6)
List2.append(6)


print(List1)
print(List2)
print(thingOfWork(List1,List2))

