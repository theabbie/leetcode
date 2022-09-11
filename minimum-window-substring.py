from collections import Counter

class Solution:
    def contains(self, tctr, ctr):
        for c in tctr:
            if ctr[c] < tctr[c]:
                return False
        return True

    def pos(self, s, n, tctr, p):
        ctr = Counter(s[:p])
        if self.contains(tctr, ctr):
            return s[:p]
        for i in range(n - p):
            ctr[s[i]] -= 1
            ctr[s[i + p]] += 1
            if self.contains(tctr, ctr):
                return s[i + 1: i + p + 1]
        return False
    
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        k = len(t)
        tctr = Counter(t)
        beg = 1
        end = n
        res = ""
        while beg <= end:
            mid = (beg + end) // 2
            curr = self.pos(s, n, tctr, mid)
            if curr:
                res = curr
                end = mid - 1
            else:
                beg = mid + 1
        return res