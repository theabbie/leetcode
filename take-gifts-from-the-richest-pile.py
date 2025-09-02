import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for el in gifts:
            heapq.heappush(heap, -el)
        for _ in range(k):
            v = -heapq.heappop(heap)
            heapq.heappush(heap, -int(v ** 0.5))
        return -sum(heap)