import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) >= k:
            return 0
        heap = []
        for el in nums:
            heapq.heappush(heap, el)
        res = 0
        while len(heap) >= 2:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            val = min(x, y) * 2 + max(x, y)
            heapq.heappush(heap, val)
            res += 1
            if heap[0] >= k:
                break
        return res