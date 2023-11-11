class Solution:
    def count(self, num, i, n, tight, nzseen, mod, k, diff, cache):
        if i >= n:
            return int(mod == 0 and diff == 0)
        key = (i, tight, nzseen, mod, diff)
        if key in cache:
            return cache[key]
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            newnzseen = nzseen or d != 0
            newdiff = diff
            if newnzseen:
                if d & 1:
                    newdiff += 1
                else:
                    newdiff -= 1
            res += self.count(num, i + 1, n, tight and d == maxd, newnzseen, (10 * mod + d) % k, k, newdiff, cache)
        cache[key] = res
        return res
    
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        return self.count(str(high), 0, len(str(high)), True, False, 0, k, 0, {}) - self.count(str(low - 1), 0, len(str(low - 1)), True, False, 0, k, 0, {})