class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            lastcol = [row[-1] for row in grid]
            for i in range(m):
                for j in range(n - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]
            for i in range(m):
                grid[i][0] = lastcol[(m + i - 1) % m]
        return grid