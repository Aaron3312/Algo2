class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            if temp_node.next is not self.head:
                result += str(temp_node.data)+ " -> "
            else:
                result += str(temp_node.data)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return result

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
            # TODO
            temp = self.head
            new_node = Node(0)
            new_node.next = self.head
            prev = new_node
            counter = 0
            lps = []


            while temp is not None:
                lps.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
                counter += 1

            while temp is not None:
                if counter == 1 or counter == 0:
                    return True
         
                temp = temp.next
                if temp == self.head:
                    break
            ad = lps[:]
            ad.sort()
            print(ad, lps)
            if lps == ad:
                return True
            else:
                return False

a = CircularLinkedList()
for i in range (1, 3 , 1):
    a.append(i +23)
a.append(233)
print(a)
print(a.is_sorted())
