import heapq
from collections import defaultdict

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[0 if cell == 0 else float('inf') for cell in row] for row in mat]
        heap = []
        deleted = defaultdict(int)
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(heap, (dist[i][j], i, j))
        while len(heap) > 0:
            currdist, i, j = heapq.heappop(heap)
            while (currdist, i, j) in deleted and len(heap) > 0:
                deleted[(currdist, i, j)] -= 1
                if deleted[(currdist, i, j)] == 0:
                    del deleted[(currdist, i, j)]
                currdist, i, j = heapq.heappop(heap)
            adj = []
            if i > 0:
                adj.append((i - 1, j))
            if i < m - 1:
                adj.append((i + 1, j))
            if j > 0:
                adj.append((i, j - 1))
            if j < n - 1:
                adj.append((i, j + 1))
            for a, b in adj:
                if dist[a][b] > 1 + currdist:
                    deleted[(dist[a][b], a, b)] += 1
                    dist[a][b] = 1 + currdist
                    heapq.heappush(heap, (1 + currdist, a, b))
        return dist