import heapq

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGap = float('-inf')
        n = len(nums)
        if n <= 1:
            return 0
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        while len(nums) > 0:
            curr = heapq.heappop(nums)
            maxGap = max(maxGap, curr - prev)
            prev = curr
        return maxGap