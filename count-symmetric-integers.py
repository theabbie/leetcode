class Solution:
    def count(self, num, i, n, tight, nz, isSecHalf, rem, diff, cache):
        if i >= n:
            if not nz:
                return 0
            return int(diff == 0 and rem == 0)
        key = (i, tight, nz, isSecHalf, rem, diff)
        if key in cache:
            return cache[key]
        res = 0
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            newnz = nz or d != 0
            newrem = rem
            newdiff = diff
            if isSecHalf:
                newdiff -= d
                if newnz:
                    newrem -= 1
            else:
                newdiff += d
                if newnz:
                    newrem += 1
            res += self.count(num, i + 1, n, tight and d == maxd, newnz, isSecHalf, newrem, newdiff, cache)
            if newnz and not isSecHalf:
                res += self.count(num, i + 1, n, tight and d == maxd, newnz, True, newrem, newdiff, cache)
        cache[key] = res
        return res
    
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        low -= 1
        low = str(low)
        high = str(high)
        return self.count(high, 0, len(high), True, False, False, 0, 0, {}) - self.count(low, 0, len(low), True, False, False, 0, 0, {})