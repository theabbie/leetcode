class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        p = {pow(5, i) for i in range(10)}
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            curr = 0
            for j in range(i, n):
                curr = 2 * curr + int(s[j])
                if curr in p:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        if dp[0] == float('inf'):
            return -1
        return dp[0]