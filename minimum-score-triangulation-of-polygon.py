class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[float('inf')] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                if l <= 1:
                    dp[i][i + l] = 0
                for j in range(i, i + l):
                    dp[i][i + l] = min(dp[i][i + l], values[i] * values[j] * values[i + l] + dp[i][j] + dp[j][i + l])
        return dp[0][n - 1]