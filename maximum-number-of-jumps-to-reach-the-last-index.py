class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if -target <= nums[i] - nums[j] <= target:
                    dp[i] = max(dp[i], 1 + dp[j])
        if dp[0] == float('-inf'):
            return -1
        return dp[0]