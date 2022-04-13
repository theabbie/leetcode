# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        n = 2
        curr = self.head.next
        while curr:
            isSwap = random.randrange(0, n)
            if isSwap == 0:
                res = curr.val
            curr = curr.next
            n += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()