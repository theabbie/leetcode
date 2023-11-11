class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        lcp = [[0] * n for _ in range(n)]
        dp = [1] * n
        if n % 2 == 0:
            dp[n // 2] = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                lcp[i][j] = 1 + lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 1
                if text[i] != text[j]:
                    lcp[i][j] = 0
        for i in range(n // 2, -1, -1):
            for l in range(1, 1 + (n - 2 * i) // 2):
                if lcp[i][n - i - l] >= l:
                    dp[i] = max(dp[i], 2 + dp[i + l])
        return dp[0]