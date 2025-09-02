cost = [[0] * 26 for _ in range(26)]
for i in range(26):
    for j in range(26):
        c = float('inf')
        for t in range(26):
            c = min(c, min(abs(i - t), 26 - abs(i - t)) + min(abs(j - t), 26 - abs(j - t)))
        cost[i][j] = c

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for r in range(k + 1):
                dp[i][i][r] = 1
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                for r in range(k + 1):
                    res = max(dp[i + 1][j][r], dp[i][j - 1][r])
                    c = cost[ord(s[i]) - 97][ord(s[j]) - 97]
                    if c <= r:
                        candidate = 2 + (dp[i + 1][j - 1][r - c] if i + 1 <= j - 1 else 0)
                        res = max(res, candidate)
                    dp[i][j][r] = res
        return dp[0][n - 1][k]