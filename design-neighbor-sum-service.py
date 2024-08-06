class neighborSum:
    def __init__(self, grid: List[List[int]]):
        m = len(grid)
        n = len(grid[0])
        self.pos = {}
        for i in range(m):
            for j in range(n):
                self.pos[grid[i][j]] = (i, j)
        self.m, self.n, self.grid = m, n, grid

    def adjacentSum(self, value: int) -> int:
        if value not in self.pos:
            return 0
        i, j = self.pos[value]
        res = 0
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < self.m and 0 <= y < self.n:
                res += self.grid[x][y]
        return res

    def diagonalSum(self, value: int) -> int:
        if value not in self.pos:
            return 0
        i, j = self.pos[value]
        res = 0
        for x, y in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            if 0 <= x < self.m and 0 <= y < self.n:
                res += self.grid[x][y]
        return res