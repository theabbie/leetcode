class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        v = set()
        q = deque([(0, 0, health - grid[0][0])])
        while q:
            i, j, h = q.pop()
            if h > 0 and (i, j) == (m - 1, n - 1):
                return True
            if h <= 0:
                continue
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y, h - grid[x][y]) not in v:
                    v.add((x, y, h - grid[x][y]))
                    q.appendleft((x, y, h - grid[x][y]))
        return False