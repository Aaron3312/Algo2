# Remove Duplicates from a Singly Linked List
# Given a singly linked list, write a function that removes all the duplicates. use this linked list .

# Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

# Result Linked List - "1 -> 2 -> 4 -> 3



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
    
    def removeIndex(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == (self.length ):
            self.tail = self.get(index)
            self.get(index).next = None
            self.length -= 1

        else:
            before = self.get(index - 1)
            removed = before.next
            after = removed.next
            before.next = after
            self.length -= 1
            

    def remove_duplicates(self):
        # TODO
        s = []
        remove = []
        for i in range(0, self.length):
            if (self.get(i).value) not in s: 
                s.append(self.get(i).value)
                remove.append(i)
        
        count = 0
        f = []
        for i in range(0, self.length ):
            if i not in remove:
                count += 1
                f. append (i)
        f.reverse()
        for i in f:
            self.removeIndex(i)

        


a = LinkedList()
for i in range(1, 6, 1):
    a.append(i)
    a.append(i)
    a.append(i)
    a.append(i)
    a.append(i)


    
for i in range(1, 6, 1):
    a.append(i)
    a.append(i+23)


a.remove_duplicates()
print(a)