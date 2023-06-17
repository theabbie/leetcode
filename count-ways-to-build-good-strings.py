class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        M = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        res = 0
        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
                dp[i] %= M
            if i >= one:
                dp[i] += dp[i - one]
                dp[i] %= M
            if low <= i <= high:
                res = (res + dp[i]) % M
        return res