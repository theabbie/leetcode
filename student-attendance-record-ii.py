class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        for i in range(2):
            for j in range(3):
                dp[0][i][j] = 1
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    dp[i][j][k] = dp[i - 1][j][0]
                    if j == 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j + 1][0]) % M
                    if k < 2:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k + 1]) % M
        return dp[n][0][0]