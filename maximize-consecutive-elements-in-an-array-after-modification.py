from collections import *

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(Counter(nums).items(), reverse = True)
        res = 1
        dp = defaultdict(int)
        for el, f in nums:
            if f == 1:
                dp[el] = max(dp[el], 1 + dp[el + 1])
                dp[el + 1] = max(dp[el + 1], 1 + dp[el + 2])
            else:
                dp[el] = max(dp[el], 1 + dp[el + 1], 2 + dp[el + 2])
                dp[el + 1] = max(dp[el + 1], 1 + dp[el + 2])
        for el in dp:
            res = max(res, dp[el])
        return res