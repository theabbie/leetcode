class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            total = 0
            curr = head
            while curr:
                total += curr.val
                if total == 0:
                    return self.removeZeroSumSublists(curr.next)
                curr = curr.next
            head.next = self.removeZeroSumSublists(head.next)
        return head