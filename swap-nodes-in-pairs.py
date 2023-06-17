class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(head.next.next)
        newhead.next = head
        return newhead