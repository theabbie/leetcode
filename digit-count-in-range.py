class Solution:
    def count(self, s, i, tight, nzseen, ctr, target, cache):
        if i >= len(s):
            return ctr
        key = (i, tight, nzseen, ctr)
        if key in cache:
            return cache[key]
        maxd = 9
        if tight:
            maxd = int(s[i])
        res = 0
        for d in range(maxd + 1):
            newnzseen = nzseen or d != 0
            res += self.count(s, i + 1, tight and d == maxd, newnzseen, ctr + int(newnzseen and d == target), target, cache)
        cache[key] = res
        return res
    
    def digitsCount(self, d: int, low: int, high: int) -> int:
        return self.count(str(high), 0, True, False, 0, d, {}) - self.count(str(low - 1), 0, True, False, 0, d, {})