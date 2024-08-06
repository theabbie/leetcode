class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        for mask in range(1 << n):
            dist = [[float('inf')] * n for _ in range(n)]
            for u, v, w in roads:
                if not mask & (1 << u) and not mask & (1 << v):
                    dist[u][v] = dist[v][u] = min(dist[u][v], dist[v][u], w)
            for j in range(n):
                if not mask & (1 << j):
                    dist[j][j] = 0
                for i in range(n):
                    for k in range(n):
                        dist[i][k] = min(dist[i][k], dist[i][j] + dist[j][k])
            valid = True
            for i in range(n):
                for j in range(n):
                    if not mask & (1 << i) and not mask & (1 << j) and dist[i][j] > maxDistance:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                res += 1
        return res