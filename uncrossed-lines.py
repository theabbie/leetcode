class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])
        return dp[0][0]