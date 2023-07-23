class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key = lambda p: -grid[p[0]][p[1]])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i, j in points:
            dp[i][j] = 1
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    dp[i][j] += dp[x][y]
                    dp[i][j] %= M
            res += dp[i][j]
            res %= M
        return res