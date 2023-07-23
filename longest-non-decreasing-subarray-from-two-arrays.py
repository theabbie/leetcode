class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        arr = [nums1, nums2]
        dp = [[1, 1] for _ in range(n)]
        res = 1
        for i in range(n - 2, -1, -1):
            for j in range(2):
                for k in range(2):
                    if arr[j][i] <= arr[k][i + 1]:
                        dp[i][j] = max(dp[i][j], 1 + dp[i + 1][k])
                        res = max(res, dp[i][j])
        return res