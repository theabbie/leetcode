import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = total
        heap = []
        for el in nums:
            heapq.heappush(heap, -el)
        res = 0
        while 2 * curr > total:
            val = -heapq.heappop(heap)
            curr -= val / 2
            heapq.heappush(heap, -val / 2)
            res += 1
        return res