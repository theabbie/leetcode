class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dc = set(dictionary)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = min(dp[i], 1 + dp[i - 1])
            for l in range(1, i + 1):
                if s[i-l:i] in dc:
                    dp[i] = min(dp[i], dp[i - l])
        return dp[n]