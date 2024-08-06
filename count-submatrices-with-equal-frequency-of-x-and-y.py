class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        x = y = 0
        xx = [[0] * (n + 1) for _ in range(m + 1)]
        yy = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xx[i][j] = int(grid[i - 1][j - 1] == 'X') + xx[i][j - 1] + xx[i - 1][j] - xx[i - 1][j - 1]
                yy[i][j] = int(grid[i - 1][j - 1] == 'Y') + yy[i][j - 1] + yy[i - 1][j] - yy[i - 1][j - 1]
                if xx[i][j] > 0 and xx[i][j] == yy[i][j]:
                    res += 1
        return res