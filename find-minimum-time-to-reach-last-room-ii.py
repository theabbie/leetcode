import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0, True)]
        while heap:
            d, i, j, even = heapq.heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return d
            cost = 1 if even else 2
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and max(d, moveTime[x][y]) + cost < dist[x][y]:
                    dist[x][y] = max(d, moveTime[x][y]) + cost
                    heapq.heappush(heap, (dist[x][y], x, y, not even))