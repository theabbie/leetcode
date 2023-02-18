import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (nums[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        heap.sort(key = lambda x: x[1])
        return [h[0] for h in heap]