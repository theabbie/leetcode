class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            if i < n - 1 and nums[i] + 1 == nums[i + 1]:
                dp[i] = 1 + dp[i + 1]
        res = []
        for i in range(n - k + 1):
            if dp[i] >= k:
                res.append(nums[i] + k - 1)
            else:
                res.append(-1)
        return res