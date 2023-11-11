class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        M = 12345
        pf = [1] * (m + 1)
        sf = [1] * (m + 1)
        for i in range(m):
            curr = 1
            for j in range(n):
                curr *= grid[i][j]
                curr %= M
            pf[i + 1] = pf[i] * curr
            pf[i + 1] %= M
        for i in range(m):
            curr = 1
            for j in range(n):
                curr *= grid[m - i - 1][j]
                curr %= M
            sf[i + 1] = sf[i] * curr
            sf[i + 1] %= M
        for i in range(m):
            top = pf[i]
            bottom = sf[m - i - 1]
            rowpf = [1] * (n + 1)
            rowsf = [1] * (n + 1)
            for j in range(n):
                rowpf[j + 1] = rowpf[j] * grid[i][j]
                rowsf[j + 1] = rowsf[j] * grid[i][n - j - 1]
                rowpf[j + 1] %= M
                rowsf[j + 1] %= M
            for j in range(n):
                grid[i][j] = top * bottom * rowpf[j] * rowsf[n - j - 1]
                grid[i][j] %= M
        return grid