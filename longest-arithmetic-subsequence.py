from collections import defaultdict, Counter

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter(nums)
        res = max(ctr.values())
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        for j in range(n):
            for i in range(j):
                d = nums[j] - nums[i]
                if d != 0:
                    dp[j][d] = max(dp[j][d], 1 + dp[i][d])
                    res = max(res, dp[j][d])
        return res