class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # def __init__(self, value = 0):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head =None
        self.tail = None
        self.length = 0


    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            if temp_node.next is not self.head:
                result += str(temp_node.value)+ " -> "
            else:
                result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        index = index - 1 
        if index <= -1:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        else:
            dummy_n = self.head
            for _ in range(index):
                dummy_n = dummy_n.next
            nextDm = dummy_n.next
            dummy_n.next = new_node
            new_node.next = nextDm
        self.length += 1

    def traverCircleList(self):
        iwannakilmyself = self.head
        while iwannakilmyself is not None:
            print(iwannakilmyself.value)
            iwannakilmyself = iwannakilmyself.next
            if iwannakilmyself == self.head:
                break

    def search(self, val):
        iwannakilmyself = self.head
        while iwannakilmyself is not None:
            if iwannakilmyself.value == val:
                return True
            iwannakilmyself = iwannakilmyself.next
            if iwannakilmyself == self.head:
                return False
    def get(self, index):
        dumb = self.head
        counter = 0
        while dumb is not None:
            if counter == index:
                return dumb
            counter +=1
            dumb = dumb.next

    def setValue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def popFirst(self):
        temp = self.head
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.tail.next = self.head
        self.length -= 1
        return temp.value
    
    def pop(self):
        temp = self.tail
        tempi = self.head
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            for _ in range(self.length - 2):
                tempi = tempi.next
        tempi.next = self.head
        self.tail = tempi
        self.length -= 1
        print(tempi.value)
        return temp.value
    
    def remove(self, index):
        temp = self.head
        before = self.head
        if index == 0:
            return(self.popFirst())
        elif index == self.length:
            return(self.pop())
        else:
            for _ in range(index - 1 ):
                before = before.next
            removed = before.next
            nexted = removed.next
            before.next = nexted
            removed.next = None
            return(removed.value)


    def removeAll(self):
        if self.length == 0:
            return
        self.tail.next =None
        self.tail = None
        self.head = None
        self.length = 0
        
a = CSLinkedList()
a.prepend(33)
for i in range (1, 6 , 1):
    a.append(i)
a.append(40)
a.insert(20, 0)

print(a)
# a.traverCircleList()
print(a.search(7))
print(a.search(1))
print((a.get(5).value))
print(a.setValue(7,22))
print(a)
for i in range(0, 1):
    print(a.popFirst())
print(a.length)
print(a)
print(a.pop())
print(a)
print(a.pop())

print(a)
print(a.remove(4))
print(a)
a.removeAll()
print(a)