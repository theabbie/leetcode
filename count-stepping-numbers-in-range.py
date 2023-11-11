M = 10 ** 9 + 7

class Solution:
    def count(self, num, i, n, prev, tight, nzseen):
        if i >= n:
            return 1
        key = (i, prev, tight, nzseen)
        if key in self.cache:
            return self.cache[key]
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            if prev == -1 or d == prev + 1 or d == prev - 1:
                newprev = prev
                if nzseen or d != 0:
                    newprev = d
                res += self.count(num, i + 1, n, newprev, tight and d == maxd, nzseen or d != 0)
                res %= M
        self.cache[key] = res
        return res
    
    def countSteppingNumbers(self, low: str, high: str) -> int:
        self.cache = {}
        l = self.count(low, 0, len(low), -1, True, False)
        extra = 1
        for i in range(len(low) - 1):
            if abs(int(low[i]) - int(low[i + 1])) != 1:
                extra = 0
                break
        self.cache = {}
        r = self.count(high, 0, len(high), -1, True, False)
        res = (M + r - l + extra) % M
        return res