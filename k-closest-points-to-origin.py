import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(p[0] * p[0] + p[1] * p[1], p) for p in points]
        heapq.heapify(points)
        return [heapq.heappop(points)[1] for i in range(k)]