class Solution:
    def isEmpty(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or  j >= n:
            return True
        if grid[i][j] == 1:
            return False
        return True
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if self.isEmpty(grid, x, y, m, n):
                            perimeter += 1
        return perimeter