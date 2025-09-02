class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        M = max(nums) - min(nums)
        n = len(nums)
        dp = defaultdict(Counter)
        res = 1
        for i in range(n - 1, -1, -1):
            l = 1
            for diff in range(M + 1):
                l = max(l, 1 + dp[nums[i] - diff][diff], 1 + dp[nums[i] + diff][diff])
                dp[nums[i]][diff] = l
                res = max(res, l)
        return res