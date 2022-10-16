class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        total = sum([ord(c) for c in s1]) + sum([ord(c) for c in s2])
        dp=[[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return total - 2 * dp[-1][-1]