class Solution:
    def DFS(self, grid, i, j, m, n):
        if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == 1:
            grid[i][j] = 0
            self.ctr += 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                self.DFS(grid, x, y, m, n)
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.ctr = 0
                    self.DFS(grid, i, j, m, n)
                    mArea = max(mArea, self.ctr)
        return mArea