class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10 ** 9 + 7
        @lru_cache(maxsize = None)
        def count(rem, x):
            if rem < 0:
                return 0
            if x == 0:
                return int(rem == 0)
            res = 0
            for i in range(1, k + 1):
                res += count(rem - i, x - 1)
                res %= M
            return res
        return count(target, n)