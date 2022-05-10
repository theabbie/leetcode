# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            a, b = l1, l2
            if b.val < a.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
            return a
        return l1 or l2