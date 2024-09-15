class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    def pop(self):
        return (self.list.pop())
    def peek(self):
        if self.isEmpty():
            return "there is not any eleemnt in stack"
        else:
            return self.list[len(self.list)-1]



a = Stack()
print(a.isEmpty())

a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
print(a.isEmpty())
print(a)
print(a.pop())
print(a.peek())
