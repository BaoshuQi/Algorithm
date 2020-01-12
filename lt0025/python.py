# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = head
        grouphead = dummy
        cur = 0
        while head:
            cur += 1
            delay = head
            head = head.next
            if cur % k == 0:
                t = p
                tmp = p.next
                p.next = head
                grouphead.next = delay
                while tmp != head:
                    last = p
                    p = tmp
                    tmp = p.next
                    p.next = last
                grouphead = t
                p = t.next
        return dummy.next