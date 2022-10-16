class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        prev = slow
        fast = head
        n = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            n += 1
        if n == 0:
            return None
        prev.next = slow.next
        return head