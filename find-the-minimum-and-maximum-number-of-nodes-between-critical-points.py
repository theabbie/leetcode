# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isCritical(self, curr, prev, forw):
        if curr.val > prev.val and curr.val > forw.val:
            return True
        if curr.val < prev.val and curr.val < forw.val:
            return True
        return False
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []
        prev = None
        curr = head
        i = 0
        while curr and curr.next:
            if prev and self.isCritical(curr, prev, curr.next):
                critical.append(i)
            prev = curr
            curr = curr.next
            i += 1
        if len(critical) >= 2:
            k = len(critical)
            return [min(critical[i+1] - critical[i] for i in range(k - 1)), critical[-1] - critical[0]]
        return [-1, -1]