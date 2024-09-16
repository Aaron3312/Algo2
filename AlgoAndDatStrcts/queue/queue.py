


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else: 
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "the elemeent is inserted wuu"
    
    def dequeue(self):
        if (self.isEmpty()):
            return "theres no any element in queue"
        else:
            return self.items.pop(0)
    
    def delete(self):
        self.items = None

customQueue = Queue()
print(customQueue.isEmpty())
print(customQueue.enqueue(1))
print(customQueue.enqueue(2))
print(customQueue.enqueue(3))
print(customQueue)
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())

print(customQueue)
