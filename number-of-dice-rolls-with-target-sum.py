from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            return 1 if 1 <= target <= k else 0
        ways = 0
        for i in range(1, k + 1):
            ways += self.numRollsToTarget(n - 1, k, target - i)
        return ways % (10 ** 9 + 7)