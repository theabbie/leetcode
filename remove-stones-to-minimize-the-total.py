import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        total = 0
        for el in piles:
            heapq.heappush(heap, -el)
            total += el
        while k:
            pile = -heapq.heappop(heap)
            heapq.heappush(heap, -pile + pile // 2)
            total -= pile // 2
            k -= 1
        return total