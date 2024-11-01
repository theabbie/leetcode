M = 10 ** 9 + 7

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        k = min(n, x)
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][i] = 1
        for i in range(1, k + 1):
            for j in range(i + 1, n + 1):
                dp[i][j] = (i * dp[i][j - 1] + dp[i - 1][j - 1]) % M
        res = 0
        v = x * y
        for choose in range(1, k + 1):
            res += dp[choose][n] * v
            v *= y * (x - choose)
            v %= M
            res %= M
        return res