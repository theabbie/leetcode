M = 10 ** 9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        @lru_cache(maxsize = None)
        def count(i, l, val):
            if l > n:
                return 0
            res = val
            j = 2
            while i * j <= maxValue:
                res += count(i * j, l + 1, (val * (n - l) * pow(l, M - 2, M)) % M)
                res %= M
                j += 1
            return res
        res = 0
        for i in range(1, maxValue + 1):
            res += count(i, 1, 1)
            res %= M
        return res