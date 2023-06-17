class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for j in range(n - 2, -1, -1):
            for i in range(m):
                for x in range(i - 1, i + 2):
                    if 0 <= x < m and grid[x][j + 1] > grid[i][j]:
                        dp[i][j] = max(dp[i][j], 1 + dp[x][j + 1])
                        if j == 0:
                            res = max(res, dp[i][j])
        return res