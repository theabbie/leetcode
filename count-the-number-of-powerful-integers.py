from collections import defaultdict

class Solution:
    def count(self, num, i, n, tight, limit, suff, s, cache):
        if n < len(s):
            return 0
        if i >= n:
            return int(suff)
        key = (i, tight, suff)
        if key in cache:
            return cache[key]
        res = 0
        maxd = limit
        if tight:
            maxd = min(maxd, int(num[i]))
        for d in range(maxd + 1):
            newsuff = suff
            if n - i <= len(s):
                if s[-(n - i)] != str(d):
                    newsuff = False
            res += self.count(num, i + 1, n, tight and d == int(num[i]), limit, newsuff, s, cache)
        cache[key] = res
        return res
    
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.count(str(finish), 0, len(str(finish)), True, limit, True, s, {}) - self.count(str(start - 1), 0, len(str(start - 1)), True, limit, True, s, {})