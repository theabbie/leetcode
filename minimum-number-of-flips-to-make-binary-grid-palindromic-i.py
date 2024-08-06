class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        a = b = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][~j]:
                    a += 1
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[~i][j]:
                    b += 1
        return min(a, b)