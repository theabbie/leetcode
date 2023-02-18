import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for el in nums:
            heapq.heappush(heap, -el)
        for _ in range(k):
            curr = heapq.heappop(heap)
            curr *= -1
            res += curr
            heapq.heappush(heap, -math.ceil(curr / 3))
        return res