class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        points = []
        for i in range(m):
            for j in range(n):
                points.append((i, j))
        points.sort(key = lambda p: grid[p[0]][p[1]])
        if points[0] != (0, 0):
            return False
        for i in range(1, m * n):
            a, b = points[i - 1]
            c, d = points[i]
            if abs(a - c) + abs(b - d) != 3 or min(abs(a - c), abs(b - d)) == 0:
                return False
        return True