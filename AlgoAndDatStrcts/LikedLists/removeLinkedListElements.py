# Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):  

    def removeElements(self, head, val):
        # TODO

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        counter = 0
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
                
                
