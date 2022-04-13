class Solution:
    def DFS(self, grid, i, j, m, n, visited):
        if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == 1:
            grid[i][j] = 0
            visited.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (x, y) not in visited:
                    self.DFS(grid, x, y, m, n, visited)
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set()
                    self.DFS(grid, i, j, m, n, visited)
                    mArea = max(mArea, len(visited))
        return mArea