class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                dp[i] += dp[i + 1]
        return sum(dp)