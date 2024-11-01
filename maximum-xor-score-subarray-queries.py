class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        msb = [-1] * (n + 1)
        for i in range(1, n + 1):
            msb[i] = 1 + msb[i // 2]
        msb[0] = 0
        dp = [[0] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l - 1, -1, -1):
                if l == 0:
                    dp[i][i + l] = nums[i]
                else:
                    w = l & ~(1 << msb[l])
                    dp[i][i + l] = dp[i][i + w] ^ dp[i + l - w][i + l]
        for l in range(1, n):
            for i in range(n - l - 1, -1, -1):
                dp[i][i + l] = max(dp[i][i +  l], dp[i + 1][i + l], dp[i][i + l - 1])
        return [dp[l][r] for l, r in queries]