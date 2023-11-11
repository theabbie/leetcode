class Solution:
    def minops(self, unequals, i, ctr, n, x):
        if i >= n:
            if ctr == 0:
                return 0
            return float('inf')
        key = (i, ctr)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        if i + 1 < n:
            res = min(res, self.minops(unequals, i + 2, ctr, n, x) + min(x, unequals[i + 1] - unequals[i]))
        if ctr > 0:
            res = min(res, self.minops(unequals, i + 1, ctr - 1, n, x))
        res = min(res, x + self.minops(unequals, i + 1, ctr + 1, n, x))
        self.cache[key] = res
        return res
    
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        unequals = []
        for i in range(n):
            if s1[i] != s2[i]:
                unequals.append(i)
        m = len(unequals)
        if m & 1:
            return -1
        self.cache = {}
        return self.minops(unequals, 0, 0, m, x)