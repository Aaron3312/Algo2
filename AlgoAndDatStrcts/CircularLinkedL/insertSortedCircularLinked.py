class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        prepend = Node(0)
        prepend.next = self.head
        temp = self.head
        new_node = Node(data)
        if temp == None:
            print("what" + str(data))
            self.prepend(data)
            return
        if data <= self.head.data:
            self.prepend(data)
            print("counter 0 " + str(data))
        else:
            temp = self.head
            while temp.next != self.head and temp.next.data < data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            
            print("tempD " + str(temp.data))
            print("paso " + str(data))



    def print_list(self):
        if not self.head:
            print("La lista está vacía")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break


# Prueba del código
cll = CircularLinkedList()

# Insertar algunos nodos en la lista de forma ordenada

cll.insert_into_sorted(10)
cll.insert_into_sorted(5)
cll.insert_into_sorted(52)
cll.insert_into_sorted(20)


print("lista")
# Imprimir la lista
cll.print_list()