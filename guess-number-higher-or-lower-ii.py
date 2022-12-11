class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]
        get = lambda i, j: 0 if i >= j else dp[i][j]
        for l in range(1, n + 1):
            for i in range(n - l):
                dp[i][i + l] = float('inf')
                for j in range(i, i + l + 1):
                    dp[i][i + l] = min(dp[i][i + l], j + 1 + max(get(i, j - 1), get(j + 1, i + l)))
        return dp[0][n - 1]