class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        revdp = [1] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], 1 + dp[i])
        for j in range(n - 1, -1, -1):
            for i in range(j + 1, n):
                if nums[i] < nums[j]:
                    revdp[j] = max(revdp[j], 1 + revdp[i])
        used = 0
        for i in range(n):
            if dp[i] > 1 and revdp[i] > 1:
                used = max(used, dp[i] + revdp[i] - 1)
        return n - used