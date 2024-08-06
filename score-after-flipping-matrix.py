class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for flip in range(2):
            pw = 1 << (n - 1)
            curr = 0
            for j in range(n):
                colsum = 0
                for i in range(m):
                    fval = grid[i][0] if not flip else 1 - grid[i][0]
                    colsum += grid[i][j] if fval == 1 else 1 - grid[i][j]
                curr += pw * max(colsum, m - colsum)
                pw //= 2
            res = max(res, curr)
        return res