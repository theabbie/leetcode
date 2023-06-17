class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowsums = [[0] * (n + 1) for _ in range(m)]
        colsums = [[0] * (m + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rowsums[i][j + 1] += rowsums[i][j] + grid[i][j]
                colsums[j][i + 1] += colsums[j][i] + grid[i][j]
        def same(i0, j0, i1, j1):
            s = rowsums[i0][j1 + 1] - rowsums[i0][j0]
            a = b = 0
            for x in range(i0, i1 + 1):
                a += grid[x][j0 + x - i0]
                if rowsums[x][j1 + 1] - rowsums[x][j0] != s:
                    return False
            for y in range(j0, j1 + 1):
                b += grid[i1 - (y - j0)][y]
                if colsums[y][i1 + 1] - colsums[y][i0] != s:
                    return False
            return a == b == s
        res = 1
        for i in range(m):
            for j in range(n):
                for l in range(1, min(m - i, n - j)):
                    if same(i, j, i + l, j + l):
                        res = max(res, l + 1)
        return res