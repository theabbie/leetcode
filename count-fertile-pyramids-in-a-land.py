class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        def count():
            nonlocal res
            dp = [[0] * n for _ in range(m)]
            for j in range(n):
                if grid[m - 1][j] == 1:
                    dp[m - 1][j] = 1
                else:
                    dp[m - 1][j] = 0
            for i in range(m - 2, -1, -1):
                for j in range(n):
                    l = r = 0
                    if j > 0:
                        l = dp[i + 1][j - 1]
                    if j + 1 < n:
                        r = dp[i + 1][j + 1]
                    if grid[i][j] == grid[i + 1][j] == 1:
                        dp[i][j] = 1 + min(l, r)
                    elif grid[i][j] == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                    res += max(dp[i][j] - 1, 0)
        count()
        for i in range(m // 2):
            grid[i], grid[m - i - 1] = grid[m - i - 1], grid[i]
        count()
        return res