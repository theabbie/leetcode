class Solution:
    def lenOfVDiagonal(self, grid):
        m = len(grid)
        n = len(grid[0])
        clock = {(1, 1): (1, -1), (1, -1): (-1, -1), (-1, -1): (-1, 1), (-1, 1): (1, 1)}
        @cache
        def dp(i, j, dx, dy, done, even):
            if not (0 <= i < m) or not (0 <= j < n):
                return 0
            if grid[i][j] == 1:
                return 0
            if even and grid[i][j] != 2:
                return 0
            if not even and grid[i][j] != 0:
                return 0
            cdx, cdy = clock[(dx, dy)]
            return 1 + max(dp(i + dx, j + dy, dx, dy, done, not even), dp(i + cdx, j + cdy, cdx, cdy, True, not even) if not done else 0)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in clock:
                        res = max(res, 1 + dp(i + dx, j + dy, dx, dy, False, True))
        return res