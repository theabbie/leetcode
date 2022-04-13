class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxSum = float('-inf')
        for i in range(n // 2):
            maxSum = max(maxSum, nums[i] + nums[n - 1 - i])
        return maxSum