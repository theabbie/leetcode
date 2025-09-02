class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dp[i] = 1 + dp[i + 1]
        for i in range(n - 2 * k + 1):
            if dp[i] >= k and dp[i + k] >= k:
                return True
        return False