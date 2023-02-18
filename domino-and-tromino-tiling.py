class Solution:
    def numTilings(self, n: int) -> int:
        M = 10 ** 9 + 7
        dp = [0] * max(n + 1, 3)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= M
        return dp[n]