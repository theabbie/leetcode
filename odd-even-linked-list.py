class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenprev = None
        oddprev = None
        evenhead = None
        oddhead = None
        curr = head
        odd = False
        while curr:
            nextcurr = curr.next
            if odd:
                if oddprev != None:
                    oddprev.next = curr
                else:
                    oddhead = curr
                oddprev = curr
                oddprev.next = None
            else:
                if evenprev != None:
                    evenprev.next = curr
                else:
                    evenhead = curr
                evenprev = curr
                evenprev.next = None
            curr = nextcurr
            odd = not odd
        if evenprev:
            evenprev.next = oddhead
        return evenhead