import numpy as np

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)
        M = max(nums) + k + 1
        dp = np.ones(n, dtype=int)
        vals = np.zeros(M, dtype=int)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + np.max(vals[nums[i] + 1 : nums[i] + k + 1])
            vals[nums[i]] = max(vals[nums[i]], dp[i])
        return np.max(dp)