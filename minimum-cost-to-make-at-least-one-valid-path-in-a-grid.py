class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ways = [(0, -1, 2), (0, 1, 1), (-1, 0, 4), (1, 0, 3)]
        q = deque([(0, 0)])
        d = [[float('inf')] * n for _ in range(m)]
        d[0][0] = 0
        while q:
            i, j = q.pop()
            if (i, j) == (m - 1, n - 1):
                return d[i][j]
            for dx, dy, need in ways:
                x, y = i + dx, j + dy
                if not 0 <= x < m or not 0 <= y < n:
                    continue
                cost = int(grid[i][j] != need)
                if d[x][y] > d[i][j] + cost:
                    d[x][y] = d[i][j] + cost
                    (q.appendleft if cost == 1 else q.append)((x, y))