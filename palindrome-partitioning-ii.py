class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        prevpal = [True] * n
        pal = [False] * n
        for i in range(1, n + 1):
            for j in range(i - 1, n):
                pal[j] = True
            l = 1
            while l <= i:
                if i >= 2 and i - l < n - 1:
                    pal[i - l] = s[i - l] == s[i - 1] and prevpal[i - l + 1]
                if pal[i - l]:
                    dp[i] = min(dp[i], 1 + dp[i - l])
                l += 1
            prevpal, pal = pal, prevpal
        return dp[n] - 1