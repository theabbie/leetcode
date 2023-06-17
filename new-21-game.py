class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        L = max(k + maxPts + 1, n + 1)
        dp = [0] * L
        dpsum = [0]
        for i in range(L - 1, k - 1, -1):
            if k <= i <= n:
                dp[i] = 1
            dpsum.append(dpsum[-1] + dp[i])
        for i in range(k - 1, -1, -1):
            dp[i] = (dpsum[-1] - dpsum[-maxPts - 1]) / maxPts
            dpsum.append(dpsum[-1] + dp[i])
        return dp[0]