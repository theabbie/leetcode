class Solution:
    def getList(self, head, rem, i):
        if not head:
            return head
        if i % 2 != rem:
            return self.getList(head.next, rem, i + 1)
        newhead = TreeNode(val = head.val)
        newhead.next = self.getList(head.next, rem, i + 1)
        return newhead
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = self.getList(head, 1, 1)
        right = self.getList(head, 0, 1)
        if not left:
            return right
        curr = left
        while curr and curr.next:
            curr = curr.next
        curr.next = right
        return left