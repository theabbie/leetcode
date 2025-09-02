class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0
        for i in range(n - 1, -1, -1):
            for rem in range(1, k + 1):
                s = 0
                for j in range(i, n):
                    s += nums[j]
                    dp[i][rem] = max(dp[i][rem], s / (j - i + 1) + dp[j + 1][rem - 1])
        return dp[0][k]