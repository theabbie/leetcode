from collections import *
import heapq

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        diag = 0
        for i in range(n):
            diag += fruits[i][i]
        def topright():
            dist = [[0] * n for _ in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(n):
                    dist[i][j] = fruits[i][j]
                    for di, dj in [(1, -1), (1, 0), (1, 1)]:
                        x = i + di
                        y = j + dj
                        if not 0 <= x < n or not 0 <= y < n:
                            continue
                        if x == y and (x, y) != (n - 1, n - 1):
                            continue
                        if (i < j) != (x < y) and (x, y) != (n - 1, n - 1):
                            continue
                        dist[i][j] = max(dist[i][j], fruits[i][j] + dist[x][y])
            return dist[0][n - 1]
        def bottomleft():
            dist = [[0] * n for _ in range(n)]
            for j in range(n - 1, -1, -1):
                for i in range(n):
                    dist[i][j] = fruits[i][j]
                    for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                        x = i + di
                        y = j + dj
                        if not 0 <= x < n or not 0 <= y < n:
                            continue
                        if x == y and (x, y) != (n - 1, n - 1):
                            continue
                        if (i < j) != (x < y) and (x, y) != (n - 1, n - 1):
                            continue
                        dist[i][j] = max(dist[i][j], fruits[i][j] + dist[x][y])
            return dist[n - 1][0]
        return diag + topright() + bottomleft() - 2 * fruits[n - 1][n - 1]