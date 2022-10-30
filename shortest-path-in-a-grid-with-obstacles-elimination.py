from collections import deque, defaultdict

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if k + 2 > m + n:
            return m + n - 2
        dist = defaultdict(lambda: float('inf'))
        beg = (0, 0, k, 0)
        q = deque([beg])
        v = {(0, 0, k)}
        res = float('inf')
        while len(q) > 0:
            x, y, rem, d = q.pop()
            if (x, y) == (m - 1, n - 1):
                res = min(res, d)
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n:
                    newrem = rem - grid[i][j]
                    if newrem >= 0 and (i, j, newrem) not in v:
                        v.add((i, j, newrem))
                        q.appendleft((i, j, newrem, d + 1))
        if res == float('inf'):
            return -1
        return res