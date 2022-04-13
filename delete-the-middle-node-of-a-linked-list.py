# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        prev = slow
        fast = head
        n = 0
        while fast and fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            n += 2
        if fast and fast.next:
            n += 1
        if n == 0:
            return None
        if n % 2 == 0:
            prev.next = slow.next
        else:
            slow.next = slow.next.next
        return head