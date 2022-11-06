from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def neighbours(i, j):
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    yield (x, y)
        indegree = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for x, y in neighbours(i, j):
                    if matrix[x][y] > matrix[i][j]:
                        indegree[x][y] += 1
        q = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.appendleft((i, j))
        dist = [[1] * n for _ in range(m)]
        res = 1
        while len(q) > 0:
            i, j = q.pop()
            for x, y in neighbours(i, j):
                if matrix[x][y] > matrix[i][j]:
                    indegree[x][y] -= 1
                    if indegree[x][y] == 0:
                        q.appendleft((x, y))
                elif matrix[x][y] < matrix[i][j]:
                    dist[i][j] = max(dist[i][j], 1 + dist[x][y])
                    res = max(res, dist[i][j])
        return res