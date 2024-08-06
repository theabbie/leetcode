class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        f = [[0] * 10 for _ in range(n)]
        for j in range(n):
            for i in range(m):
                f[j][grid[i][j]] += 1
        dp = [[float('inf')] * 10 for _ in range(n)]
        for i in range(n):
            for j in range(10):
                for prev in range(10):
                    if j != prev:
                        dp[i][j] = min(dp[i][j], m - f[i][j] + (dp[i - 1][prev] if i > 0 else 0))
        return min(dp[n - 1])