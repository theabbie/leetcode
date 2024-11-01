class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        dp[i][k] = min(dp[i][k], dp[i - 1][j] + costs[i][k])
        return min(dp[n - 1])