class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = float('-inf')
        mx = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                mx[i][j] = max(mx[i + 1][j], mx[i][j + 1])
                res = max(res, mx[i][j] - grid[i][j])
                mx[i][j] = max(mx[i][j], grid[i][j])
        return res