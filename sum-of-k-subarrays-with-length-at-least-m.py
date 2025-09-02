class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        dp = [[float('-inf')] * (k + 2) for _ in range(n + 1)]
        dp[n][0] = 0
        for rem in range(k + 1):
            best = [float('-inf')] * (n + 2)
            for t in range(n, -1, -1):
                best[t] = max(best[t + 1], p[t] + dp[t][rem - 1])
            for i in range(n - 1, -1, -1):
                dp[i][rem] = dp[i + 1][rem]
                if i + m <= n:
                    dp[i][rem] = max(dp[i][rem], best[i + m] - p[i])
        return dp[0][k]