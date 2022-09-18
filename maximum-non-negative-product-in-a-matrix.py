class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[(0, 0)] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr = []
                if i == 0 and j == 0:
                    curr += [grid[i][j]]
                if i > 0:
                    curr += [grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1]]
                if j > 0:
                    curr += [grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1]]
                dp[i][j] = (max(curr), min(curr))
        res = max(dp[m - 1][n - 1])
        if res < 0:
            return -1
        return res % (10 ** 9 + 7)