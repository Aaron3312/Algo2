class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp is not self.tail:
                result += " <-> "
            temp = temp.next
            if temp == self.head:
                return result


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def reverseTraversal(self):
        temp = self.tail
        while temp is not None:
            print (temp.value)
            temp = temp.prev
            if temp == self.tail:
                break
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def get(self, index):
        if index >= (self.length//2):
            temp = self.tail
            counter = self.length -1
            print("indexMayortail")
            for _ in range(self.length):
                if counter == index:
                    return temp
                temp= temp.prev
                counter -= 1

        elif index < (self.length//2):
            temp = self.head
            counter = 0
            print("indexmenorHead")
            for _ in range(self.length):
                if counter == index:
                    return temp
                temp= temp.next
                counter += 1

    def set(self, index, value):
        if index >= (self.length//2):
            temp = self.tail
            counter = self.length -1
            for _ in range(self.length):
                if counter == index:
                    temp.value = value
                    return True
                temp = temp.prev
                counter -= 1
        if index <= (self.length//2):
            temp = self.head
            counter = 0              
            for _ in range(self.length):
                if counter == index:
                    temp.value = value
                    print("lesser")
                    return True
                temp = temp.next
                counter += 1
        return False
    
    def insert(self, index, value):
        temp = self.get(index-1)
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
            new_node.next.prev = new_node
            self.length += 1

    def popFirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.tail.next = temp.next
            self.head = temp.next
            self.head.prev = self.tail
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail.prev.next = self.head
            self.tail = self.tail.prev
            self.head.prev = self.tail
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def remove(self, index):
        if self.length == 0:
            return None
        if index == self.length -1:
            return (self.pop())
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -=1
        return temp


    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0





c = CircularDoublyLinkedList()

c.append(2232)
c.append(202)
c.append(272)
c.append(242)
c.append(12)
c.prepend(32)
print(c.get(4).value)
print(c)
c.insert(2,223)
print(c.set(1,22))
c.insert(7, 454)
print(c.length)
print(c.popFirst())
print(c.tail.next.value)
print(c)

print(c.pop())
print(c.remove(4))

print(c)
