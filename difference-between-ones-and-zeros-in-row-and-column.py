class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onerows = [0] * m
        onecols = [0] * n
        for i in range(m):
            for j in range(n):
                onerows[i] += grid[i][j]
                onecols[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * onerows[i] + 2 * onecols[j] - m - n
        return grid