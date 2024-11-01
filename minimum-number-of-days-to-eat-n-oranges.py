class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize = None)
        def dp(n):
            if n == 0:
                return -1
            return 1 + min(n % 2 + dp(n // 2), n % 3 + dp(n // 3))
        return dp(n)