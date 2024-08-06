class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s, f = (0, -1), (0, -1)
        for i in range(m):
            for j in range(n):
                if f[1] != j:
                    grid[i][j] += f[0]
                else:
                    grid[i][j] += s[0]
            s, f = (float('inf'), 0), (float('inf'), 0)
            for j in range(n):
                f, s, x = sorted([s, f, (grid[i][j], j)])
        return f[0]