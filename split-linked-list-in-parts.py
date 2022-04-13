# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        if head:
            return 1 + self.getLength(head.next)
        return 0
    
    def getParts(self, head, lens, p):
        if not head:
            return [None]
        i = 0
        prev = None
        curr = head
        while curr and i < lens[p - 1]:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = None
        if p < len(self.op):
            self.op[p] = curr
        self.getParts(curr, lens, p + 1)
    
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.getLength(head)
        lens = [n // k] * k
        for i in range(n % k):
            lens[i] += 1
        self.op = [None] * k
        self.op[0] = head
        self.getParts(head, lens, 1)
        return self.op