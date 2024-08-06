from collections import defaultdict
import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [set() for _ in range(n)]
        for u, v, w in edges:
            graph[u].add((v, w))
            graph[v].add((u, w))
        res = [-1] * n
        heap = [(0, 0)]
        dist = [float('inf')] * n
        dist[0] = 0
        while len(heap) > 0:
            d, curr = heapq.heappop(heap)
            if res[curr] == -1:
                res[curr] = d
            for j, w in list(graph[curr]):
                if disappear[j] > d + w and dist[j] > d + w:
                    dist[j] = d + w
                    heapq.heappush(heap, (dist[j], j))
                if disappear[j] <= d + w:
                    graph[curr].remove((j, w))
                    if (curr, w) in graph[j]:
                        graph[j].remove((curr, w))
        return res