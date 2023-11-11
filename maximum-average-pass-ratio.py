import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        diff = lambda a, b: (a + 1) / (b + 1) - a / b
        heap = []
        for a, b in classes:
            heapq.heappush(heap, (-diff(a, b), a, b))
        for _ in range(extraStudents):
            currdiff, a, b = heapq.heappop(heap)
            heapq.heappush(heap, (-diff(a + 1, b + 1), a + 1, b + 1))
        res = 0
        for diff, a, b in heap:
            res += a / b
        res /= n
        return res