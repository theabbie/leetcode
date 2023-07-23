from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        valid = lambda x, y: 0 <= x < m and 0 <= y < n and grid[x][y] != "#"
        start = box = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "S":
                    start = (i, j)
                if grid[i][j] == "B":
                    box = (i, j)
        q = deque([(start, box, 0)])
        v = {(start, box)}
        res = -1
        while len(q) > 0:
            curr, currbox, d = q.pop()
            if grid[currbox[0]][currbox[1]] == "T":
                return d
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x, y = curr[0] + dx, curr[1] + dy
                if not valid(x, y):
                    continue
                if (x, y) == currbox:
                    newbox = (curr[0] + 2 * dx, curr[1] + 2 * dy)
                    if valid(newbox[0], newbox[1]) and ((x, y), newbox) not in v:
                        v.add(((x, y), newbox))
                        q.appendleft(((x, y), newbox, d + 1))
                elif ((x, y), currbox) not in v:
                    v.add(((x, y), currbox))
                    q.append(((x, y), currbox, d))
        return res