from collections import defaultdict
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = [0]
        deleted = defaultdict(int)
        points = []
        for a, b, h in buildings:
            points.append((a, -h, -1))
            points.append((b, h, 1))
        points.sort()
        res = []
        for x, y, p in points:
            y = abs(y)
            if p == -1:
                while len(heap) > 0 and deleted[heap[0]] > 0:
                    deleted[heap[0]] -= 1
                    heapq.heappop(heap)
                if y > -heap[0]:
                    res.append((x, y))
                heapq.heappush(heap, -y)
            else:
                deleted[-y] += 1
                while len(heap) > 0 and deleted[heap[0]] > 0:
                    deleted[heap[0]] -= 1
                    heapq.heappop(heap)
                if y > -heap[0]:
                    res.append((x, -heap[0]))
        return res