import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            heapq.heappush(heap, int(num))
            if len(heap) > k:
                heapq.heappop(heap)
        return str(heap[0])