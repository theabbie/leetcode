class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowmax = [0] * m
        colmax = [0] * n
        for i in range(m):
            for j in range(n):
                rowmax[i] = max(rowmax[i], grid[i][j])
                colmax[j] = max(colmax[j], grid[i][j])
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(rowmax[i], colmax[j]) - grid[i][j]
        return res