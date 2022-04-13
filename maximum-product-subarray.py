class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxSoFar = nums[0]
        maxEndingHere = nums[0]
        minEndingHere = nums[0]
        for i in range(1, n):
            temp = max(nums[i], maxEndingHere * nums[i], minEndingHere * nums[i])
            minEndingHere = min(nums[i], maxEndingHere * nums[i], minEndingHere * nums[i])
            maxEndingHere = temp
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar