class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                r = [0, 0, 0]
                c = [0, 0, 0]
                a = b = 0
                used = [0] * 9
                for x in range(i - 1, i + 2):
                    a += grid[x][j + x - i]
                    b += grid[x][j - x + i]
                    for y in range(j - 1, j + 2):
                        if 1 <= grid[x][y] <= 9:
                            used[grid[x][y] - 1] = 1
                        r[x - i + 1] += grid[x][y]
                        c[y - j + 1] += grid[x][y]
                if sum(used) == 9 and r[0] == r[1] == r[2] == c[0] == c[1] == c[2] == a == b:
                    res += 1
        return res