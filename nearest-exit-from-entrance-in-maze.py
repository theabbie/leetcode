from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        i, j = entrance
        maze[i][j] = "+"
        q = deque([(i, j, 0)])
        while len(q) > 0:
            i, j, d = q.pop()
            if d > 0 and min(i, m - i - 1, j, n - j - 1) == 0:
                return d
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                    maze[x][y] = "+"
                    q.appendleft((x ,y, d + 1))
        return -1