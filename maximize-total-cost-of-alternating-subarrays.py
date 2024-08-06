class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + (-1 if i % 2 == 1 else 1) * nums[i]
        dp = [0] * (n + 1)
        mx = p[n]
        mn = p[n]
        for i in range(n - 1, -1, -1):
            if i % 2 == 0:
                dp[i] = mx - p[i]
            else:
                dp[i] = p[i] - mn
            mx = max(mx, p[i] + dp[i])
            mn = min(mn, p[i] - dp[i])
        return dp[0]