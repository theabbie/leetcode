class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(0, n, 2):
            cost = int(s[i]) + int(s[i + 1])
            cost = min(cost, 2 - cost)
            res += cost
        return res