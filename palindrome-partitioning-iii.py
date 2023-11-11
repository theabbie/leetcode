from collections import defaultdict
import heapq

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        graph = defaultdict(set)
        for i in range(n):
            for x, y in [(i, i), (i, i + 1)]:
                minops = 0
                while x >= 0 and y < n:
                    minops += int(s[x] != s[y])
                    graph[x].add((y + 1, minops))
                    x -= 1
                    y += 1
        dist = defaultdict(lambda: float('inf'))
        heap = [(0, 0, k)]
        dist[(0, k)] = 0
        while len(heap) > 0:
            d, curr, rem = heapq.heappop(heap)
            if curr == n and rem == 0:
                return d
            if rem == 0:
                continue
            for j, cost in graph[curr]:
                if dist[(j, rem - 1)] > d + cost:
                    dist[(j, rem - 1)] = d + cost
                    heapq.heappush(heap, (dist[(j, rem - 1)], j, rem - 1))