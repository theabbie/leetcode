# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head = head.next
        curr = head
        total = 0
        while curr:
            total += curr.val
            if curr.val == 0:
                head = ListNode(val = total)
                head.next = self.mergeNodes(curr)
                return head
            curr = curr.next