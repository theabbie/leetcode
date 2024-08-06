from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        ctr = Counter()
        for i in range(n):
            ctr = Counter()
            for j in range(i, n):
                ctr[s[j]] += 1
                if max(ctr.values()) <= 2:
                    res = max(res, j - i + 1)
        return res