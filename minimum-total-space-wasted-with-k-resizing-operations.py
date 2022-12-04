class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k += 1
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(k + 1):
            dp[n][i] = 0
        for i in range(n - 1, -1, -1):
            for l in range(1, k + 1):
                mval = float('-inf')
                total = 0
                for j in range(i, n):
                    mval = max(mval, nums[j])
                    total += nums[j]
                    dp[i][l] = min(dp[i][l], (j - i + 1) * mval - total + dp[j + 1][l - 1])
        return dp[0][k]