class Solution:
    def longest(self, strs, i, m, n, slen):
        if m < 0 or n < 0:
            return -1
        if i >= slen:
            return 0
        key = (i, m, n)
        if key in self.cache:
            return self.cache[key]
        x, y = strs[i]
        a = 1 + self.longest(strs, i + 1, m - x, n - y, slen)
        b = self.longest(strs, i + 1, m, n, slen)
        mlen = max(a, b)
        self.cache[key] = mlen
        return mlen
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        slen = len(strs)
        strs = [(s.count("0"), s.count("1")) for s in strs]
        self.cache = {}
        return self.longest(strs, 0, m, n, slen)