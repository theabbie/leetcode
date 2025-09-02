import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while len(nums) > 1 and nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            heapq.heappush(nums, a * 2 + b)
            res += 1
        return res