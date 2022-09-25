class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        curr.prev = None
        n = 1
        while curr and curr.next:
            curr.next.prev = curr
            curr = curr.next
            n += 1
        if n <= 2:
            return
        beg = head
        while beg and curr:
            newbeg = beg.next
            newcurr = curr.prev
            beg.next, curr.next = curr, beg.next
            beg = newbeg
            curr = newcurr
            if newbeg and newcurr and (newbeg == newcurr or newbeg.next == newcurr):
                if newbeg != newcurr:
                    newcurr.prev.next = None
                newcurr.next = None