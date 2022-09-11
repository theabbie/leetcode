from collections import defaultdict

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(i, n + 1):
                if i == 0:
                    dp[i][j] = 1
                elif t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] += dp[i][j - 1]
        return dp[m][n]
                    