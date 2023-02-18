class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 2)
        mval = float('-inf')
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i], mval - prices[i])
            dp[i] = max(dp[i], dp[i + 1])
            mval = max(mval, prices[i] + dp[i + 2])
        return dp[0]