class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = None
        while head:
            cur = head
            head = head.next
            cur.next = new
            new = cur
            # easy version: head.next, new, head= new, head, head.next
        return new

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next, n2.next, n3.next = n2, n3, n4
t = Solution()
print(t.reverseList(n1))