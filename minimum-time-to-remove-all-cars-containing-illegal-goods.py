class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        res = float('inf')
        maxval = float('-inf')
        p = 0
        for i in range(n + 1):
            c = 2 * p - i
            maxval = max(maxval, c)
            res = min(res, n + c - maxval)
            p += int(s[min(i, n - 1)])
        return res