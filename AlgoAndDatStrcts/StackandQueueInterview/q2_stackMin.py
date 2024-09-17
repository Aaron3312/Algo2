class Node:
    def __init__(self, value = None, next = None):
        self.next = next
        self.value = value
        self.prev = None
    
    def __str__(self):
        return str(self.value)

    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
        self.minVal= 100000

    def __iter__(self):
            curNode = self.head
            while curNode:
                yield curNode
                curNode = curNode.next


            
class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        return False
    
    def push(self,value):
        new_node = Node(value)
        if self.LinkedList.minVal == 100000:
            self.LinkedList.minVal = new_node
        elif self.LinkedList.minVal > value:
            self.LinkedList.minVal.next = new_node
         
        if self.LinkedList.head == None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            s = self.LinkedList.tail
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node
            self.LinkedList.tail.prev = s
        self.LinkedList.lenght += 1
    
    def pop(self):
        temp = self.LinkedList.tail
        if self.LinkedList.lenght == 1:
            print(temp)
            print("dude")
            self.LinkedList.head = None
            self.LinkedList.tail = None
            self.LinkedList.length = 0
            return temp
        elif not temp:
            print("wtf")
            self.LinkedList.head = None
            self.LinkedList.tail = None
            self.LinkedList.length = 0
            return None
        else:
            print(temp)
            self.LinkedList.tail = temp.prev
            self.LinkedList.tail.next = None
            self.LinkedList.lenght -= 1
            return temp
        
    def min(self):
        if not self.LinkedList.minVal:
            return None
        return self.minNode.value
    




stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
stack.pop()
stack.pop()
stack.pop()

print("kill yourself " + str(stack))
