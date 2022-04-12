# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lessThan(self, head, x):
        if not head:
            return head
        if head.val >= x:
            return self.lessThan(head.next, x)
        newhead = TreeNode(val = head.val)
        newhead.next = self.lessThan(head.next, x)
        return newhead
    
    def greaterThan(self, head, x):
        if not head:
            return head
        if head.val < x:
            return self.greaterThan(head.next, x)
        newhead = TreeNode(val = head.val)
        newhead.next = self.greaterThan(head.next, x)
        return newhead
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = self.lessThan(head, x)
        right = self.greaterThan(head, x)
        if not left:
            return right
        curr = left
        while curr and curr.next:
            curr = curr.next
        curr.next = right
        return left