class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prev = float('inf')
                if i > 0:
                    prev = min(prev, dp[i - 1][j])
                if j > 0:
                    prev = min(prev, dp[i][j - 1])
                if prev == float('inf'):
                    prev = 0
                dp[i][j] = prev + grid[i][j]
        return dp[m - 1][n - 1]