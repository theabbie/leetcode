from collections import deque

class Solution:
    def neighbours(self, a, b, m, n):
        for i in range(a - 1, a + 2):
            for j in range(b - 1, b + 2):
                if (i, j) != (a, b) and 0 <= i < m and 0 <= j < n:
                    yield (i, j)
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        path = deque([(0, 0, 1)])
        visited = {(0, 0)}
        while len(path) > 0:
            a, b, d = path.popleft()
            if (a, b) == (m - 1, n - 1):
                return d
            for i, j in self.neighbours(a, b, m, n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    path.append((i, j, d + 1))
        return -1