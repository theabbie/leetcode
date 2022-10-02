class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, 1 + (n + i) // 2):
                if s[i : j] == s[j : 2 * j - i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[0]