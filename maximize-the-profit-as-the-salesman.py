class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        left = [[] for _ in range(n + 1)]
        for a, b, gold in offers:
            left[b + 1].append((a, gold))
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            for l, g in left[i]:
                dp[i] = max(dp[i], g + dp[l])
        return dp[n]