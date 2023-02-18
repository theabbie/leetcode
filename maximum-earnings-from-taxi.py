from collections import defaultdict

class Solution:
    def maxTaxiEarnings(self, n, rides):
        dp = [0] * (n + 1)
        graph = defaultdict(lambda: defaultdict(int))
        for a, b, d in rides:
            graph[a - 1][b - 1] = max(graph[a - 1][b - 1], b - a + d)
        for i in range(n - 1, -1, -1):
            for j in graph[i]:
                dp[i] = max(dp[i], graph[i][j] + dp[j])
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]