class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for i, j, d in edges:
            dist[i][j] = d
            dist[j][i] = d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        res = (float('inf'), 0)
        for i in range(n):
            curr = len([d for d in dist[i] if d <= distanceThreshold])
            res = min(res, (curr, -i))
        return -res[1]