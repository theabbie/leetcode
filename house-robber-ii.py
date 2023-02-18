class Solution:
    def maxrob(self, nums):
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.maxrob(nums[:-1]), self.maxrob(nums[1:]))