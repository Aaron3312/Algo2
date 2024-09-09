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


        
a = CSLinkedList()
a.prepend(33)
for i in range (1, 6 , 1):
    a.append(i)
a.append(40)
a.insert(20, 0)

print(a)
a.traverCircleList()


