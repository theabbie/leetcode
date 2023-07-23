from collections import defaultdict

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + int(nums[i] == 1)
        dp = [0] * (n + 1)
        dp[n] = 1
        prefdp = defaultdict(int)
        prefdp[p[n]] = dp[n]
        for i in range(n - 1, -1, -1):
            dp[i] += prefdp[p[i] + 1]
            prefdp[p[i]] += dp[i]
            dp[i] %= M
            prefdp[p[i]] %= M
        return dp[0]