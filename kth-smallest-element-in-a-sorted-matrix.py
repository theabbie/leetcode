import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])
        for i in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)