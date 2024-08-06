import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-((p + 1) / (t + 1) - p / t), p, t))
        for _ in range(extraStudents):
            diff, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-((p + 2) / (t + 2) - (p + 1) / (t + 1)), p + 1, t + 1))
        ratio = 0
        for diff, p, t in heap:
            ratio += p / t
        return ratio / len(classes)