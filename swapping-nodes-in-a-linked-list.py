class Solution:
    def lenList(self, head, a, k):
        if head:
            curr = 1 + self.lenList(head.next, a + 1, k)
            if a == k:
                self.a = head
            if curr == k:
                self.b = head
            return curr
        return 0
    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.lenList(head, 1, k)
        self.a.val, self.b.val = self.b.val, self.a.val
        return head