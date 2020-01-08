# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        hp = list()
        heapq.heapify(hp)
        d = dict()
        root = None
        cur = None
        for node in lists:
            if node:
                heapq.heappush(hp, node.val)
                if node.val in d:
                    d[node.val].append(node)
                else:
                    d[node.val] = [node]

        while hp:
            val = heapq.heappop(hp)
            t = d[val].pop()
            if t.next:
                heapq.heappush(hp, t.next.val)
                if t.next.val in d:
                    d[t.next.val].append(t.next)
                else:
                    d[t.next.val] = [t.next]
            t.next = None
            if not root:
                root = t
                cur = root
            else:
                cur.next = t
                cur = cur.next
        return root



