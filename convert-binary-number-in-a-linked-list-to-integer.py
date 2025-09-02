class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        val = 0
        while curr:
            val = 2 * val + curr.val
            curr = curr.next
        return val