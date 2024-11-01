class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        @lru_cache(maxsize = None)
        def dp(n):
            if n & 1:
                return 0
            if n <= 2:
                return 1
            l = 0
            res = 0
            while n - l >= 2:
                res += dp(l) * dp(n - l - 2)
                res %= 1000000007
                l += 2
            return res
        return dp(numPeople)