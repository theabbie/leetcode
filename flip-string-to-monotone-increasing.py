class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        res = float('inf')
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + int(s[i])
        for i in range(n + 1):
            leftones = p[i]
            rightzeroes = (n - p[n]) - (i - p[i])
            res = min(res, leftones + rightzeroes)
        return res