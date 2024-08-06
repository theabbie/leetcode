class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = (n // 2, n // 2)
        ycells = set()
        x = y = 0
        while x <= center[0]:
            ycells.add((x, y))
            x += 1
            y += 1
        x = 0
        y = n - 1
        while x <= center[0]:
            ycells.add((x, y))
            x += 1
            y -= 1
        x = center[0]
        y = center[1]
        while x < n:
            ycells.add((x, y))
            x += 1
        res = n * n
        for ycolor in range(3):
            for rest in range(3):
                if ycolor == rest:
                    continue
                ychange = 0
                restchange = 0
                for i in range(n):
                    for j in range(n):
                        if (i, j) in ycells and grid[i][j] != ycolor:
                            ychange += 1
                        if (i, j) not in ycells and grid[i][j] != rest:
                            restchange += 1
                res = min(res, ychange + restchange)
        return res