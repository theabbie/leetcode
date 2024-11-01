class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        v = [0] * n
        for i in targetIndices:
            v[i] = 1
        dp = [float('-inf')] * (m + 1)
        ndp = [float('-inf')] * (m + 1)
        dp[m] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m + 1):
                if j < m and source[i] == pattern[j]:
                    ndp[j] = dp[j + 1]
                ndp[j] = max(ndp[j], v[i] + dp[j])
            dp, ndp = ndp, dp
        return dp[0]