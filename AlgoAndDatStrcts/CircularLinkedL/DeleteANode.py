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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        # TODO
        temp = self.head
        prev = Node(0)
        prev.next = self.head
        if self.length == 0:
            return False
        else:
            while temp is not None:
                if temp.value == value:
                    if temp == self.head:
                        self.tail.next = temp.next
                        self.head = temp.next
                        temp.next = None
                        
                        break
                    elif temp == self.tail:
                        prev.next = self.head
                        temp.next = None
                        self.tail = prev
                    else:
                        prev.next = temp.next
                        temp.next = None
                        
                if temp.next == self.head:
                    return False
                temp = temp.next
                prev = prev.next
            self.length -= 1

            return True
