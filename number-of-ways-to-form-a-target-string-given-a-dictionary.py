from collections import Counter

M = 10 ** 9 + 7

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(target)
        n = len(words[0])
        chars = [Counter() for _ in range(n)]
        for w in words:
            for i in range(n):
                chars[i][w[i]] += 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[m][i] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if chars[j][target[i]] > 0:
                    dp[i][j] += chars[j][target[i]] * dp[i + 1][j + 1]
                dp[i][j] %= M
        return dp[0][0]