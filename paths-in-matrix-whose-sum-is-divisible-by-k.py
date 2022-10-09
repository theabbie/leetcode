class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        dp[m - 1][n - 1][grid[m - 1][n - 1] % k] += 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    for p in range(k):
                        dp[i][j][(p + grid[i][j]) % k] += dp[i + 1][j][p]
                if j < n - 1:
                    for p in range(k):
                        dp[i][j][(p + grid[i][j]) % k] += dp[i][j + 1][p]
        return dp[0][0][0] % (10 ** 9 + 7)