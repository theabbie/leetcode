class Solution:
    def count(self, num, i, tight, s, x, cache):
        if i >= len(num):
            return s
        key = (i, tight, s)
        if key in cache:
            return cache[key]
        maxd = 1
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            curr = self.count(num, i + 1, tight and d == maxd, s + int(d == 1 and (len(num) - i) % x == 0), x, cache)
            res += curr
        cache[key] = res
        return res
    
    def findMaximumNumber(self, k: int, x: int) -> int:
        end = 1
        while self.count("{:0b}".format(end), 0, True, 0, x, {}) <= k:
            end *= 2
        beg = end // 2
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            if self.count("{:0b}".format(mid), 0, True, 0, x, {}) <= k:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res