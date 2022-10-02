class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                curr = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        curr += grid[x][y]
                curr -= grid[i][j - 1] + grid[i][j + 1]
                res = max(res, curr)
        return res