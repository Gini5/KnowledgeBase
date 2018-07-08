# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = e = ListNode(val+1)
        e.next = head
        while e and e.next:
            if e.next.val == val:
                e.next = e.next.next
            else:
                e = e.next
        return dummy.next