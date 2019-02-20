def reverseList(self, head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def reverse(head):
    prev = None

    while head:
        nex = head.next
        head.next = prev
        prev = head
        head = nex
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

def hasCycle(self, head):
    if not head:
        return False
    walker = head
    runner = head.next
    try:
        while walker != runner:
            walker = walker.next
            runner = runner.next.next
        return True
    except:
        return False

def removeElements(self, head, val):
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    while cur:
        while cur.next and cur.next.val == val:
            cur.next = cur.next.next
        cur = cur.next
    return dummy.next

def isPalindrome(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt

    while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True