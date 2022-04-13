class Solution:
    def calcMin(self, grid, x, y, m, n):
        if (x, y) in self.cache:
            return self.cache[(x, y)]
        if (x, y) == (m - 1, n - 1):
            self.cache[(x, y)] = grid[m - 1][n - 1]
            return self.cache[(x, y)]
        right = float('inf')
        bottom = float('inf')
        if y < n - 1:
            right = self.calcMin(grid, x, y + 1, m, n)
        if x < m - 1:
            bottom = self.calcMin(grid, x + 1, y, m, n)
        currMin = min(right, bottom)
        self.cache[(x, y)] = grid[x][y] + currMin
        return self.cache[(x, y)]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.cache = {}
        return self.calcMin(grid, 0, 0, len(grid), len(grid[0]))