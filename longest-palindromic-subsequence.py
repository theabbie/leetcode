class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                dp[i][j] = 2 * int(s[i] == s[j]) + dp[i + 1][j - 1]
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])
        return max(max(r) for r in dp)