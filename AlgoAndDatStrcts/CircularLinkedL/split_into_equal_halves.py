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

    def split_list(self):
        # TODO
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        temp = self.head
        if self.length == 0:
            return first_list, second_list

        else:
            if self.length % 2 == 0:
                for i in range((self.length // 2)):
                    first_list.append(temp.value)
                    temp = temp.next
                for i in range(self.length //2):
                    second_list.append(temp.value)
                    temp = temp.next  
            else:
                for i in range((self.length // 2) + 1):
                    first_list.append(temp.value)
                    temp = temp.next
                for i in range(self.length //2):
                    second_list.append(temp.value)
                    temp = temp.next                  
        return first_list, second_list


a = CSLinkedList()
for i in range (1, 7 , 1):
    a.append(i)
a.append(40)
print(a.length)
print(a)
b, c = (a.split_list())
print("b")
print(b)
print("c")
print(c)