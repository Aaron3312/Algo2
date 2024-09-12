class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class CDList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result +=" <-> "
            temp = temp.next
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def reverseTraversal(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def search(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def get(self, index):
        if index > (self.length //2):
            print("indexMayor")
            temp = self.tail
            counter = (self.length -1)
            while temp is not None:
                if counter == index:
                    return temp
                else:
                    temp = temp.prev
                    counter -= 1
        else:
            temp = self.head
            counter = 0
            while temp is not None:
                if counter == index:
                    return temp
                else:
                    temp = temp.next
                    counter += 1

    def set(self, index, value):
        temp = self.head
        for i in range(index):
            temp = temp.next
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        temp = self.head
        if index == (self.length):
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            for i in range(index -1 ):
                temp = temp.next
            print("other")
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1

    def popFirst(self):
        temp = self.head
        if not self.head:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def pop(self):
        temp = self.tail
        if not self.head:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    
    def remove(self, index):
        temp = self.get(index)
        if not temp:
            return False
        else:
            if index == 0:
                return (self.popFirst())
            elif index == (self.length - 1):
                return (self.pop())
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                self.length -= 1
                return temp

        




new_node = Node(10)
c = CDList()

c.append(110)
c.append(13220)
c.append(1320)
c.append(1023)
c.append(22)
c.prepend(223)
c.popFirst()


print(c.get(3))
print(c.set(2 , 222))
c.insert(1, 12)
print(c)

print(c)