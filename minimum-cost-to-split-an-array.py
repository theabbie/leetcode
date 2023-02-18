from collections import Counter

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            curr = 0
            ctr = Counter()
            for j in range(i, n):
                ctr[nums[j]] += 1
                if ctr[nums[j]] == 1:
                    curr += 1
                elif ctr[nums[j]] == 2:
                    curr -= 1
                dp[i] = min(dp[i], k + j - i + 1 - curr + dp[j + 1])
        return dp[0]