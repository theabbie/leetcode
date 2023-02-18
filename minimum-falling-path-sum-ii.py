class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        m = sm = (float('inf'), -1)
        for i in range(n):
            dp[0][i] = grid[0][i]
            m, sm, temp = sorted([m, sm, (dp[0][i], i)])
        for i in range(1, n):
            for j in range(n):
                if m[1] != j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][m[1]] + grid[i][j])
                if sm[1] != j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][sm[1]] + grid[i][j])
            m = sm = (float('inf'), -1)
            for j in range(n):
                m, sm, temp = sorted([m, sm, (dp[i][j], j)])
        return m[0]