class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ln = lambda h: 1 + ln(h.next) if h else 0
        l = ln(head)
        res = []
        prev = None
        curr = head
        for i in range(k):
            res.append(curr)
            for _ in range(l // k + int(i < l % k)):
                prev, curr = curr, curr.next
            if prev:
                prev.next = None
        return res