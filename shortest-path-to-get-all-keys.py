from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        si = sj = -1
        target = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    si, sj = i, j
                if grid[i][j].isalpha() and grid[i][j].islower():
                    target |= 1 << (ord(grid[i][j]) - ord('a'))
        q = deque([(si, sj, 0, 0, 0)])
        v = {(si, sj, 0, 0)}
        while len(q) > 0:
            i, j, key, lock, steps = q.pop()
            if key == target:
                return steps
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                    newkey = key
                    newlock = lock
                    if grid[x][y].isalpha():
                        if grid[x][y].islower():
                            newkey |= 1 << (ord(grid[x][y]) - ord('a'))
                        if grid[x][y].isupper():
                            if not key & (1 << (ord(grid[x][y]) - ord('A'))):
                                continue
                            newlock |= 1 << (ord(grid[x][y]) - ord('A'))
                    if (x, y, newkey, newlock) not in v:
                        v.add((x, y, newkey, newlock))
                        q.appendleft((x, y, newkey, newlock, steps + 1))
        return -1