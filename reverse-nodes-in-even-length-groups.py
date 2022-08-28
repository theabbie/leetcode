# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode], l=1) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        currlen = 0
        while currlen < l and curr:
            curr = curr.next
            currlen += 1
        prev = None
        curr = head
        rev = currlen % 2 == 0
        while currlen and curr:
            if rev:
                curr.next, prev, curr = prev, curr, curr.next
            else:
                prev, curr = curr, curr.next
            currlen -= 1
        if rev:
            head.next = self.reverseEvenLengthGroups(curr, l + 1)
            return prev
        prev.next = self.reverseEvenLengthGroups(curr, l + 1)
        return head