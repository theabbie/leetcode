from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            ctr = Counter()
            for j in range(i, n):
                ctr[s[j]] += 1
                res += max(ctr.values()) - min(ctr.values())
        return res