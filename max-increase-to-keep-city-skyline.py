class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowmaxes = [float('-inf')] * n
        colmaxes = [float('-inf')] * n
        for i in range(n):
            for j in range(n):
                rowmaxes[i] = max(rowmaxes[i], grid[i][j])
                colmaxes[j] = max(colmaxes[j], grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(rowmaxes[i], colmaxes[j]) - grid[i][j]
        return res