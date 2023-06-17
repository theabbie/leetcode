class Solution:
    def stoneGameIII(self, arr):
        n = len(arr)
        dp = [float('-inf')] * (n + 3)
        dp[n] = dp[n + 1] = dp[n + 2] = 0
        for i in range(n - 1, -1, -1):
            s = 0
            for j in range(i, min(i + 3, n)):
                s += arr[j]
                dp[i] = max(dp[i], s - dp[j + 1])
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"