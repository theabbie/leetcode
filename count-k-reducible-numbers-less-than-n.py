M = 10 ** 9 + 7

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        @lru_cache(maxsize = None)
        def count(x):
            if x <= 1:
                return 0
            return 1 + count(x.bit_count())
        cache = {}
        def dp(i, ctr, tight):
            if i >= len(s):
                return int(1 + count(ctr) <= k and not tight)
            key = (i, ctr, tight)
            if key in cache:
                return cache[key]
            up = 1
            if tight:
                up = int(s[i])
            res = 0
            for d in range(0, up + 1):
                res += dp(i + 1, ctr + d, tight and d == up)
                res %= M
            cache[key] = res
            return res
        return (dp(0, 0, True) - 1) % M