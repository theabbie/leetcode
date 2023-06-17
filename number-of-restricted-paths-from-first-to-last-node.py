from collections import defaultdict
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        graph = defaultdict(set)
        for a, b, w in edges:
            graph[a - 1].add((b - 1, w))
            graph[b - 1].add((a - 1, w))
        dist = [float('inf')] * n
        dist[n - 1] = 0
        heap = [(0, n - 1)]
        while len(heap) > 0:
            currdist, curr = heapq.heappop(heap)
            for j, w in graph[curr]:
                if dist[j] > currdist + w:
                    dist[j] = currdist + w
                    heapq.heappush(heap, (dist[j], j))
        count = [0] * n
        count[n - 1] = 1
        for curr in sorted(range(n), key = lambda i: dist[i]):
            for j, w in graph[curr]:
                if dist[j] < dist[curr]:
                    count[curr] += count[j]
                    count[curr] %= M
        return count[0]
