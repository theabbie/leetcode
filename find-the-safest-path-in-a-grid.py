from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        beg = 0
        end = 2 * (n - 1)
        while beg <= end:
            mid = (beg + end) // 2
            q = deque()
            blocked = [[False] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        blocked[i][j] = True
                        q.appendleft((i, j, 0))
            while q:
                i, j, d = q.pop()
                if d <= mid:
                    blocked[i][j] = True
                if d == mid:
                    continue
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < n and not blocked[x][y]:
                        blocked[x][y] = True
                        q.appendleft((x, y, d + 1))
            if blocked[0][0]:
                end = mid - 1
                continue
            possible = False
            q = deque([(0, 0)])
            while q:
                i, j = q.pop()
                if (i, j) == (n - 1, n - 1):
                    possible = True
                    break
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < n and not blocked[x][y]:
                        blocked[x][y] = True
                        q.appendleft((x, y))
            if possible:
                beg = mid + 1
            else:
                end = mid - 1
        return beg