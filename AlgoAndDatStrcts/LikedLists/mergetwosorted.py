# Merge Two Sorted Linked List
# You are given the heads of two sorted linked lists list1 and list2. 

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.   

# Example 1: 

# Input: list1 = [1,2,4], list2 = [1,3,4]

# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []

# Output: []

# Example 3: 

# Input: list1 = [], list2 = [0]

# Output: [0]



# Constraints: 

# The number of nodes in both lists is in the range [0, 50].

# -100 <= Node.val <= 100

# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

       
class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def countList(self, l1, l2):
        l1_head = l1.head
        l2_head = l2.head
        count = 0
        while l1_head is not None:
            l1_head = l1_head.next
            count += 1
        while l2_head is not None:
            l2_head = l2_head.next
            count += 1
        print(count)
        return(count)
    
    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1        

    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_h = l1.head
        l2_h = l2.head
        count = (self.countList(l1, l2))
        print(l1_h.val)
        print("dead" + str(l2_h.val))
        if count == 0:
            print("length = 0")
            return
        else:
            for i in range(count):
                if l1_h is None or l2_h is None:
                    break
                if l1_h.val > l2_h.val:
                    self.append(l2_h.val)
                    l2_h = l2_h.next  # Avanza al siguiente nodo
                else:
                    self.append(l1_h.val)
                    l1_h = l1_h.next  # Avanza al siguiente nodo
            if count != self.length:
                if l1_h is None:
                    while l2_h is not None:
                        self.append(l2_h.val)
                        l2_h = l2_h.next  # Avanza al siguiente nodo
                if l2_h is None:
                    while l1_h is not None:
                        self.append(l1_h.val)
                        l1_h = l1_h.next  # Avanza al siguiente nodo

    

a = LinkedList()
for i in range(1, 6, 1):
    a.append(i+32)

b = LinkedList()    
for i in range(1, 6, 1):
    b.append(i+32)

print(a)
print(b)
s = Solution()
s.mergeTwoLists(a,b)
print(s)
print(s.length)


