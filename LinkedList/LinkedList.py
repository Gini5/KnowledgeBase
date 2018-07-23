def reverseList(self, head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def reverse(head):
    prev = None
    current = head

    while current:
        nex = current.next
        current.next = prev
        prev = current
        current = nex
    return prev


def deleteDuplicates(self, head):
    if not head: return head
    res = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return res