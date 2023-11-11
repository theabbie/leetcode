class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        left = [[] for _ in range(n + 1)]
        for i in range(n + 1):
            left[min(i + ranges[i], n)].append(max(i - ranges[i], 0))
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for l in left[i]:
                dp[i] = min(dp[i], 1 + min(dp[l:i+1]))
        if dp[n] == float('inf'):
            return -1
        return dp[n]