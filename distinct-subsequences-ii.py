class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        prev = {}
        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            if s[i - 1] in prev:
                dp[i] -= dp[prev[s[i - 1]]]
            prev[s[i - 1]] = i - 1
        dp[n] -= 1
        return dp[n] % (10 ** 9 + 7)