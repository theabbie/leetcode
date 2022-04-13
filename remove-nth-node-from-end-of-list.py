# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(h, n):
            if not h.next:
                return 1
            l = 1 + getLength(h.next, n)
            if l == n + 1:
                h.next = h.next.next
            return l
        tmp = getLength(head, n)
        if tmp == n:
            head = head.next
        return head