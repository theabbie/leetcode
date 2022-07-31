from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        ctr = 0
        maxt = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.appendleft((i, j, 0))
                    seen.add((i, j))
                elif grid[i][j] == 0:
                    ctr += 1
        while len(queue) > 0:
            x, y, t = queue.pop()
            for i, j in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    if (i, j) not in seen:
                        queue.appendleft((i, j, t + 1))
                        seen.add((i, j))
            maxt = t
        if len(seen) + ctr != m * n:
            return -1
        return maxt