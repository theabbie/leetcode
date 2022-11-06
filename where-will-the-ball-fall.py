class Solution:
    def getpos(self, grid, i, j, m, n):
        if i == m:
            return j
        nj = j - 1
        if grid[i][j] == 1:
            nj = j + 1
        if 0 <= nj < n and grid[i][j] == grid[i][nj]:
            return self.getpos(grid, i + 1, nj, m, n)
        return -1
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        return [self.getpos(grid, 0, j, m, n) for j in range(n)]