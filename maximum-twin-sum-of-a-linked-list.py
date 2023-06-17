class Solution:
    def lenList(self, head):
        if head:
            return 1 + self.lenList(head.next)
        return 0
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = {}
        n = self.lenList(head)
        curr = head
        i = 0
        while curr:
            key = min(i, n - i - 1)
            sums[key] = sums.get(key, 0) + curr.val
            curr = curr.next
            i += 1
        return max(sums.values())