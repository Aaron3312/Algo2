from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    



class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__ (self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


def remove_duplicates(ll):
    if ll.head is None:
        return
    

    valores_vistos = set()
    temp = ll.head
    valores_vistos.add(temp.value)
    while temp.next:
        if temp.next.value in valores_vistos:
            temp.next = temp.next.next
        else:
            valores_vistos.add(temp.next.value)
            temp = temp.next
    return ll
    
def return_nthFromLast(ll, num):
    if ll.head is None:
        return None
    temp = ll.head
    counter = len(ll)
    nIndex = counter - num 
    for _ in range(nIndex):
        temp = temp.next
    return temp

def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

def sumList(ll, ll2):
    list1 = []
    list2 = []
    n1 = ll.head
    n2 = ll2.head
    carry = 0
    counts = 0
    lls = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        print(result)
        lls.add(int(result % 10))
        print("llsadd")
        print(int(result % 10))
        carry = result / 10
        print("carry")
        print(carry)
    return lls

def sumList1(ll, ll2):
    list1 = []
    list2 = []
    n1 = ll.head
    n2 = ll2.head
    carry = 0
    carry2 = 0
    counts = 0
    lls = LinkedList()
    while n1 or n2:
        result1 = carry
        result2 = carry
        if n1:
            result1 += n1.value
            list1.append(n1.value)
            n1 = n1.next
        if n2:
            result2 += n2.value
            list2.append(n2.value)
            n2 = n2.next
        counts += 1
    
    for i in range(counts, 0, -1):
        a = list1.pop()
        b = list2.pop()
        if i == 0:
            a = a
            b = b
        else:
            a = a * (10 ** (i - 1))
            b = b * (10 ** (i - 1))
            carry += a
        carry2 += b
    carry2 = carry2 + carry
    print(carry2)
    b = 0
    counts += 1

    if carry2 >= 1000:
        counts += 1

    for i in range(1, counts, +1):
    
        a = ((carry2 % (10 ** i) )// (10 ** (i-1)))
        print (a)
        lls.add(a)
    
    return lls


def interseccion(ll,ll2):
    temp1 = ll.head
    temp2 = ll2.head
    if ll.tail is not ll2.tail:
        print("no misma cola")
        return False
    if len(ll) > len(ll2):
        for i in range(len(ll) - len(ll2)):
            temp1 = temp1.next
            print("mas")
    elif len(ll) < len(ll2):
        for i in range(len(ll2) - len(ll)):
            temp2 = temp2.next
            print("menos")
    
    for _ in range(len(ll)):
        if temp2 == temp1:
            return temp2
        temp2 = temp2.next
        temp1 = temp1.next
    return False

def intersequen(ll, ll2):
    temp = ll.head
    temp2 = ll2.head
    temp2 = temp2.next
    temp = temp.next
    temp = temp.next
    temp = temp.next

    temp.next = temp2


    ll.tail = ll2.tail

    



customLL = LinkedList()
customLL2 = LinkedList()
customLL.generate(5, 0, 9)
customLL2.generate(5, 0, 9)
print(customLL)
# print(len(customLL))
# print(return_nthFromLast(customLL, 0))
# print(partition(customLL, 50))
print(customLL2)
intersequen(customLL,customLL2)

print(customLL)
print(interseccion(customLL,customLL2))

