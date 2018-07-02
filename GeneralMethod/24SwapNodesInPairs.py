# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p1,p2 = head,head.next
        h = pre = ListNode(0)
        while p1 and p2:
            new = p2.next
            pre.next,p1.next,p2.next = p2,p2.next,p1
            pre = p1
            p1= new
            if new: p2 = new.next
        return h.next