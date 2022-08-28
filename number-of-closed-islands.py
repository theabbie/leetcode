class Solution:
    def DFS(self, grid, i, j, m, n):
        if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == 0:
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                self.isBoundary = True
            grid[i][j] = 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                self.DFS(grid, x, y, m, n)
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ctr = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.isBoundary = False
                    self.DFS(grid, i, j, m, n)
                    if not self.isBoundary:
                        ctr += 1
        return ctr