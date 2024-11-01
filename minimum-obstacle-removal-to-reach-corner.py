from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0, 0, 0)])
        v = {(0, 0)}
        while len(q) > 0:
            x, y, d = q.pop()
            if (x, y) == (m - 1, n - 1):
                return d
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n:
                    if (i, j) in v:
                        continue
                    v.add((i, j))
                    if grid[i][j] == 1:
                        q.appendleft((i, j, d + 1))
                    else:
                        q.append((i, j, d))