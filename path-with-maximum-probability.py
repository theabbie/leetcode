from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        res = 0
        graph = defaultdict(set)
        for i in range(len(edges)):
            graph[edges[i][0]].add((edges[i][1], succProb[i]))
            graph[edges[i][1]].add((edges[i][0], succProb[i]))
        heap = []
        dist = defaultdict(int)
        dist[start] = 1
        for i in range(n):
            heapq.heappush(heap, (-dist[i], i))
        while len(heap) > 0:
            currp, curr = heapq.heappop(heap)
            for j, p in graph[curr]:
                if dist[j] < dist[curr] * p:
                    dist[j] = dist[curr] * p
                    heapq.heappush(heap, (-dist[j], j))
        return dist[end]