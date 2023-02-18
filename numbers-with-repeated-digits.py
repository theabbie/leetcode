class Solution:
    def count(self, num, i, n, tight, used):
        if i >= n:
            return 1
        key = (i, tight, used)
        if key in self.cache:
            return self.cache[key]
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            if not used & (1 << d):
                newused = used | (1 << d)
                if used == 0 and d == 0:
                    newused = used
                res += self.count(num, i + 1, n, tight and d == maxd, newused)
        self.cache[key] = res
        return res
    
    def numDupDigitsAtMostN(self, n: int) -> int:
        self.cache = {}
        num = str(n)
        return n - self.count(num, 0, len(num), True, 0) + 1