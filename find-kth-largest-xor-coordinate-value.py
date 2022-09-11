import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev = [0] * n
        heap = []
        for i in range(m):
            curr = 0
            for j in range(n):
                curr ^= matrix[i][j]
                val = curr ^ prev[j]
                prev[j] = val
                heapq.heappush(heap, val)
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0]