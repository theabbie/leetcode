import numpy as np

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = np.array([n] * n)
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                dp[i] = 1 + np.min(dp[i : i + nums[i] + 1])
        return dp[0]