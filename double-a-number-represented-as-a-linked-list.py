class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    
    def addTwoNumbers(self, l1, l2, carry):
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
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        head = self.addTwoNumbers(head, head, carry = 0)
        return self.reverseList(head)