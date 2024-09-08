# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):


    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def deleteDuplicates(self, head):
        # TODO
        list = []
        while head is not None:
            if head.val not in list:
                list.append(head.val)
                self.append(head.val)
            head = head.next
        return(self.head)
            
        
            



            

        