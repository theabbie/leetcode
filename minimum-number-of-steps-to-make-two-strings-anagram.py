from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str):
        ctrs = Counter(s)
        ctrt = Counter(t)
        res = 0
        for i in range(26):
            c = chr(ord("a") + i)
            res += abs(ctrs[c] - ctrt[c])
        return res // 2