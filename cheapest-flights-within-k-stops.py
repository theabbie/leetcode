from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))
        dist = defaultdict(lambda: float('inf'))
        dist[(src, k)] = 0
        heap = []
        for i in range(n):
            heapq.heappush(heap, (dist[(i, k)], i, k))
        while len(heap) > 0:
            d, curr, rem = heapq.heappop(heap)
            for j, c in graph[curr]:
                newrem = rem - 1
                if j == dst:
                    newrem = rem
                if newrem >= 0 and dist[(j, newrem)] > d + c:
                    dist[(j, newrem)] = d + c
                    heapq.heappush(heap, (dist[(j, newrem)], j, newrem))
        res = float('inf')
        for rem in range(k + 1):
            res = min(res, dist[(dst, rem)])
        if res == float('inf'):
            return -1
        return res