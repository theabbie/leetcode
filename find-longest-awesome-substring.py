class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        f = {}
        f[0] = 0
        p = 0
        res = 0
        for i in range(n):
            p ^= 1 << (ord(s[i]) - ord('0'))
            res = max(res, i + 1 - f.get(p, n))
            for c in range(10):
                res = max(res, i + 1 - f.get(p ^ (1 << c), n))
            if p not in f:
                f[p] = i + 1
        return res