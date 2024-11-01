class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[float('inf')] * k for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            p = [float('inf')] * (k + 1)
            s = [float('inf')] * (k + 1)
            for j in range(k):
                p[j + 1] = min(p[j], dp[i - 1][j])
                s[j + 1] = min(s[j], dp[i - 1][k - j - 1])
            for j in range(k):
                dp[i][j] = min(dp[i][j], min(p[j], s[k - j - 1]) + costs[i][j])
        return min(dp[n - 1])