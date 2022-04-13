class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSoFar = float('-inf')
        maxEndingHere = 0
        for i in range(n):
            maxEndingHere += nums[i]
            maxSoFar = max(maxSoFar, maxEndingHere)
            maxEndingHere = max(maxEndingHere, 0)
        return maxSoFar