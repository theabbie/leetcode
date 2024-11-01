class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0] * k for _ in range(n + 1)]
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(k):
                for l in range(1, 3):
                    if i > l:
                        dp[i][j] += s[i - l] - dp[i - l][j]
                    elif i == l:
                        dp[i][j] += 1
            s[i] = sum(dp[i])
        return sum(dp[n])