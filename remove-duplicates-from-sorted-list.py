# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next and head.val == head.next.val:
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head