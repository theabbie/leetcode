# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        n = 1
        while curr and curr.next:
            curr = curr.next
            n += 1
        k = k % n
        curr.next = head
        curr = head
        for i in range(n - k - 1):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head