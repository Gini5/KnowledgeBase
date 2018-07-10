class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next

        start = reverse = prev.next
        new = None
        for i in range(n - m + 1):
            cur = reverse
            reverse = reverse.next
            cur.next = new
            new = cur

        prev.next = new
        start.next = reverse

        return dummy.next