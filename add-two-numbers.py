# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            currval = l1val + l2val + carry
            curr = ListNode(val = currval % 10)
            curr.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry = currval // 10)
            return curr
        else:
            if carry > 0:
                return ListNode(val = carry)
            return None