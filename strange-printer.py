class Solution:
    def minops(self, s, l, r):
        if s[l : r + 1] == s[l] * (r - l + 1):
            return 0
        if self.cache[l][r] != -1:
            return self.cache[l][r]
        res = r - l + 1
        ldiff = l
        while ldiff < r and s[ldiff] == s[r]:
            ldiff += 1
        for i in range(ldiff, r):
            ll = self.minops(s, ldiff, i)
            rr = self.minops(s, i + 1, r)
            res = min(res, ll + rr + 1)
        self.cache[l][r] = res
        return res
    
    def strangePrinter(self, s: str) -> int:
        self.cache = [[-1] * len(s) for _ in range(len(s))]
        return 1 + self.minops(s, 0, len(s) - 1)