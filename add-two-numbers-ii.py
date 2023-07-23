class Solution:
    def add(self, l1, l2, carry = 0):
        if l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            currval = l1val + l2val + carry
            curr = ListNode(val = currval % 10)
            curr.next = self.add(l1.next if l1 else None, l2.next if l2 else None, carry = currval // 10)
            return curr
        else:
            if carry > 0:
                return ListNode(val = carry)
            return None
        
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        return self.reverse(self.add(l1, l2, carry = 0))