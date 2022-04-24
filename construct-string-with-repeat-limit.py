import heapq
from collections import Counter

class Solution:
    def lastRepeatLen(self, s, currc, replen):
        n = len(s)
        if n == 0 or currc == s[-1]:
            return replen + 1
        return 1
    
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ctr = Counter(s)
        op = ""
        replen = 0
        heap = []
        for c in ctr:
            heapq.heappush(heap, (-ord(c), c))
        while len(heap) > 0:
            k, currc = heapq.heappop(heap)
            while len(heap) > 0 and currc not in ctr:
                k, currc = heapq.heappop(heap)
            if self.lastRepeatLen(op, currc, replen) > repeatLimit:
                if len(heap) > 0:
                    newk, newc = heapq.heappop(heap)
                    replen = self.lastRepeatLen(op, newc, replen)
                    op += newc
                    ctr[newc] -= 1
                    if ctr[newc] == 0:
                        del ctr[newc]
                    else:
                        heapq.heappush(heap, (newk, newc))
                    heapq.heappush(heap, (k, currc))
                else:
                    break
            else:
                replen = self.lastRepeatLen(op, currc, replen)
                op += currc
                ctr[currc] -= 1
                if ctr[currc] == 0:
                    del ctr[currc]
                else:
                    heapq.heappush(heap, (k, currc))
        return op