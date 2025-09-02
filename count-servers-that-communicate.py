class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        r = [0] * m
        c = [0] * n
        for i in range(m):
            for j in range(n):
                r[i] += grid[i][j]
                c[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                if r[i] > 1 or c[j] > 1:
                    res += grid[i][j]
        return res