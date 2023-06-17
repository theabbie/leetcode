M = 10 ** 9 + 7

class Solution:
    def countnums(self, num, i, n, tight, s, mins, maxs, cache):
        if i >= n:
            if mins <= s <= maxs:
                return 1
            return 0
        key = (i, tight, s)
        if key in cache:
            return cache[key]
        maxd = 9
        if tight:
            maxd = int(num[i])
        res = 0
        for d in range(maxd + 1):
            res += self.countnums(num, i + 1, n, tight and d == maxd, s + d, mins, maxs, cache)
            res %= M
        cache[key] = res
        return res
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        x = 0
        if min_sum <= sum(map(int, num1)) <= max_sum:
            x = 1
        return (M + self.countnums(num2, 0, len(num2), True, 0, min_sum, max_sum, {}) - self.countnums(num1, 0, len(num1), True, 0, min_sum, max_sum, {}) + x) % M