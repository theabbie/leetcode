import heapq

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[0 if cell == 0 else float('inf') for cell in row] for row in mat]
        heap = []
        deleted = {}
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
            if i > 0 and dist[i - 1][j] > 1 + currdist:
                deleted[(dist[i - 1][j], i - 1, j)] = deleted.get((dist[i - 1][j], i - 1, j), 0) + 1
                dist[i - 1][j] = 1 + currdist
                heapq.heappush(heap, (1 + currdist, i - 1, j))
            if i < m - 1 and dist[i + 1][j] > 1 + currdist:
                deleted[(dist[i + 1][j], i + 1, j)] = deleted.get((dist[i + 1][j], i + 1, j), 0) + 1
                dist[i + 1][j] = 1 + currdist
                heapq.heappush(heap, (1 + currdist, i + 1, j))
            if j > 0 and dist[i][j - 1] > 1 + currdist:
                deleted[(dist[i][j - 1], i, j - 1)] = deleted.get((dist[i][j - 1], i, j - 1), 0) + 1
                dist[i][j - 1] = 1 + currdist
                heapq.heappush(heap, (1 + currdist, i, j - 1))
            if j < n - 1 and dist[i][j + 1] > 1 + currdist:
                deleted[(dist[i][j + 1], i, j + 1)] = deleted.get((dist[i][j + 1], i, j + 1), 0) + 1
                dist[i][j + 1] = 1 + currdist
                heapq.heappush(heap, (1 + currdist, i, j + 1))
        return dist