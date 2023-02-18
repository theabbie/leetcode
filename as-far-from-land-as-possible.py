from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        v = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.appendleft((i, j, 0))
                    v.add((i, j))
        res = -1
        while len(q) > 0:
            i, j, d = q.pop()
            if grid[i][j] == 0:
                res = max(res, d)
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in v:
                    v.add((x, y))
                    if grid[i][j] != 1 or grid[x][y] != 1:
                        q.appendleft((x, y, d + 1))
        return res