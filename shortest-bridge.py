from collections import deque, defaultdict

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        dist = defaultdict(lambda: float('inf'))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.appendleft((0, i, j))
                    dist[(i, j)] = 0
                    break
            if len(q) > 0:
                break
        while len(q) > 0:
            currdist, i, j = q.pop()
            if grid[i][j] == 1 and currdist > 0:
                return currdist
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    w = 0 if grid[x][y] == 1 else 1
                    if dist[(x, y)] > currdist + w:
                        dist[(x, y)] = currdist + w
                        if w == 0:
                            q.append((currdist + w, x, y))
                        else:
                            q.appendleft((currdist + w, x, y))