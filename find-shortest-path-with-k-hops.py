from collections import *
import heapq

class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = defaultdict(lambda: float('inf'))
        dist[(s, k)] = 0
        heap = [(0, s, k)]
        while heap:
            dt, i, rem = heapq.heappop(heap)
            if i == d:
                return dt
            for j, w in graph[i]:
                if dist[(j, rem)] > dt + w:
                    dist[(j, rem)] = dt + w
                    heapq.heappush(heap, (dist[(j, rem)], j, rem))
                if rem == 0:
                    continue
                if dist[(j, rem - 1)] > dt:
                    dist[(j, rem - 1)] = dt
                    heapq.heappush(heap, (dist[(j, rem - 1)], j, rem - 1))