import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        graph = defaultdict(set)
        for u, v, d in roads:
            graph[u].add((v, d))
            graph[v].add((u, d))
        dist = defaultdict(lambda: float('inf'))
        dist[0] = 0
        heap = [(0, 0)]
        ctr = defaultdict(int)
        ctr[0] = 1
        while len(heap) > 0:
            currdist, curr = heapq.heappop(heap)
            for j, d in graph[curr]:
                if dist[j] > currdist + d:
                    ctr[j] = ctr[curr]
                    dist[j] = dist[curr] + d
                    heapq.heappush(heap, (dist[j], j))
                elif dist[j] == currdist + d:
                    ctr[j] = (ctr[j] + ctr[curr]) % M
        return ctr[n - 1]