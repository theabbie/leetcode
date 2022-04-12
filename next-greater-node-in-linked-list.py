# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        curr = head
        greater = {}
        vals = {}
        i = 0
        while curr:
            vals[i] = curr.val
            while len(stack) > 0 and curr.val > vals[stack[-1]]:
                popped = stack.pop()
                greater[popped] = curr.val
            stack.append(i)
            curr = curr.next
            i += 1
        return [greater.get(j, 0) for j in range(i)]