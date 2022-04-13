import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0] * p[0] + p[1] * p[1], p))
        return [heapq.heappop(heap)[1] for i in range(k)]