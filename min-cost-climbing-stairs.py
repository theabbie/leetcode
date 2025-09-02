class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 2)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])