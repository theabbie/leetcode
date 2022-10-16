class Solution:
    def minLen(self, s, i, n, prev, ctr, k):
        if k < 0:
            return float('inf')
        if i >= n:
            return 0
        key = (i, prev, ctr, k)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        res = min(res, self.minLen(s, i + 1, n, prev, ctr, k - 1))
        if s[i] != prev:
            res = min(res, 1 + self.minLen(s, i + 1, n, s[i], 1, k))
        else:
            l = 0
            if ctr == 1 or ctr == 9 or ctr == 99:
                l = 1
            res = min(res, l + self.minLen(s, i + 1, n, s[i], ctr + 1, k))
        self.cache[key] = res
        return res
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        self.cache = {}
        return self.minLen(s, 0, n, None, 0, k)