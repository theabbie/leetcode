from collections import deque, defaultdict

class Solution:
    def DFS(self, grid, i, j, n, v):
        v.add((i, j))
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and (x, y) not in v:
                self.DFS(grid, x, y, n, v)
                
    def BFS(self, grid, n, a):
        q = deque([(a, 0)])
        dist = defaultdict(lambda: float('inf'))
        dist[a] = 0
        while len(q) > 0:
            p, d = q.pop()
            i, j = p
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n:
                    diff = 1
                    if grid[i][j] == 1 and grid[x][y] == 1:
                        diff = 0
                    if dist[(x, y)] > dist[(i, j)] + diff:
                        dist[(x, y)] = dist[(i, j)] + diff
                        q.appendleft(((x, y), d + 1))
        return dist
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a = b = None
        v = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in v:
                        if a == None:
                            a = (i, j)
                        elif b == None:
                            b = (i, j)
                        self.DFS(grid, i, j, n, v)
        dist = self.BFS(grid, n, a)
        return dist[b] - 1