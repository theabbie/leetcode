class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        dp = [1] * n
        longest = {}
        for i in range(n):
            if (nums[i] * nums[i]) in longest:
                dp[i] = 1 + longest[nums[i] * nums[i]]
            longest[nums[i]] = max(longest.get(nums[i], 1), dp[i])
        res = max(dp)
        if res < 2:
            return -1
        return res