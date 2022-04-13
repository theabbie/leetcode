import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n):
            for j in range(n - 1, i, -1):
                heapq.heappush(heap, (-arr[i] / arr[j], (arr[i], arr[j])))
                if len(heap) > k:
                    heapq.heappop(heap)
        return list(heap[0][1])