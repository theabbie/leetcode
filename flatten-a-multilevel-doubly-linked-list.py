"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            curr = head
            while curr:
                tmp = curr.next
                if curr.child:
                    curr.next = self.flatten(curr.child)
                    if curr.next:
                        curr.next.prev = curr
                    curr.child = None
                    ccurr = curr.next
                    while ccurr and ccurr.next:
                        ccurr = ccurr.next
                    ccurr.next = tmp
                    if tmp:
                        tmp.prev = ccurr
                curr = tmp
        return head