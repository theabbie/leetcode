class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            m = float('-inf')
            for j in range(i, min(i + k, n)):
                m = max(m, arr[j])
                dp[i] = max(dp[i], m * (j - i + 1) + dp[j + 1])
        return dp[0]