from collections import Counter

class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        np = len(p)
        ns = len(s)
        ctrp = Counter(p)
        ctrs = Counter()
        for i in range(ns):
            ctrs[s[i]] += 1
            if i >= np:
                ctrs[s[i - np]] -= 1
            if i >= np - 1 and ctrp == ctrs:
                return True
        return False