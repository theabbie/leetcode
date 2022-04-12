# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deldup(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.val in self.dups or (head.next and head.val == head.next.val):
            self.dups.add(head.val)
            head = self.deldup(head.next)
        else:
            head.next = self.deldup(head.next)
        return head
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dups = set()
        head = self.deldup(head)
        return head