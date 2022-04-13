import heapq
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (abs(x - num), num))
        kclosest = []
        for i in range(k):
            bisect.insort(kclosest, heapq.heappop(heap)[1])
        return kclosest