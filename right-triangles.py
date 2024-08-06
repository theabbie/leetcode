class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        row = []
        col = []
        for i in range(m):
            row.append([0])
            for j in range(n):
                row[-1].append(row[-1][-1] + grid[i][j])
        for j in range(n):
            col.append([0])
            for i in range(m):
                col[-1].append(col[-1][-1] + grid[i][j])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = col[j][i]
                    left = row[i][j]
                    bottom = col[j][m] - top - 1
                    right = row[i][n] - left - 1
                    res += top * left + left * bottom + bottom * right + top * right
        return res