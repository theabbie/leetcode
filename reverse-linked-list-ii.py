class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        stack = []
        i = 1
        while curr:
            if left <= i <= right:
                stack.append(curr.val)
            curr = curr.next
            i += 1
        curr = head
        i = 1
        while curr:
            if left <= i <= right:
                curr.val = stack.pop()
            curr = curr.next
            i += 1
        return head