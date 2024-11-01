M = 10 ** 9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        @lru_cache(maxsize = None)
        def count(i, l):
            if l > n:
                return 0
            res = 1
            j = 2
            while i * j <= maxValue:
                res += (n - l) * pow(l, M - 2, M) * count(i * j, l + 1)
                res %= M
                j += 1
            return res
        res = 0
        for i in range(1, maxValue + 1):
            res += count(i, 1)
            res %= M
        return res