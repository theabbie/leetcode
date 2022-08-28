from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        res = 0
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            prev = dp[i - 1][diff]
            dp[i][diff] = prev + 1
            res += prev
        return res