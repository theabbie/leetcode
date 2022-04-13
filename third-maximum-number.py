import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dup = set()
        heap = []
        for num in nums:
            if num not in dup:
                heapq.heappush(heap, num)
                if len(heap) > 3:
                    heapq.heappop(heap)
                dup.add(num)
        if len(heap) == 3:
            return heap[0]
        else:
            return max(nums)