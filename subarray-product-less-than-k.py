class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] == nums[i + 1] == 1:
                dp[i] = 1 + dp[i + 1]
        res = 0
        for i in range(n):
            p = 1
            j = i
            while j < n and p * nums[j] < k:
                p *= nums[j]
                res += dp[j]
                j += dp[j]
        return res