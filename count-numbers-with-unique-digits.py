class Solution:
    def count(self, num, i, n, tight, nzseen, mask):
        if i >= n:
            return 1
        key = (i, tight, nzseen, mask)
        if key in self.cache:
            return self.cache[key]
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            if not mask & (1 << d) or (d == 0 and not nzseen):
                newmask = mask
                if d != 0 or (nzseen and d == 0):
                    newmask = mask | (1 << d)
                res += self.count(num, i + 1, n, tight and d == maxd, nzseen or d != 0, newmask)
        self.cache[key] = res
        return res
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.cache = {}
        return self.count(str(10 ** n - 1), 0, n, True, False, 0)