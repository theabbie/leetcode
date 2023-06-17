class Solution:
    def count(self, grid, i, j, m, n, mask, target):
        if grid[i][j] == 2:
            if mask == target:
                return 1
            return 0
        key = (i, j, mask)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] != -1 and not mask & (1 << (n * x + y)):
                res += self.count(grid, x, y, m, n, mask | (1 << (n * x + y)), target)
        self.cache[key] = res
        return res
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.cache = {}
        start = (-1, -1)
        target = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    target |= 1 << (n * i + j)
        return self.count(grid, start[0], start[1], m, n, 1 << (n * start[0] + start[1]), target)